# CON ĐƯỜNG TỚI A(a) VÀ CÁC BÀI TOÁN CÒN MỞ

## 1. Phát biểu cần chứng minh

**A(a).** Cho $c > c^*$. Tồn tại $\eta^* > 0$ và $C$ không phụ thuộc $\varepsilon$ sao cho, với $t_1 = C\ln(1/\varepsilon)$ và mọi cửa sổ $[t_1, t_2]$ có độ dài cố định:
$$\mathbb{P}\big(\exists\, t\in[t_1,t_2]:\; \eta_t < \eta^*\big) \;\longrightarrow\; 0 \quad (\varepsilon\to 0).$$
Nói bằng lời: sau thời gian cỡ $\ln(1/\varepsilon)$, **phòng** $\eta = F - \ln\bar\delta$ bị chặn khỏi 0 theo xác suất, đều theo $\varepsilon$, trên mọi cửa sổ cố định.

---

## 2. Chuỗi suy luận đã được chứng minh

Toàn bộ phần động lực đã chặt. Chuỗi đi từ A(a) ngược về các giả thiết tĩnh như sau:

```text
A(a)
 │
 ├─ Rào chắn theo dải (Bổ đề 10.135, Hệ quả 10.136)
 │    Phòng không thể rơi xuống ηa nếu:
 │    (i)  trôi ≥ κ > 0 trên dải [ηa, ηb];
 │    (ii) bước nhảy ≤ j = o(1);
 │    (iii) tốc độ phương sai σ² = O(ε).
 │    Xác suất thoát xuống ≤ E[N↓]·exp(−c/ε) → 0.
 │
 ├─ Trôi dương trên dải (Định lý 10.130)
 │    Không cần chặn độ sâu. Chỉ cần:
 │    (F1) F(r) ≤ (γ²/16)·ψ(eφ)  với r ≥ Λ₁ε;
 │    (F2) ∫ F(r) dr/r ≤ CF;
 │    (ND) Ur ≥ γ√Wr;   (W−) Wr ≥ w−ε/r.
 │    Khi đó dải thô thắng dải mịn vì dài ln(1/x²) quãng tám.
 │
 ├─ (F1)+(F2) ⇐ chặn L² = ∫(ln ρ̂)² (Bổ đề 10.132)
 │    L² ≤ 2e^{B*} + B*² + I,  với I = ∫(u−)².
 │    Và I ≤ ∫A² (Bổ đề 10.171: độ sâu ≤ tuổi đầy).
 │
 ├─ σ² = O(ε) và j = o(1) ⇐ (VT)
 │    (VT) được chứng minh qua Poincaré Poisson
 │    (Bổ đề 10.138, 10.139, Mệnh đề 10.140, Định lý 10.144).
 │    Chỉ ứng viên ĐƯỢC NHẬN mới có ảnh hưởng.
 │    C* ∝ 1/x_a² — khớp số liệu gói 14.
 │
 ├─ (VT) ⇐ (Lloc) đều theo thời gian (Hệ quả 10.145)
 │    Cần: (QT) phần nhớ co + (LV-Palm) + (B′).
 │
 ├─ (Lloc) cho GEOM ⇐ so sánh với P(γ) (Mệnh đề 10.48, 10.73)
 │    Khuyết tật sinh ra từ lệch mức δ = O(√ε) (Định lý 10.167),
 │    lan với tốc độ hữu hạn (Mệnh đề 10.67, 10.95),
 │    có mô-men bậc hai (Định lý 10.168) và bậc bốn (Định lý 10.169).
 │
 └─ (QT) ⇔ (C₀): hệ số hồi phục C ≥ C₀ > 0
      Theo đồng nhất thức 10.122, 10.125:
      C = 1 − ⟨g⟩̄/W.  C ≥ C₀ nghĩa là
      "cung hợp lệ tránh chỗ đặc".
```

**Kết luận của chuỗi:** Mọi định lý động lực đã được chứng minh. A(a) đúng **có điều kiện** dưới đúng **bốn bài toán tĩnh/động** còn mở, cộng một số việc kỹ thuật.

---

## 3. Bốn bài toán còn mở

### Bài toán 1 — Phân phối cục bộ quanh khuyết tật và quanh ngưỡng *(tĩnh, khó nhất)*

Gồm hai nửa:

**1a. (LV-Palm).** Ép nhận một cung $S_w$, gọi $U = \bigcup_j S_j$ là hợp các cung nhận lệch. Cần:
$$\big|\{y: S(y,r)\cap U\ne\emptyset,\; \rho_r(y)\le s\}\big| \;\le\; (\|U\|+2r\,N_c(U))\,\bar\alpha_r(s)(1+C_0\sqrt{\varepsilon/r}),$$
với $a_1, a_0, a_{-1}, a_2$ của $\bar\alpha_r$ hữu hạn. Dạng đủ: $\bar\alpha_r(\theta) \le C e^{-c_0 x_a^2 r/\varepsilon}$.

> Lưu ý quan trọng: dạng "đúng với **mọi** cung $I$" là **sai** (Mục 10.60). Chỉ đòi cho các tập $U$ do động lực sinh ra.

