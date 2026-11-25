import json
import re
from pathlib import Path
from typing import Dict, List

MISSING_TEX_TAG = "[CẢNH BÁO: Chưa có file"
MISSING_TEX_DIR_TAG = "[CẢNH BÁO: Chưa có thư mục tex_sections/"


def _read_text(path: Path) -> str:
    """Đọc UTF-8 (bỏ BOM) và loại bỏ ký tự NUL có thể làm hỏng request API."""
    return path.read_text(encoding="utf-8-sig").replace("\x00", "")


def clean_latex_source(tex: str) -> str:
    """Loại bỏ comment thuần túy và khoảng trắng thừa nhưng giữ nguyên công thức & label."""
    lines = []
    for line in tex.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("%"):
            continue
        line_no_comment = re.sub(r"(?<!\\)%.*$", "", line)
        lines.append(line_no_comment.rstrip())
    cleaned = "\n".join(lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def load_core_state(core_dir: str = "core") -> str:
    """Nạp tệp trạng thái và hiến pháp trong core/ (chỉ .md và .json)."""
    cdir = Path(core_dir)
    if not cdir.exists():
        return "[CẢNH BÁO: Không tìm thấy thư mục core/]"
    blocks = []
    for cf in sorted(cdir.glob("*")):
        if not cf.is_file() or cf.suffix.lower() not in (".md", ".json"):
            continue
        content = _read_text(cf)
        if cf.suffix.lower() == ".json":
            # Không đưa lịch sử chạy vào ngữ cảnh: tránh phình token sau mỗi phiên
            try:
                data = json.loads(content)
                data.pop("run_history", None)
                content = json.dumps(data, ensure_ascii=False, indent=2)
            except json.JSONDecodeError:
                pass
        blocks.append(f"=== CORE: {cf.name} ===\n{content}")
    return "\n\n".join(blocks)


def load_base_context(context_dir: str, dep_file: str, roadmap_file: str) -> Dict[str, str]:
    base = Path(context_dir)
    dep_path = base / dep_file
    road_path = base / roadmap_file

    if not dep_path.exists():
        raise FileNotFoundError(f"Không tìm thấy file nền: {dep_path}")
    if not road_path.exists():
        raise FileNotFoundError(f"Không tìm thấy file lộ trình: {road_path}")

    return {
        "dependency_map": _read_text(dep_path),
        "roadmap": _read_text(road_path),
    }


def load_tex_sections(tex_dir: str, tex_filenames: List[str]) -> str:
    tdir = Path(tex_dir)
    if not tdir.exists():
        return f"{MISSING_TEX_DIR_TAG} — chạy dựa trên core/ và context/]"
    blocks = []
    for fname in tex_filenames:
        fpath = tdir / fname
        if fpath.exists():
            blocks.append(f"=== FILE: {fname} ===\n{clean_latex_source(_read_text(fpath))}")
        else:
            blocks.append(f"=== FILE: {fname} ===\n{MISSING_TEX_TAG} {fpath}]")
    return "\n\n".join(blocks)


def build_shared_system_context(cfg: dict, problem_id: int, extra_tex: List[str] = None) -> str:
    proj = cfg["project"]
    prob = cfg["open_problems"][problem_id]

    core_content = load_core_state(proj.get("core_dir", "core"))
    base_ctx = load_base_context(
        proj["context_dir"],
        proj["dependency_map_file"],
        proj["roadmap_file"],
    )

    tex_list = list(prob.get("tex_files", []))
    for f in extra_tex or []:
        if f not in tex_list:
            tex_list.append(f)

    tex_content = load_tex_sections(proj["tex_dir"], tex_list)

    return f"""BẢN THẢO: {proj["title"]}
MỤC TIÊU HIỆN TẠI: {prob["title"]}

<core_state>
{core_content}
</core_state>

<dependency_map>
{base_ctx["dependency_map"]}
</dependency_map>

<roadmap_and_open_problems>
{base_ctx["roadmap"]}
</roadmap_and_open_problems>

<relevant_latex_sections>
{tex_content}
</relevant_latex_sections>"""
