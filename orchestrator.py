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
        os.environ.setdefault(k.strip(), v.strip())


def get_client(provider: str) -> OpenAI:
    if provider == "local":
        return OpenAI(
            base_url=os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:11434/v1"),
            api_key=os.getenv("LOCAL_LLM_API_KEY", "ollama"),
        )
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("Thiếu biến môi trường OPENROUTER_API_KEY. Hãy tạo file .env từ .env.example.")
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
) -> str:
    print(f"\n>>> Đang chạy [{agent_key}] - {agent_cfg['name']} ({agent_cfg['model']})...")
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
    parser = argparse.ArgumentParser(description="Điều phối 7 Agent nghiên cứu trên OpenRouter")
    parser.add_argument("--problem", type=int, required=True, choices=[1, 2, 3, 4], help="Số thứ tự bài toán mở (1..4)")
    parser.add_argument("--goal", type=str, default="", help="Mục tiêu cụ thể (để trống sẽ dùng default_goal trong config.yaml)")
    parser.add_argument("--extra-tex", nargs="*", default=[], help="Danh sách file .tex bổ sung trong tex_sections/")
    parser.add_argument("--config", type=str, default="config.yaml", help="Đường dẫn file cấu hình")
    args = parser.parse_args()

    load_env_file()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))

    prob_cfg = cfg["open_problems"][args.problem]
    goal = args.goal.strip() if args.goal.strip() else prob_cfg["default_goal"].strip()

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = Path(cfg["project"]["runs_dir"]) / f"problem_{args.problem}_{ts}"
    run_dir.mkdir(parents=True, exist_ok=True)

    shared_context = build_shared_system_context(cfg, args.problem, args.extra_tex)
    (run_dir / "0_packed_context.txt").write_text(shared_context, encoding="utf-8")

    agents = cfg["agents"]
    outputs = {}

    # Bước 1: Architect
    outputs["1_architect"] = call_agent(
        "1_architect",
        agents["1_architect"],
        shared_context,
        f"MỤC TIÊU CỤ THỂ:\n{goal}\n\nHãy lập chiến lược chứng minh chi tiết và phân rã bổ đề.",
        run_dir,
    )

    # Bước 2: Prover Main
    outputs["2_prover_main"] = call_agent(
        "2_prover_main",
        agents["2_prover_main"],
        shared_context,
        f"MỤC TIÊU:\n{goal}\n\nCHIẾN LƯỢC TỪ AGENT 1:\n{outputs['1_architect']}\n\nHãy viết chứng minh chi tiết từng bước.",
        run_dir,
    )

    # Bước 3: Prover Alt / Counterexample
    outputs["3_prover_alt"] = call_agent(
        "3_prover_alt",
        agents["3_prover_alt"],
        shared_context,
        f"MỤC TIÊU:\n{goal}\n\nCHỨNG MINH CỦA AGENT 2:\n{outputs['2_prover_main']}\n\nHãy kiểm tra phản ví dụ biên và đề xuất nhánh dự phòng.",
        run_dir,
    )

    # Bước 4: Numerical & Symbolic Verifier + Thực thi sandbox
    outputs["4_numeric_verifier"] = call_agent(
        "4_numeric_verifier",
        agents["4_numeric_verifier"],
        shared_context,
        f"Dựa trên bất đẳng thức/hệ số của Agent 2 và Agent 3 dưới đây, hãy viết script Python kiểm chứng số học:\n\n"
        f"--- AGENT 2 ---\n{outputs['2_prover_main']}\n\n--- AGENT 3 ---\n{outputs['3_prover_alt']}",
        run_dir,
    )
    sandbox_log = run_verification_script(outputs["4_numeric_verifier"])
    (run_dir / "4_sandbox_execution.log").write_text(sandbox_log, encoding="utf-8")
    print(f"    Kết quả chạy Sandbox:\n{sandbox_log}")

    # Bước 5: Rigor Auditor
    outputs["5_rigor_auditor"] = call_agent(
        "5_rigor_auditor",
        agents["5_rigor_auditor"],
        shared_context,
        f"HÃY PHẢN BIỆN TOÀN BỘ KẾT QUẢ SAU:\n\n"
        f"=== AGENT 2 (CHỨNG MINH CHÍNH) ===\n{outputs['2_prover_main']}\n\n"
        f"=== AGENT 3 (ĐỐI TRỌNG / PHẢN VÍ DỤ) ===\n{outputs['3_prover_alt']}\n\n"
        f"=== AGENT 4 & SANDBOX ===\n{outputs['4_numeric_verifier']}\n\n{sandbox_log}",
        run_dir,
    )

    # Bước 6: LaTeX Integrator
    outputs["6_latex_integrator"] = call_agent(
        "6_latex_integrator",
        agents["6_latex_integrator"],
        shared_context,
        f"Biên tập thành mã LaTeX chuẩn xác dựa trên chứng minh và kết quả phản biện của Agent 5:\n\n"
        f"=== CHỨNG MINH ===\n{outputs['2_prover_main']}\n\n=== PHẢN BIỆN AGENT 5 ===\n{outputs['5_rigor_auditor']}",
        run_dir,
    )

    # Bước 7: Synthesizer
    outputs["7_synthesizer"] = call_agent(
        "7_synthesizer",
        agents["7_synthesizer"],
        shared_context,
        f"Tổng kết phiên làm việc cho {prob_cfg['title']}:\n\n"
        f"=== PHẢN BIỆN AGENT 5 ===\n{outputs['5_rigor_auditor']}\n\n"
        f"=== BẢN LATEX AGENT 6 ===\n{outputs['6_latex_integrator']}",
        run_dir,
    )

    # Xuất báo cáo tổng hợp
    final_report = run_dir / "FINAL_REPORT.md"
    final_report.write_text(
        f"# BÁO CÁO PHIÊN NGHIÊN CỨU — {prob_cfg['title']}\n\n"
        f"**Thời gian:** {ts}\n**Mục tiêu:** {goal}\n\n---\n\n"
        f"## 1. Tổng kết & Hành động tiếp theo (Agent 7)\n{outputs['7_synthesizer']}\n\n---\n\n"
        f"## 2. Kết quả phản biện (Agent 5)\n{outputs['5_rigor_auditor']}\n\n---\n\n"
        f"## 3. Mã LaTeX tích hợp (Agent 6)\n{outputs['6_latex_integrator']}\n\n---\n\n"
        f"## 4. Log kiểm chứng số (Agent 4 Sandbox)\n```text\n{sandbox_log}\n```\n",
        encoding="utf-8",
    )

    (run_dir / "meta.json").write_text(
        json.dumps({"problem": args.problem, "timestamp": ts, "goal": goal}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\n=== HOÀN TẤT! Xem báo cáo tổng hợp tại: {final_report} ===")


if __name__ == "__main__":
    main()
