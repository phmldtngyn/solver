import json
import os
import sys
import urllib.request
from pathlib import Path

# Ép giới hạn 4 luồng giống orchestrator.py
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "4")

import yaml
from orchestrator import load_env_file, resolve_openrouter_key
from context_packer import build_shared_system_context
from prompts import SYSTEM_ROLES
from sandbox_executor import run_verification_script

EXPECTED_AGENTS = [
    "1_commander",
    "2_coordinator",
    "3_prover",
    "4_local_code",
    "5_numeric_verifier",
    "6_auditor",
    "7_latex",
]

def status(tag: str, msg: str):
    print(f"[{tag:<4}] {msg}")

def main():
    print("============================================================")
    print("   KIỂM TRA TỔNG THỂ KIẾN TRÚC HỆ THỐNG 7 AGENT (PRE-FLIGHT) ")
    print("============================================================\n")
    errors = 0

    # 1. Kiểm tra thư viện & giới hạn CPU
    print("--- 1. MÔI TRƯỜNG & GIỚI HẠN TÀI NGUYÊN ---")
    for pkg in ("openai", "yaml", "numpy", "scipy", "sympy"):
        try:
            __import__(pkg)
        except ImportError:
            status("FAIL", f"Thiếu thư viện Python: {pkg}")
            errors += 1
    if errors == 0:
        status("PASS", f"Python {sys.version.split()[0]} & đủ 5 thư viện lõi (openai, yaml, numpy, scipy, sympy)")
    status("PASS", f"Giới hạn luồng CPU: OMP_NUM_THREADS={os.environ.get('OMP_NUM_THREADS')}")

    # 2. Kiểm tra khóa API OpenRouter
    print("\n--- 2. BẢO MẬT & KHÓA API ---")
    load_env_file()
    api_key = resolve_openrouter_key()
    if api_key.startswith("sk-or-"):
        status("PASS", f"Đã nạp OPENROUTER_API_KEY hợp lệ ({api_key[:12]}...)")
    else:
        status("FAIL", "Không tìm thấy hoặc sai định dạng OPENROUTER_API_KEY trong .env")
        errors += 1

    # 3. Kiểm tra cấu trúc tệp & JSON checkpoint
    print("\n--- 3. CẤU TRÚC THƯ MỤC & SỔ CHECKPOINT ---")
    cfg = yaml.safe_load(Path("config.yaml").read_text(encoding="utf-8"))
    core_dir = Path(cfg["project"].get("core_dir", "core"))
    ctx_dir = Path(cfg["project"]["context_dir"])

    for req_file in [
        core_dir / "00_GLOBAL_CONSTITUTION.md",
        core_dir / "00_PROBLEM_SPEC.md",
        core_dir / "01_PROOF_STATE.md",
        core_dir / "02_CHECKPOINT.json",
        ctx_dir / cfg["project"]["dependency_map_file"],
        ctx_dir / cfg["project"]["roadmap_file"],
    ]:
        if req_file.exists() and req_file.stat().st_size > 0:
            status("PASS", f"Tồn tại & có dữ liệu: {req_file.as_posix()} ({req_file.stat().st_size:,} bytes)")
        else:
            status("FAIL", f"Thiếu hoặc rỗng: {req_file.as_posix()}")
            errors += 1

    ckpt_file = core_dir / "02_CHECKPOINT.json"
    if ckpt_file.exists():
        try:
            json.loads(ckpt_file.read_text(encoding="utf-8"))
            status("PASS", "02_CHECKPOINT.json đúng cú pháp JSON")
        except Exception as e:
            status("FAIL", f"02_CHECKPOINT.json lỗi cú pháp JSON: {e}")
            errors += 1

    # 4. Kiểm tra đồng bộ 7 Agent & đối chiếu tên model trên OpenRouter (miễn phí)
    print("\n--- 4. ĐỒNG BỘ 7 AGENT & ENDPOINT OPENROUTER ---")
    agents_cfg = cfg.get("agents", {})
    if list(agents_cfg.keys()) == EXPECTED_AGENTS and set(SYSTEM_ROLES.keys()) >= set(EXPECTED_AGENTS):
        status("PASS", "Khớp 100% thứ tự và định danh 7 Agent giữa config.yaml và prompts.py")
    else:
        status("FAIL", f"Lệch khóa Agent! config={list(agents_cfg.keys())}, prompts={list(SYSTEM_ROLES.keys())}")
        errors += 1

    live_models = {}
    if api_key:
        try:
            req = urllib.request.Request(
                "https://openrouter.ai/api/v1/models",
                headers={"Authorization": f"Bearer {api_key}"},
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8")).get("data", [])
                live_models = {m["id"]: m for m in data}
            status("PASS", f"Kết nối OpenRouter thành công (truy xuất {len(live_models)} models khả dụng)")
        except Exception as e:
            status("WARN", f"Không truy vấn được danh mục OpenRouter: {e}")

    for k in EXPECTED_AGENTS:
        acfg = agents_cfg[k]
        provider = acfg.get("provider", "openrouter")
        raw_model = acfg["model"]
        base_model = raw_model.split(":")[0]
        if provider != "openrouter":
            status("WARN", f"{k}: đang đặt provider='{provider}' ({raw_model}) — cần bật server local trước khi chạy")
        elif live_models:
            if base_model in live_models:
                ctx_len = live_models[base_model].get("context_length", "?")
                status("PASS", f"{k} -> {raw_model} (Khớp OpenRouter, context={ctx_len})")
            else:
                status("FAIL", f"{k} -> {raw_model}: KHÔNG TÌM THẤY '{base_model}' trên OpenRouter!")
                errors += 1
        else:
            status("WARN", f"{k} -> {raw_model} (Chưa đối chiếu được online)")

    # 5. Kiểm tra đóng gói ngữ cảnh & ước tính token cho cả 4 bài toán
    print("\n--- 5. ĐÓNG GÓI NGỮ CẢNH & DUNG LƯỢNG TOKEN (BÀI TOÁN 1..4) ---")
    for pid in (1, 2, 3, 4):
        try:
            packed = build_shared_system_context(cfg, pid)
            est_tokens = len(packed) // 4
            missing_tex = packed.count("[CẢNH BÁO: Chưa có file")
            note = f" (thiếu {missing_tex} file .tex rời, dùng bản tóm tắt context/)" if missing_tex else ""
            status("PASS", f"Bài toán {pid}: {len(packed):,} ký tự (~{est_tokens:,} tokens){note}")
        except Exception as e:
            status("FAIL", f"Bài toán {pid} lỗi đóng gói ngữ cảnh: {e}")
            errors += 1

    # 6. Kiểm tra Sandbox thực thi Python trên CPU local
    print("\n--- 6. SANDBOX THỰC THI CODE TRÊN CPU LOCAL ---")
    sample_reply = (
        "```python\n"
        "import numpy as np, scipy.integrate as spi, sympy as sp\n"
        "x = sp.Symbol('x', positive=True)\n"
        "assert sp.simplify(sp.diff(sp.log(1 + x), x) - 1/(1 + x)) == 0\n"
        "val, _ = spi.quad(lambda t: np.exp(-t), 0, np.inf)\n"
        "assert abs(val - 1.0) < 1e-9\n"
        "print('SANDBOX_CHECK_OK')\n"
        "```"
    )
    sb_out = run_verification_script(sample_reply)
    if "SANDBOX_CHECK_OK" in sb_out and "[SANDBOX EXIT CODE: 0]" in sb_out:
        status("PASS", "Sandbox chạy trơn tru numpy + scipy + sympy trên CPU local")
    else:
        status("FAIL", f"Sandbox lỗi:\n{sb_out}")
        errors += 1

    print("\n============================================================")
    if errors == 0:
        print(" KẾT LUẬN: TẤT CẢ 6 MẤU CHỐT ĐỀU ĐẠT [PASS]. SẴN SÀNG CHẠY THẬT!")
    else:
        print(f" KẾT LUẬN: PHÁT HIỆN {errors} LỖI [FAIL]. HÃY XỬ LÝ TRƯỚC KHI CHẠY THẬT.")
    print("============================================================")

if __name__ == "__main__":
    main()
