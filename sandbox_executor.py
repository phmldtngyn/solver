import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# Chỉ chuyển các biến môi trường cần thiết cho tiến trình con.
# KHÔNG chuyển OPENROUTER_API_KEY hay bất kỳ khóa bí mật nào sang code do AI sinh ra.
_SAFE_ENV_KEYS = (
    "PATH", "SYSTEMROOT", "SYSTEMDRIVE", "WINDIR", "COMSPEC", "PATHEXT",
    "TEMP", "TMP", "TMPDIR", "HOME", "USERPROFILE", "LANG", "LC_ALL",
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS",
)


def _safe_env(workdir: str) -> dict:
    env = {k: os.environ[k] for k in _SAFE_ENV_KEYS if k in os.environ}
    env["PYTHONIOENCODING"] = "utf-8"
    env["MPLBACKEND"] = "Agg"  # không mở cửa sổ đồ họa
    env["TEMP"] = env["TMP"] = env["TMPDIR"] = workdir
    return env


def extract_python_code(text: str) -> str:
    """Lấy khối ```python``` CUỐI CÙNG (thường là script hoàn chỉnh), không ghép các đoạn ví dụ rời."""
    matches = re.findall(r"```python\s*(.*?)```", text, flags=re.DOTALL | re.IGNORECASE)
    if not matches:
        return ""
    return matches[-1].strip()


def run_verification_script(agent_output: str, timeout_sec: int = 120) -> str:
    code = extract_python_code(agent_output)
    if not code:
        return "[SANDBOX] Không tìm thấy khối mã ```python``` trong phản hồi của Agent."

    with tempfile.TemporaryDirectory() as tmpdir:
        script_path = Path(tmpdir) / "verify_step.py"
        script_path.write_text(code, encoding="utf-8")

        try:
            proc = subprocess.run(
                [sys.executable, "-I", str(script_path)],  # -I: không nạp module từ thư mục dự án
                cwd=tmpdir,                                 # chạy trong thư mục tạm, không đụng file dự án
                env=_safe_env(tmpdir),
                capture_output=True,
                text=True,
                timeout=timeout_sec,
                encoding="utf-8",
                errors="replace",
            )
            out = proc.stdout.strip()[-6000:]
            err = proc.stderr.strip()[-3000:]
            return (
                f"[SANDBOX EXIT CODE: {proc.returncode}]\n"
                f"--- STDOUT ---\n{out if out else '(trống)'}\n"
                f"--- STDERR ---\n{err if err else '(không có lỗi)'}"
            )
        except subprocess.TimeoutExpired:
            return f"[SANDBOX TIMEOUT] Script vượt quá giới hạn {timeout_sec} giây."
        except Exception as exc:
            return f"[SANDBOX ERROR] {exc}"
