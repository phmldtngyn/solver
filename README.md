# Hệ thống 7 Agent Nghiên cứu (OpenRouter + Python Sandbox)

## 1. Cấu trúc thư mục chuẩn

Đặt toàn bộ file trong gói này vào thư mục gốc dự án của bạn theo cấu trúc sau:

```text
du_an_poisson_cascade/
├── context/
│   ├── tong_hop_dinh_ly_va_dinh_nghia.md
│   └── con_duong_toi_Aa_va_bai_toan_mo.md
├── tex_sections/          # Chứa các file .tex đã tách theo từng mục (sec10_46.tex, sec10_67.tex, ...)
├── runs/                  # Tự động sinh log và báo cáo sau mỗi lần chạy
├── .env                   # Copy từ .env.example và điền OPENROUTER_API_KEY
├── config.yaml            # Cấu hình model cho 7 Agent và danh sách file .tex từng bài toán
├── context_packer.py      # Đóng gói ngữ cảnh + làm sạch comment LaTeX
├── prompts.py             # System prompt chuyên biệt cho từng Agent
├── sandbox_executor.py    # Chạy kiểm chứng Python của Agent 4
├── orchestrator.py        # Bộ điều phối tuần tự 7 Agent
└── run_problem.ps1        # Script chạy nhanh trên Windows PowerShell
```

## 2. Cài đặt thư viện

```powershell
pip install openai pyyaml numpy scipy sympy
Copy-Item .env.example .env
# Mở .env và dán OPENROUTER_API_KEY của bạn vào
```

## 3. Cách sử dụng trên Windows PowerShell

Chạy mặc định cho một trong 4 bài toán mở (`1`, `2`, `3`, hoặc `4`):
```powershell
.\run_problem.ps1 -Problem 4
```

Truyền mục tiêu cụ thể và nạp thêm file `.tex` bổ sung:
```powershell
.\run_problem.ps1 -Problem 3 -Goal "Chứng minh C_{u,r} >= kappa > 0 trên khối quãng tám dựa trên Mệnh đề 10.178" -ExtraTex "sec10_49.tex"
```

Nếu muốn trỏ một hoặc nhiều Agent về model cục bộ (ví dụ GLM chạy local qua Ollama), chỉ cần sửa `provider: "local"` và `model: "glm4"` cho agent tương ứng trong `config.yaml`.
