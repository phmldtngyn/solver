import re
import subprocess
import sys
import tempfile
from pathlib import Path


def extract_python_code(text: str) -> str:
    matches = re.findall(r"```python\s*(.*?)```", text, flags=re.DOTALL | re.IGNORECASE)
    if not matches:
        return ""
    return "\n\n".join(m.strip() for m in matches)


def run_verification_script(agent_output: str, timeout_sec: int = 30) -> str:
    code = extract_python_code(agent_output)
    if not code:
        return "[SANDBOX] Không tìm thấy khối mã ```python``` trong phản hồi của Agent 4."

    with tempfile.TemporaryDirectory() as tmpdir:
        script_path = Path(tmpdir) / "verify_step.py"
        script_path.write_text(code, encoding="utf-8")

        try:
            proc = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True,
                timeout=timeout_sec,
                encoding="utf-8",
                errors="replace",
            )
            out = proc.stdout.strip()
            err = proc.stderr.strip()
            return (
                f"[SANDBOX EXIT CODE: {proc.returncode}]\n"
                f"--- STDOUT ---\n{out if out else '(trống)'}\n"
                f"--- STDERR ---\n{err if err else '(không có lỗi)'}"
            )
        except subprocess.TimeoutExpired:
            return f"[SANDBOX TIMEOUT] Script vượt quá giới hạn {timeout_sec} giây."
        except Exception as exc:
            return f"[SANDBOX ERROR] {exc}"