**1b. (B⁺-atom).** Mật độ của khoảng cách tới ngưỡng bị chặn:
$$|\{y: |X_r(y)|\le\delta\}| \;\le\; 2\kappa_r\,\delta + e_r,$$
với $K_1, K_2$ hữu hạn. Số hạng $e_r$ chứa các khúc phẳng do lượng tử hoá $\hat\rho = (1+c)^N/Z$.

- **Vai trò:** Nền của mọi chặn động lực (10.143, 10.144, 10.167–10.169). Không có nó, không có (VT), không có (MIX), không có độ lệch mức.
- **Số liệu (gói 17):** (LV-Palm) có phân vị 90% $\le 1{,}46$; không phát hiện nguyên tử; $\kappa$ phẳng theo $K$; $D \approx 10\varepsilon$, $D_4 = O(\varepsilon^3)$.
- **Đánh giá:** **Khó nhất.** Đây là phát biểu về phân phối dừng của một hệ tương tác không cục bộ. Chưa có đường chứng minh trọn.

---

### Bài toán 2 — Hai cận của hệ số hồi phục *(tĩnh, cộng mô-men)*

**Phát biểu chính.** Tồn tại $0 < C_0 \le C^+ < \infty$ sao cho, theo $(*)$, với mọi $\ell \ge \Lambda\varepsilon$:
$$C_0 \;\le\; C_\ell \;\le\; C^+.$$

**Cận dưới tách theo thang:**
- *Thang trung:* Định lý 10.146 (tất định) + (NS) — cung ngắn không chọn ngược. Gần xong.
- *Thang thô:* Định lý 10.148, cần **(B⁻)** dạng hai điểm và **(LE)** (cân bằng cục bộ). Đây là phần mở.

**Cận trên:** $C \le C^+$ tương đương với **(W⁻)**: $W_r \ge w^-\varepsilon/r$.

**Kèm theo: (QT) bậc bốn.** $\mathbb{E}\|\hat H_k^{(T)}\|^4 \le q\,\mathbb{E}\|\hat G_k(t-T)\|^4 + c_0\varepsilon^2$. Bản bậc hai đã có; bản bậc bốn cần cho Định lý 10.169 và chặn từng quỹ đạo.

- **Vai trò:** $C_0$ cho hồi phục (dư âm pha nóng tan, cửa sổ $t_1 \sim \ln(1/\varepsilon)$) và tính co (QT). $C^+$ cho (W⁻), rồi Paley–Zygmund cho tỉ lệ hợp lệ $a_r \ge \gamma^2/16$.
- **Số liệu:** $C \in [2{,}3;\, 8{,}1]$, dương ở mọi dump và mọi tầng; $\zeta \approx 0{,}67$–$0{,}84$; trùng hợp chưa giải thích: $C \approx e_\Phi$ tới vài phần trăm.
- **Đánh giá:** Thang trung gần xong. **(LE)** là một dự án riêng. Đường khả dĩ: tự đồng dạng của GEOM trong hộp, ghép với hệ cô lập, chặn biên bằng 10.143.

---

### Bài toán 3 — Độ sâu của hõm *(động, có công cụ)*

> **Sửa ngày 22/11.** Dạng $\sup_t \mathbb{E} I_t \le C$ là **sai**: số liệu tới $t=2048$ cho $I \approx 0{,}29 + 0{,}34\ln t$. Phát biểu đúng dùng bản làm trơn theo tầng $V_r = \int \bar u_r^2$: chứng minh $\sup_t \mathbb{E} V_r \le C$ cho $r \ge \Lambda\varepsilon$, hoặc chặn trực tiếp $F(r)$ ở thang thô.

**Hai đường đã chuẩn bị:**

1. **Qua $C_{\log}$:** Theo Mệnh đề 10.172, $dI/d\Gamma \le -2C_{\log} I + L$. Cần chứng minh $C_{\log} \ge \kappa > 0$, tức các cung được nhận phủ các điểm sâu nhiều hơn trung bình. Đây là bản sao, trên trường log, của $C_0$ ở Bài toán 2.

2. **Qua tuổi, tái sinh:** Theo Bổ đề 10.171, $I \le \int A^2$, với $A(y)$ là phần tăng của $\Gamma$ kể từ lần cuối $u(y)\ge 0$. Cần chặn đuôi của $A$.

- **Số liệu:** $C_{\log} \approx 0{,}14$–$0{,}17$, có xu hướng $\sim 1/\ln t$; lá sâu nhất có $u \approx -10$ đến $-16$.
- **Đẳng thức mới (10.178):** $dV_r/d\Gamma = -2C_{u,r}V_r + \nu_r$, với $\nu_r$ tính đóng. Số liệu: $C_{u,r} \approx 2{,}5$–$3$ ở $\ell \ge 16\varepsilon$, **phẳng theo $K$ và $t$**. Bài toán còn lại là chứng minh $C_{u,r} \ge \kappa > 0$ trên một khối quãng tám.
- **Vai trò:** Chặn $L^2$, rồi (F1) và (F2) qua Bổ đề 10.132, tức cho trôi dương trên dải.
- **Đánh giá:** Khả thi; đường 2 không phụ thuộc Bài toán 2.

