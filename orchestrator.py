import argparse
import json
import os
from datetime import datetime
from pathlib import Path

import yaml
from openai import OpenAI

from context_packer import build_shared_system_context
from prompts import SYSTEM_ROLES
from sandbox_executor import run_verification_script


def load_env_file(env_path: str = ".env"):
    p = Path(env_path)
    if not p.exists():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        val = v.strip().strip('"').strip("'")
        os.environ.setdefault(k.strip(), val)


def resolve_openrouter_key() -> str:
    for key_name in ("OPENROUTER_API_KEY", "OPENROUTER_KEY", "OR_API_KEY"):
        val = os.getenv(key_name)
        if val and val.strip():
            return val.strip()
    return ""


def get_client(provider: str) -> OpenAI:
    if provider == "local":
        return OpenAI(
            base_url=os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:11434/v1"),
            api_key=os.getenv("LOCAL_LLM_API_KEY", "ollama"),
        )
    api_key = resolve_openrouter_key()
    if not api_key:
        raise RuntimeError(
            "Thiếu API key OpenRouter. Hãy thêm dòng OPENROUTER_API_KEY=sk-or-v1-... vào tệp .env."
        )
    return OpenAI(
        base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
        api_key=api_key,
        default_headers={
            "HTTP-Referer": "https://github.com/phmldtngyn",
            "X-Title": "Self-Regulating Poisson Cascade Research System",
        },
    )


def call_agent(
    agent_key: str,
    agent_cfg: dict,
    shared_context: str,
    user_prompt: str,
    run_dir: Path,
    dry_run: bool = False,
) -> str:
    print(f"\n>>> Đang chạy [{agent_key}] - {agent_cfg['name']} ({agent_cfg['model']})...")

    if dry_run:
        if agent_key in ("4_local_code", "5_numeric_verifier"):
            content = (
                f"[DRY-RUN {agent_key.upper()}]\n```python\n"
                "import numpy as np\n"
                "c, delta_bar = 1.5, 2.0\n"
                "L = np.log(1 + c)\n"
                "B_star = np.log(c * delta_bar / L)\n"
                f"print('PASS [{agent_key}]: L=' + f'{{L:.4f}}, B*={{B_star:.4f}}')\n"
                "```"
            )
        else:
            content = (
                f"[DRY-RUN OK] {agent_key} ({agent_cfg['model']})\n"
                f"- Độ dài shared_context nhận được: {len(shared_context)} ký tự\n"
                f"- Độ dài user_prompt nhận được: {len(user_prompt)} ký tự"
            )
        out_file = run_dir / f"{agent_key}.md"
        out_file.write_text(content, encoding="utf-8")
        print(f"    [DRY-RUN] Đã lưu output tại: {out_file}")
        return content

    client = get_client(agent_cfg.get("provider", "openrouter"))
    system_msg = f"{SYSTEM_ROLES[agent_key]}\n\n========================================\n{shared_context}"

    resp = client.chat.completions.create(
        model=agent_cfg["model"],
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_prompt},
        ],
        temperature=agent_cfg.get("temperature", 0.2),
        max_tokens=agent_cfg.get("max_tokens", 4096),
    )

    content = resp.choices[0].message.content or ""
    out_file = run_dir / f"{agent_key}.md"
    out_file.write_text(content, encoding="utf-8")
    print(f"    Đã lưu output tại: {out_file}")
    return content


