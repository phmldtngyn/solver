import re
from pathlib import Path
from typing import List, Dict


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
    """Nạp toàn bộ tệp trạng thái và hiến pháp trong thư mục core/."""
    cdir = Path(core_dir)
    if not cdir.exists():
        return "[CẢNH BÁO: Không tìm thấy thư mục core/]"
    blocks = []
    for cf in sorted(cdir.glob("*")):
        if cf.is_file():
            blocks.append(f"=== CORE: {cf.name} ===\n{cf.read_text(encoding='utf-8')}")
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
        "dependency_map": dep_path.read_text(encoding="utf-8"),
        "roadmap": road_path.read_text(encoding="utf-8"),
    }


def load_tex_sections(tex_dir: str, tex_filenames: List[str]) -> str:
    tdir = Path(tex_dir)
    if not tdir.exists():
        return "[Chưa có thư mục tex_sections/ — chạy dựa trên core/ và context/]"
    blocks = []
    for fname in tex_filenames:
        fpath = tdir / fname
        if fpath.exists():
            raw = fpath.read_text(encoding="utf-8")
            cleaned = clean_latex_source(raw)
            blocks.append(f"=== FILE: {fname} ===\n{cleaned}")
        else:
            blocks.append(f"=== FILE: {fname} ===\n[CẢNH BÁO: Chưa có file {fpath}]")
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
    if extra_tex:
        for f in extra_tex:
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