---

### Bài toán 4 — Đi vào dải khi độ gồ ghề còn lớn *(động)*

> **Sửa ngày 22/11.** Bài này **không độc lập** với Bài toán 2: nửa hồi phục của nó cần $C_0$ và (Cỡ).

**Phát biểu.** Gọi $t_h$ là thời điểm đầu tiên mà $\theta_t \le 1$ (kết thúc pha nóng). Chứng minh:
$$\mathbb{P}\Big(\eta_{t_1} \ge \eta_b \;\text{ và }\; \sup_{r\ge\Lambda\varepsilon} W_r(t_1)\tfrac{r}{\varepsilon} \le M\Big) \;\longrightarrow\; 1.$$

**Khó khăn:**
- Trong đoạn $0 < \eta \ll 1$, Định lý 10.130 không áp được vì $F(r) = O(1)$ nên (F1) sai.
- $W$ lớn làm $E_r$ giảm (10.110′), tức làm trôi của $\eta$ chậm lại.

**Đường khả dĩ:** Tìm hàm Lyapunov hai biến $V = \eta - \beta\sum_j w_j W_{r_j} r_j/\varepsilon$. Nguyên liệu đã có: đồng nhất thức trôi 10.110 cho $\eta$; đồng nhất thức co 10.122–10.123 cho $W$; lực đẩy rất mạnh khi $\theta > 1$ (10.27, 10.28).

- **Số liệu:** hệ đi qua đoạn này trong dưới một đơn vị thời gian (DD, Z2); phần gồ ghề vĩ mô tan theo $t$ (gói 15).
- **Đánh giá:** **Khả thi nhất** trong bốn bài; tính toán, không cần ý tưởng mới.

---

## 4. Việc kỹ thuật chưa viết

Ba việc sau không phải bài toán mở, chỉ chưa viết chặt:

1. **Khẳng định 1 của Bổ đề 9.19** (độc lập khối) cho mức tất định bất kỳ, không chỉ tuyến tính. Cần cho Định lý 10.169.
2. **Đổi đồng hồ từ $t$ sang $\Gamma$** trong 10.172 một cách chặt, ở mức bộ bù.
3. **Bản sắc của 10.172:** chỉ tính số hạng bậc hai trên $\{u \le L\|S\|\}$. Chặn hiện tại lỏng khoảng hai lần.

---

## 5. Quan hệ giữa các bài toán và thứ tự đề xuất

```text
Bài 1 (LV-Palm, B⁺)  ─── nền ───►  mọi chặn động lực
                                      (10.143, 10.144, 10.167–10.169)

Bài 2 (C₀ ≤ C ≤ C⁺)  ◄── cùng hiện tượng ──►  Bài 3 (đường 1: Clog)
   "cung hợp lệ tránh chỗ đặc = lấp chỗ trống"

Bài 4  ─── cần C₀ của Bài 2 ───►  không thể làm đầu tiên
```

**Thứ tự đề xuất (sau sửa 22/11):** Bài 3 và Bài 2 **song song**, rồi Bài 4; Bài 1 là nền.

---

## 6. Đánh giá trung thực

> Nếu Bài 3 và Bài 4 được giải, A(a) trở thành **định lý có điều kiện** dưới đúng hai nhóm tính chất tĩnh: **Bài 1**, và **(LE)/(B⁻)** của Bài 2. Cả hai đều có số liệu đăng ký trước ủng hộ. Chứng minh chúng cho **phân phối dừng** của GEOM là bài toán nghiên cứu mở; tác giả không có đường đi trọn cho chúng.

**Những gì đã đạt:**
- Mọi bước động lực từ A(a) ngược về bốn bài toán đều **đã chứng minh đầy đủ**.
- Mỗi bài toán còn mở đều có **phát biểu chính xác**, **số liệu đăng ký trước ủng hộ**, và **ít nhất một đường khả dĩ**.
- Các kiểm thử ngoài mẫu (VX, VX2) và kiểm độc lập đều cho kết quả nhất quán.

**Những gì chưa đạt:**
- Chưa có chứng minh nào cho phân phối dừng của hệ tự tương tác, không thuận nghịch, hỗn loạn theo quỹ đạo.
- Bài 1 là chỗ khó thật sự: nó đòi hỏi một lý thuyết trạng thái dừng cho hệ hạt tương tác không cục bộ, thuộc loại bài toán trộn khó, không có công cụ chuẩn áp thẳng.
- $c^*$ chưa được xác định chặt; số liệu gợi ý $c^* \in (0{,}54;\, 0{,}77)$ ở $\bar\delta = 2$, phụ thuộc cửa sổ.

**Nói ngắn:** Con đường tới A(a) đã được vẽ hoàn chỉnh, mọi mũi tên động lực đã chặt. Chỗ còn lại là **bốn viên gạch tĩnh** ở nền móng, mà viên khó nhất (Bài 1) đòi hỏi một công cụ mới chứ không chỉ thêm tính toán.