def main():
    parser = argparse.ArgumentParser(description="Điều phối 7 Agent nghiên cứu")
    parser.add_argument("--problem", type=int, required=True, choices=[1, 2, 3, 4], help="Số thứ tự bài toán mở (1..4)")
    parser.add_argument("--goal", type=str, default="", help="Mục tiêu cụ thể")
    parser.add_argument("--extra-tex", nargs="*", default=[], help="Danh sách file .tex bổ sung trong tex_sections/")
    parser.add_argument("--config", type=str, default="config.yaml", help="Đường dẫn file cấu hình")
    parser.add_argument("--dry-run", action="store_true", help="Chạy thử toàn bộ pipeline không gọi API")
    args = parser.parse_args()

    load_env_file()
    if not args.dry_run and not resolve_openrouter_key():
        raise RuntimeError(
            "Không tìm thấy OPENROUTER_API_KEY trong .env! Hãy thêm key trước khi chạy thật (hoặc dùng --dry-run)."
        )

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    prob_cfg = cfg["open_problems"][args.problem]
    goal = args.goal.strip() if args.goal.strip() else prob_cfg["default_goal"].strip()

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    mode_tag = "dryrun_" if args.dry_run else ""
    run_dir = Path(cfg["project"]["runs_dir"]) / f"{mode_tag}problem_{args.problem}_{ts}"
    run_dir.mkdir(parents=True, exist_ok=True)

    shared_context = build_shared_system_context(cfg, args.problem, args.extra_tex)
    (run_dir / "0_packed_context.txt").write_text(shared_context, encoding="utf-8")

    agents = cfg["agents"]
    outputs = {}

    # 1. Chủ điều hành (Fable 5.2)
    outputs["1_commander"] = call_agent(
        "1_commander",
        agents["1_commander"],
        shared_context,
        f"MỤC TIÊU CỤ THỂ:\n{goal}\n\nHãy xác định hướng tấn công chiến lược và các điều kiện bất biến.",
        run_dir,
        dry_run=args.dry_run,
    )

    # 2. Điều phối (Opus 5.5)
    outputs["2_coordinator"] = call_agent(
        "2_coordinator",
        agents["2_coordinator"],
        shared_context,
        f"MỤC TIÊU:\n{goal}\n\nCHỈ THỊ TỪ CHỦ ĐIỀU HÀNH (FABLE 5.2):\n{outputs['1_commander']}\n\n"
        f"Hãy phân rã thành các bổ đề trung gian và giao việc cho Prover, Local Code, Numeric Verifier.",
        run_dir,
        dry_run=args.dry_run,
    )

    # 3. Prover (Gemini 4 Neon)
    outputs["3_prover"] = call_agent(
        "3_prover",
        agents["3_prover"],
        shared_context,
        f"MỤC TIÊU:\n{goal}\n\nKẾ HOẠCH PHÂN RÃ TỪ ĐIỀU PHỐI (OPUS 5.5):\n{outputs['2_coordinator']}\n\n"
        f"Hãy viết chứng minh giải tích chi tiết từng bước.",
        run_dir,
        dry_run=args.dry_run,
    )

    # 4. Local Code (GLM 5.3) + chạy sandbox
    outputs["4_local_code"] = call_agent(
        "4_local_code",
        agents["4_local_code"],
        shared_context,
        f"KẾ HOẠCH TỪ ĐIỀU PHỐI:\n{outputs['2_coordinator']}\n\nCHỨNG MINH CỦA PROVER (NEON):\n{outputs['3_prover']}\n\n"
        f"Hãy viết script Python chạy cục bộ để kiểm tra biểu thức/mô phỏng số.",
        run_dir,
        dry_run=args.dry_run,
    )
    local_sandbox_log = run_verification_script(outputs["4_local_code"])
    (run_dir / "4_local_sandbox.log").write_text(local_sandbox_log, encoding="utf-8")
    print(f"    Kết quả Sandbox (Local Code):\n{local_sandbox_log}")

    # 5. Numeric Verifier (Qwen 4) + chạy sandbox
    outputs["5_numeric_verifier"] = call_agent(
        "5_numeric_verifier",
        agents["5_numeric_verifier"],
        shared_context,
        f"CHỨNG MINH CỦA PROVER (NEON):\n{outputs['3_prover']}\n\n"
        f"KẾT QUẢ LOCAL CODE (GLM 5.3):\n{outputs['4_local_code']}\n\n{local_sandbox_log}\n\n"
        f"Hãy kiểm chứng số học độc lập tại các điểm biên và viết script đối chiếu.",
        run_dir,
        dry_run=args.dry_run,
    )
    numeric_sandbox_log = run_verification_script(outputs["5_numeric_verifier"])
    (run_dir / "5_numeric_sandbox.log").write_text(numeric_sandbox_log, encoding="utf-8")
    print(f"    Kết quả Sandbox (Numeric Verifier):\n{numeric_sandbox_log}")

    # 6. Auditor (Gemini 4 Carbon)
    outputs["6_auditor"] = call_agent(
        "6_auditor",
        agents["6_auditor"],
        shared_context,
        f"HÃY THẨM ĐỊNH TOÀN BỘ KẾT QUẢ SAU:\n\n"
        f"=== PROVER (NEON) ===\n{outputs['3_prover']}\n\n"
        f"=== LOCAL CODE (GLM 5.3) ===\n{outputs['4_local_code']}\n{local_sandbox_log}\n\n"
        f"=== NUMERIC VERIFIER (QWEN 4) ===\n{outputs['5_numeric_verifier']}\n{numeric_sandbox_log}",
        run_dir,
        dry_run=args.dry_run,
    )

    # 7. LaTeX Integrator (Sonnet 5.5)
    outputs["7_latex"] = call_agent(
        "7_latex",
        agents["7_latex"],
        shared_context,
        f"Biên tập thành mã LaTeX chuẩn xác và tổng kết trạng thái dựa trên kết quả của Prover và Auditor:\n\n"
        f"=== CHỨNG MINH (PROVER - NEON) ===\n{outputs['3_prover']}\n\n"
        f"=== THẨM ĐỊNH (AUDITOR - CARBON) ===\n{outputs['6_auditor']}",
        run_dir,
        dry_run=args.dry_run,
    )

    # Xuất báo cáo tổng hợp
    final_report = run_dir / "FINAL_REPORT.md"
    final_report.write_text(
        f"# BÁO CÁO PHIÊN NGHIÊN CỨU — {prob_cfg['title']}\n\n"
        f"**Thời gian:** {ts}\n**Chế độ:** {'DRY-RUN (Kiểm thử luồng)' if args.dry_run else 'LIVE (OpenRouter + Local GLM 5.3)'}\n"
        f"**Mục tiêu:** {goal}\n\n---\n\n"
        f"## 1. Chỉ thị Chủ điều hành (Fable 5.2)\n{outputs['1_commander']}\n\n---\n\n"
        f"## 2. Phân rã Điều phối (Opus 5.5)\n{outputs['2_coordinator']}\n\n---\n\n"
        f"## 3. Thẩm định của Auditor (Gemini 4 Carbon)\n{outputs['6_auditor']}\n\n---\n\n"
        f"## 4. Mã LaTeX tích hợp & Tổng kết (Sonnet 5.5)\n{outputs['7_latex']}\n\n---\n\n"
        f"## 5. Log Sandbox (Local GLM 5.3 & Qwen 4)\n```text\n{local_sandbox_log}\n\n{numeric_sandbox_log}\n```\n",
        encoding="utf-8",
    )

    (run_dir / "meta.json").write_text(
        json.dumps(
            {"problem": args.problem, "timestamp": ts, "dry_run": args.dry_run, "goal": goal},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"\n=== HOÀN TẤT! Xem báo cáo tổng hợp tại: {final_report} ===")


if __name__ == "__main__":
    main()