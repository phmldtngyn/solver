# TỔNG HỢP TOÀN BỘ ĐỊNH LÝ – MỆNH ĐỀ – BỔ ĐỀ – ĐỊNH NGHĨA
## Bản thảo: *Một thác nhân Poisson tự điều tiết trên đường tròn*

---

## §0. MÔ HÌNH VÀ KÝ HIỆU

**Không gian.** $\mathbb{T}=\mathbb{R}/\mathbb{Z}$, độ đo Lebesgue $dx$, $\|A\|=\int_A dx$. Cung $S(y,r)=\{x:\text{dist}(x,y)\le r\}$, $\|S(y,r)\|=2r$ (vì $r\le R\le 1/4$).

**Tham số.** $0<\varepsilon\le R\le 1/4$, $c>0$, $L=\ln(1+c)$, $\bar\delta\ge 1$, $b=\ln\bar\delta$.

**Trường và thế năng.** Với $\varphi$ bị chặn, đo được:
$$Z=\int e^\varphi,\quad W(A)=\int_A e^\varphi,\quad \hat Q(dx)=\frac{e^\varphi}{Z}dx,\quad \Gamma=\int\varphi,\quad F=\ln Z-\Gamma,\quad u=\varphi-\Gamma.$$
Khi đó $F=\ln\int e^u$, $\int u=0$, mật độ $\rho=e^{u-F}$.

**Luật nhận GEOM.** Nhận cung $S$ khi
$$\frac{1}{\|S\|}\int_S e^\varphi \le \bar\delta\, e^\Gamma \;\;\Longleftrightarrow\;\; h_S:=\ln\!\Big(\frac{1}{\|S\|}\int_S e^u\Big)\le b \;\;\Longleftrightarrow\;\; \frac{\hat Q(S)}{\|S\|}\le \theta:=\bar\delta\, e^{-F}.$$

**Động lực học.**
- *Phản hồi tức thời:* xét lần lượt dãy ứng viên tuỳ ý.
- *Mô hình Poisson:* ứng viên $(b,y,r)$ đến theo Poisson cường độ $\lambda\,db\,dy\,r^{-2}dr$ trên $[0,\infty)\times\mathbb{T}\times[\varepsilon,R]$, kèm nhãn trễ $e\sim G$ độc lập.
- *Trường cam kết* $\tilde\Phi_t$; *trường chết* $\Phi_t$; phép thử $\text{GEOM}_C$.

**Hằng số.**
$$B^*=\ln\frac{c\bar\delta}{L},\quad B=B^*+\ln\!\Big(1+\frac{2c\bar\delta R}{1}\Big),\quad \kappa^*=\frac{L}{c},\quad \kappa=\bar\delta e^{-B}.$$

**Đại lượng theo thang.**
- $F_\eta=\frac{1}{k}\sum_j \ln\frac{1/k}{\hat Q(I_j)}$ với $\eta=1/k$.
- $\rho_r(y)=\hat Q(S(y,r))/(2r)$; $F(r)=-\int\ln\rho_r\,dy$.
- $a(r)=\|\{y:\rho_r(y)\le\theta\}\|$.
- *Đóng băng từ thang $r_0$:* không cung nào bán kính $\in[r_0,R]$ chấp nhận được.

---

## §1. KẾT QUẢ TẤT ĐỊNH

### Bổ đề 1.1 (KL cơ bản). [Đầy đủ]
Cho $\varphi$ bị chặn, đo được, $U$ là độ đo đều trên $\mathbb{T}$.
- **(a)** $F=\mathrm{KL}(U\|\hat Q)\ge 0$ và $F(\varphi+a)=F(\varphi)$.
- **(b)** $F(\varphi+L\mathbf{1}_S)-F(\varphi)=\ln(1+c\hat Q(S))-L\|S\|$.
- **(c)** Nếu $\varphi\le\psi$ thì $F(\varphi)\le F(\psi)+\int(\psi-\varphi)$.
- **(d)** $\mu\mapsto\mathrm{KL}(U\|\mu)$ nửa liên tục dưới theo hội tụ yếu. Nếu $\mathrm{KL}(U\|\mu)\le B'$ thì mọi tập Lebesgue dương có $\mu$-độ đo dương, và phần liên tục tuyệt đối của $\mu$ có khối lượng $\ge e^{-B'}$.

### Định lý 1.2 (Chặn tất định). [Đầy đủ]
- **(a)** Với GEOM, $\bar\delta\ge 1$, $F(\varphi_0)\le B^*$ và mọi dãy ứng viên: $F(\varphi_k)\le B^*$ với mọi $k$.
- **(b)** Trong mô hình có trễ với $\text{GEOM}_C$: $F(\tilde\Phi_t)\le B^*$; $F(\Phi_t)\le B^*+L\sum_{\text{đang chờ}}\|S\|$.
- **(c)** Mọi điểm tụ yếu $\hat Q$ của $\hat Q^{\tilde\Phi_\varepsilon}_t$ có $\mathrm{KL}(U\|\hat Q)\le B^*$.

### Định lý 1.3 ($p=0$ là số mũ tới hạn). [Đầy đủ]
Họ $PM_p$: nhận $S$ khi $\frac{1}{\|S\|}\int_S e^\varphi\le\bar\delta M_p(\varphi)$.
- **(a)** Với $p\le 0$, $PM_p$ thoả Định lý 1.2(a).
- **(b)** Với $p>0$, $\bar\delta>1$: tồn tại dãy ứng viên đều được nhận sao cho $F\to\infty$.

### Mệnh đề 1.4 (Không điều tiết).
Nhận mọi cung, cường độ $\theta\,dy\,r^{-2}dr$, $s=\ln(R/\varepsilon)$, $\Phi=LN$.
- **(a)** $\mathbb{E}F(\Phi)\le 2\theta(c-L)s$.
- **(b)** [Dựa trích dẫn] Nếu $\theta<\theta_c$: $F(\Phi)-2\theta(c-L)s\to\ln Q(\mathbb{T})-LX$ h.c.c.
- **(c)** Với mọi $\theta>0$: $\mathbb{P}(F(\Phi)\ge(2\theta'(c-L)-\eta)s)\to 1$.

### Định lý 1.5 (Độc lập trễ). [Đầy đủ]
- **(a)** $\tilde\Phi$ và các chỉ báo nhận là hàm của $\Pi^\circ$ (không phụ thuộc $G$).
- **(b)** $\tilde\Phi^{(\lambda)}_t\stackrel{d}{=}\tilde\Phi^{(1)}_{\lambda t}$.
- **(c)** Có điều kiện theo $\Pi^\circ$, các đồng hồ chết độc lập.
- **(d)** $\mathbb{E}F(\Phi_t)\le B^*+L\mathbb{E}\int_{[0,t]}\bar G(t-b)\,dA_b$.

### Định lý 1.6 (Cân bằng số phủ; hệ quả của đóng băng). [Đầy đủ]
Gọi $\tilde N=\tilde\Phi/L$.
- **(a)** Với mọi cung $J$, $0<\|J\|<1$:
$$-1-\frac{\|J\|}{1-\|J\|}\Big(B+\ln\frac{1}{1-\|J\|}\Big)\le L\Big(\frac{1}{\|J\|}\int_J\tilde N-\int\tilde N\Big)\le B+\ln\frac{1}{\|J\|}.$$
- **(b)** Nếu $\varphi$ đạt được và đóng băng từ $r_0\le R/2$:
  - (i) $\ln\bar\delta<F\le B$;
  - (ii) $\hat Q(J)>\theta\|J\|\ge\kappa\|J\|$ với $\|J\|\ge 2r_0$;
  - (iii) $F_\eta<F-\ln\bar\delta$ với $\eta\ge 2r_0$;
  - (iv) nếu $\hat Q_n\Rightarrow\hat Q$ thì $\hat Q\ge\kappa\,\text{Leb}$.

### Bổ đề 1.7 (Fubini; Markov). [Đầy đủ]
$\int\rho_r\,dy=1$; $\int e^{h_{S(y,r)}}dy=e^F$. Do đó $a(r)\ge 1-e^{F-b}$. Theo cung: $\|\{y\in I:S(y,r)\text{ bị từ chối}\}\|\le\theta^{-1}\hat Q(I+r)$.

### Bổ đề 1.8 (Sàn vô điều kiện). [Đầy đủ]
Với mọi trạng thái đạt được ($F\le B^*$) và mọi khoảng $J$, $\|J\|=w$:
$$\hat Q(J)\ge w\exp(-1-B^*/w).$$

### Bổ đề 1.9 (Luật $L/c$). [Đầy đủ]
Từ $\varphi_0\equiv 0$, gọi $S_i$ là các cung được nhận, $q_i=\hat Q(S_i)$ trước lần nhận thứ $i$:
$$\sum_i\ln(1+cq_i)=\Gamma+F,\qquad \Big|\frac{\sum_i\ln(1+cq_i)}{L\sum_i\|S_i\|}-1\Big|\le\frac{B}{\Gamma}.$$

### Định lý 1.10 (Cấu trúc theo thang). [Đầy đủ]
Với $r\le 1/8$:
- **(a)** $0\le F(2r)\le F(r)\le F$;
- **(b)** $a(2r)\le 2a(r)$;
- **(c)** nếu mọi cung bán kính $\in[r_1,2r_1)$ bị từ chối thì mọi cung dài $\ge 2r_1$ có $\hat Q(S)>\theta\|S\|$ (đóng băng lan lên).

### Định lý 1.11 (Bất đẳng thức đóng băng). [Đầy đủ]
Nếu $\theta<1$ ($F>b$) thì với mọi $r\le 1/4$:
$$a(r)\,h(\theta)\le \mathrm{kl}(a(r)\|\theta a(r))\le F(r),\quad h(\theta)=\theta-1-\ln\theta>0.$$
Trong mô hình Poisson: xác suất một ứng viên bán kính $r$ được nhận $\le\mathbb{P}(F_{b^-}<b+\eta_0)+\mathbb{E}F(r)/h(e^{-\eta_0})$.

### Định lý 1.12 (Trần mật độ). [Đầy đủ]
Cho cung $J$, $r_1\in[\varepsilon,R]$, $\|J\|+4r_1<1$; đặt $J^+=J+2r_1$ và hằng $C_{J^+}$. Xét đoạn các lần nhận $S_1,\dots,S_n$ bán kính $\le r_1$, ngay trước mỗi lần $F\ge F_{\min}$, $\hat Q(J)\ge\rho^*\|J\|$. Nếu
$$\rho^*\ge(1+s)\Big(1+\frac{4r_1}{\|J\|}\Big)\frac{c}{L}\bar\delta e^{-F_{\min}},$$
thì $\Delta\Gamma:=L\sum_i\|S_i\|\le\frac{1+s}{s}\big(B+L+\ln\frac{1}{\rho^*\|J\|}\big)+\frac{C_{J^+}}{s}$.

---

## §2. CẤU TRÚC: ENTROPY THEO THANG, SÀN–PHÒNG–TRẦN, DỊCH NGƯỠNG

### Bổ đề 2.1 (Phân rã chuỗi dyadic). [Đầy đủ]
Gọi $P_j$ là các ô dyadic mức $j$, $p_Q=\hat Q(Q^-)/\hat Q(Q)$, $\kappa(p)=-\frac{1}{2}\ln(4p(1-p))$, $d_j=\sum_{Q\in P_j}\mu(Q)\kappa(p_Q)$.
- **(a)** Nếu $\varphi$ hằng trên mỗi ô của $P_J$: $F=\sum_{j=0}^{J-1}d_j$.
- **(b)** Với $\varphi$ bị chặn: $F=\sum_{j\ge 0}d_j$.
- **(c)** Với $\eta=2^{-m}$: $F_\eta=\sum_{j<m}d_j$, $F-F_\eta=\sum_{j\ge m}d_j$.
- **(d)** $\kappa(p_Q)$ chỉ phụ thuộc $\varphi|_Q$, không đổi khi cộng hằng số.

### Hệ quả 2.2. [Đầy đủ]
Nếu $\mathbb{E}F_\eta\to 0$ với mọi $\eta$ thì $F-\sum_{j\ge m}d_j\to 0$ trong $L^1$.

### Bổ đề 2.3 (Entropy của một bước nhảy). [Đầy đủ]
Cho ô dyadic $Q$ dài $h$, $\varphi=a$ bên trái, $a+\ell$ bên phải, $r=e^\ell$. Đóng góp của $Q$: $h\sum_{n\ge 0}2^{-n}\kappa_r(\{2^n\xi\})$. Nếu $\xi$ đều: kỳ vọng $2h\,k(r)$.

### Bổ đề 2.4 (Phân rã theo thang liên tục). [Đầy đủ]
Đặt $\rho_\ell(x)=\hat Q([x,x+\ell))/\ell$, $G(\ell)=-\int\ln\rho_\ell\,dx$, $D(\ell)=\int\ln\cosh\frac{X_{x,\ell}}{2}dx$.
- **(a)** $0\le G(\ell)\le F$; $G(\ell)-G(2\ell)=D(\ell)\ge 0$.
- **(b)** $\frac{1}{\ln 2}\int_{\ell^*}^{2^n\ell^*}D(\ell)\frac{d\ell}{\ell}\le F$.
- **(c)** $\int h_{S(z,r)}dz=F-G(2r)$.

### Mệnh đề 2.5 (Sàn–Phòng–Trần). [Đầy đủ]
- **(a)** $h_S=\frac{1}{\|S\|}\int_S u+\mathrm{KL}(U_S\|\hat Q(\cdot|S))$ (sàn + phòng).
- **(b)** $R(\ell):=F-G(\ell)=\int h_{[x,x+\ell)}dx=\int\mathrm{KL}(U_{[x,x+\ell)}\|\hat Q(\cdot|[x,x+\ell)))dx\in[0,F]$.
- **(c)** $R(2\ell)-R(\ell)=D(\ell)\ge 0$; nếu $\varphi$ bậc thang hữu hạn điểm gãy: $R(\ell)\to 0$.
- **(d)** $F\ge R(\ell)$ với mọi $\ell$. Nếu $R(\ell)\ge b+\eta_0$ thì $F\ge b+\eta_0$.

### Mệnh đề 2.6 (Dạng bánh cóc; đồng hồ). [Đầy đủ]
- **(a)** Mỗi lần nhận: $u\mapsto u+L(\mathbf{1}_S-\|S\|)$. Mọi độ cao tụt $L\|S\|$, chỉ cung nhận được nâng. Luật nhận không chứa $F$; $F=h_{\mathbb{T}}$.
- **(b)** Trạng thái sau $n$ ứng viên là hàm tất định của dãy nhãn; không phụ thuộc thời điểm đến.
- **(c)** Diễn biến trong vùng $A$ chỉ phụ thuộc bên ngoài qua $\Gamma$ và các cung cắt biên $\partial A$.

### Bổ đề 2.7 (Dịch ngưỡng). [Đầy đủ]
Chia $\mathbb{T}$ thành $k$ hộp $I_i$ rộng $w=1/k$, $x_i=k\hat Q(I_i)$, $y_i=\ln W(I_i)$.
- **(a)** $S\subseteq I_i$ chấp nhận được $\Leftrightarrow$ $\rho^{(i)}_S\le\theta/x_i$.
- **(b)** Phần trôi của $y_i$: $b_i^{\text{in}}=\Psi_i(\theta/x_i)$.
- **(c)** $\Psi_i$ không giảm theo $\tau$, chỉ phụ thuộc hàm chuẩn hoá trên $I_i$.

### Mệnh đề 2.8 (Phản hồi gộp). [Đầy đủ]
Đặt $\bar\Psi=\frac{1}{k}\sum\Psi_i$, $H=\frac{1}{k}\sum e_i^2$, $V=\text{Var}_i(y_i)$, $m_0$ là inf độ dốc cát tuyến của $\bar\Psi$. Khi đó:
$$\text{Cov}_i(y,b)\le -m_0 V+\sqrt{V}(\sqrt{H}+\sqrt{C_\partial}).$$

### Bổ đề 2.9 (Biên độ đáp ứng). [Đầy đủ]
$0\le\Psi_i(\tau)\le 2\lambda c\ln(w/\varepsilon)$.

### Bổ đề 2.10 (Nhiễu và sàn). [Đầy đủ]
$\hat Q(I)\ge\kappa_w w$, $\kappa_w=e^{-1-B/w}$. Tốc độ biến phân bậc hai $Q\le D$ (chặn tường minh qua $a_t(\ell)$, $\kappa_w$, $\bar\delta$). $\|b_i^\partial\|$ bị chặn tương tự.

### Bổ đề 2.11 (Bước nhảy của độ cao). [Đầy đủ]
Nếu $S'$ được nhận: $\Delta h_S=\ln(1+cq_S(S'))-L\|S'\|$; nếu từ chối: $\Delta h_S=0$.

### Bổ đề 2.12 (Ngân sách của độ cao, ba dạng). [Đầy đủ]
- **(i)** $\Delta h_S(I)=\sum_{S'\text{ nhận},S'\cap S\ne\emptyset}\ln(1+cq_S(S'))-\Delta\Gamma(I)$.
- **(ii)** $\Delta h_S(I)=\Delta\ln\hat Q(S)(I)+\Delta F(I)$.
- **(iii)** $\Delta\ln\hat Q(S)(I)=\sum_{S'\text{ nhận}}[\ln(1+cq_S(S'))-\ln(1+c\hat Q(S'))]$.

### Bổ đề 2.13 (Biên độ bước nhảy lên). [Đầy đủ]
- **(a)** $q_S(S')\le\frac{\theta}{\rho_S}\cdot\frac{\|S'\|}{\|S\|}$.
- **(b)** Nếu đóng băng từ $r_0$, $\|S\|\ge 2r_0$: $\rho_S>\theta$, bước nhảy lên $<c\|S'\|/\|S\|$.
- **(c)** $\ln(1+cq_S(S'))\le C_2(\|S\|)\frac{\|S'\|}{\|S\|}$, $C_2(w)=c\bar\delta e^{1+B^*/w}$.

### Bổ đề 2.14 (Tốc độ khối lượng nhận). [Đầy đủ]
Bù khả đoán của $A_t$: $\frac{d}{dt}\langle A\rangle_t=2\lambda\int_\varepsilon^R a_{t^-}(r)\frac{dr}{r}$. Trên $\{F_{t^-}\le b-\eta\}$: tốc độ $\ge 2\lambda(1-e^{-\eta})\ln(R/\varepsilon)$.

---

## §3. KẾT QUẢ XÁC SUẤT KHÔNG ĐIỀU KIỆN

### 3.1. Mô hình cây

### Bổ đề 3.0 (Bước nhảy của $X_Q$). [Đầy đủ]
Khi ô $D$ được nhận: nếu $D\supseteq Q$ hoặc $D\cap Q=\emptyset$: $X_Q$ không đổi; nếu $D=Q^\mp$: $X_Q\mapsto X_Q\pm L$; nếu $D\subsetneq Q^\mp$: $X_Q\mapsto X_Q\pm\ln(1+cq_D)$.

### Định lý 3.1 (Hoạt động–entropy, cây). [Đầy đủ]
Đặt $\tau_s=\frac{L}{16\lambda(L+cs)}$, $\pi(u)=\mathbb{P}(|X_Q(u)|\ge L/4)$. Khi đó:
$$\int_{t_0}^{t_1}\pi(u)du\ge\frac{\lambda\tau_s}{1+\lambda\tau_s}\int_{t_0}^{t_1-\tau_s}\mathbb{E}a_{j+1}(u)du,\qquad \mathbb{E}d_j(u)\ge\ln\cosh(L/8)\,\pi(u).$$

### Hệ quả 3.2 (Đóng băng yếu, cây). [Đầy đủ]
$$\sum_{s=0}^K\frac{\bar a_s}{L+cs}\le C_1\frac{T}{T'},\quad C_1=\frac{17B^*}{L\ln\cosh(L/8)}.$$
Nói riêng $\min_s\bar a_s\to 0$ khi $K\to\infty$.

### Hệ quả 3.3 ((L) yếu, cây). [Đầy đủ]
$$\frac{1}{T'}\int_{t_0}^{t_0+T'}\mathbb{P}(F_u\le b-\eta)du\le\frac{C_1 c\,T/T'}{(1-e^{-\eta})\ln(1+c(K+1)/L)}.$$

### 3.2. Mô hình cung (ASMS)

### Bổ đề 3.4 (Bước nhảy của $X_p$). [Đầy đủ]
Nhận cung $S$: $\Delta X_p=\ln(1+cq_A)-\ln(1+cq_B)$.
- (i) $\Delta X_p=0$ nếu $S\supseteq A_p\cup B_p$ hoặc rời.
- (ii) $|\Delta X_p|\le\min\{L,c(q_A+q_B)\}$.
- (iii) Nếu $A_p\subseteq S$, $q_B\le L/(4c)$: $\Delta X_p\ge\frac{3}{4}L$.

### Bổ đề 3.5 (Đầu mút tốt). [Dựa trích dẫn]
Điểm $y$ tốt ở thang $\rho$ nếu (a) $\hat Q([y-\delta,y))\le K_0\delta$ với $\delta\le w$, và (b) $\hat Q([y,y+\rho/2))\ge e^{-T_0\rho/2}$. Khi đó $\|\{y\text{ không tốt}\}\|\le 2/K_0+(B+1)/T_0$.

### Bổ đề 3.6 (Họ cặp gắn với một cung). [Đầy đủ]
Với cung $S=S(z,\rho)$, đầu mút phải $y=z+\rho$, đặt $P(S)$, $\nu(dp)=dx\,d\ell/(\ell\ln 2)$:
- **(a)** Nếu $y$ tốt: nhận $S$ làm $\Delta X_p\ge\frac{3}{4}L$.
- **(b)** $\nu(P(S))=\kappa_1\rho\ln 1{,}5/\ln 2$.
- **(c)** Với $p$ cố định: độ đo các $S$ có $p\in P(S)$ là $\kappa_1\ln 1{,}5$.
- **(d)** Nếu $\rho\in[\ell_k,\frac{4}{3}\ell_k]$: $P(S)\subseteq\{\ell\in[\ell_k,2\ell_k]\}$.

### Định lý 3.8 (Hoạt động–entropy, mô hình cung). [Đầy đủ, dựa Bổ đề 3.5]
$$\sum_{k=0}^{n-1}\frac{\bar a_k-p_{\text{xấu}}T/T'}{L+c(k+1)\ln 2}\le C_5\frac{T}{T'}.$$

### Hệ quả 3.9. [Đầy đủ]
- **(a)** (đóng băng yếu) Với mọi $\alpha\in(0,1]$, $\varepsilon$ đủ nhỏ: ít nhất một dải có $\bar a_k<\alpha$.
- **(b)** ((L) yếu) $\frac{1}{T'}\int\mathbb{P}(F_u\le b-\eta)du\to 0$ khi $\varepsilon\to 0$.

### 3.3. Nhám dưới thang $\varepsilon$

### Bổ đề 3.10 (Tất định). [Đầy đủ]
Với mọi trạng thái bậc thang hữu hạn bước nhảy $\pm L$ đôi một khác nhau:
$$R(2\ell)\ge 4\ell\,k(c)\cdot\#\{\text{bước nhảy cô lập ở khoảng cách }2\ell\}.$$

### Định lý 3.11 (Nhám dưới $\varepsilon$). [Đầy đủ]
Giả sử $32\Lambda_t\varepsilon\ge 1$, $\ell_t=1/(32\Lambda_t)$. Khi đó:
$$\mathbb{E}\#\{\text{bước nhảy cô lập ở }2\ell_t\}\ge\mathbb{E}N_t^{\text{acc}},\qquad \mathbb{E}F_t\ge\mathbb{E}R_t(2\ell_t)\ge\frac{k(c)}{8}\bar a_t.$$

---

## §4. LÀM PHẲNG, TỰ TRUNG BÌNH, ĐÓNG BĂNG: ĐỊNH LÝ ĐẶC TRƯNG

### Định lý 4.1 (Làm phẳng $\Leftrightarrow$ tự trung bình). [Đầy đủ]
Cho $\eta=1/k$, $I=[0,\eta)$, $p=\hat Q(I)$, $x=kp$.
- **(a)** $\mathbb{E}x=1$, $\mathbb{E}F_\eta=\mathbb{E}[-\ln x]$.
- **(b)** $\frac{1}{2}(\mathbb{E}|x-1|)^2\le\mathbb{E}F_\eta\le(6+4B^*/\eta)\text{Var}(x)$; $\text{Var}(x)\le k\mathbb{E}|x-1|$.

### Định lý 4.2 ((SA)+(L) $\Rightarrow$ đóng băng). [Đầy đủ]
Cho $r_0\in(0,R/2]$, $\eta_0\in(0,1]$, lưới $M$ tâm, $J+1$ bán kính. Khi đó:
$$\mathbb{P}(\text{không đóng băng từ }r_0)\le\mathbb{P}(F<b+\eta_0)+\frac{9M}{\eta_0^2}\sum_{j=0}^J\text{Var}(\rho_{\rho_j}(0)).$$

### Hệ quả 4.3 (Đặc trưng). [Đầy đủ]
Xét (SA), (F), (W), (L), (H*a). Khi đó:
- **(SA)** $\Leftrightarrow$ **(F)** $\Leftrightarrow$ **(W)**;
- **(SA)+(L)** $\Rightarrow$ **(H*a)** (đóng băng), và xác suất nhận một ứng viên bán kính cố định $\to 0$;
- **(H*a)** $\Rightarrow$ $\mathbb{P}(F>b)\to 1$.

### Bổ đề 4.4 (Chặn $F_\eta$ trên biến cố đóng băng). [Đầy đủ]
$$\mathbb{E}F_\eta\le\frac{\text{Var}(x)}{2\kappa^{*2}}+\sqrt{\text{Var}(x)\,\mathbb{P}(N)}+\Big(1+\frac{B^*}{\eta}\Big)\mathbb{P}(N).$$

### Định lý 4.5 (Dạng có điều kiện của Giả thuyết A).
Giả thiết (R) phòng vượt trần, (SA), (SAq).
- **(a)** (R)+(SA) $\Rightarrow$ đóng băng, $\mathbb{E}F_\eta\to 0$, $\hat Q\Rightarrow\text{Leb}$.
- **(b)** Thêm (SAq): $\mathbb{P}(N)\le C(\eta)\varepsilon$; $\mathbb{E}F_\eta\le\frac{C^{SA}}{2\kappa^{*2}}\cdot\frac{\varepsilon}{\eta}+C'(\eta)\varepsilon$.

---

## §5. ĐỊNH LÝ CO, ĐUÔI MŨ, VÀ MÔ HÌNH MỨC TẤT ĐỊNH

### 5.1. Định lý co dạng hoạt động

### Bổ đề 5.0 ($F_w$ theo $V$). [Đầy đủ]
$F_w=\ln(\frac{1}{k}\sum_i e^{z_i})$, $z_i=y_i-\bar y$. Nếu $\sigma=\max_i|z_i|$: $F_w\le\frac{1}{2}e^\sigma V$. Với trạng thái đạt được: $\sigma\le\sigma_w:=1+B/w+\ln(1/w)$, $V\le\sigma_w^2$.

### Định lý 5.1 (Co, dạng hoạt động). [Đầy đủ]
Giả sử $m_0(t)\ge m^*>0$ trên $[t_0,t_1]$. Khi đó:
$$\mathbb{E}V_t\le e^{-m^*(t-t_0)}\mathbb{E}V_{t_0}+\frac{1}{m^*}\sup_s\mathbb{E}\Big[D_s+\frac{2(H_s+C_{\partial,s})}{m^*}\Big],\quad F_w\le\frac{1}{2}e^{\sigma_w}V.$$

### Hệ quả 5.1'. [Đầy đủ]
Nếu $m_0\ge m^*$, $\int a(\ell)(2+\ell/w)d\ell\to 0$, $H\to 0$: $\limsup\mathbb{E}F_w\le\frac{1}{2}e^{\sigma_w}\sigma_w^2 e^{-m^*T}$. Nếu luật vi mô $O(\varepsilon)$: $\mathbb{E}V\lesssim\varepsilon/(m^*w)$ sau thời gian hồi phục.

### 5.2. Đuôi mũ kiểu Ornstein–Uhlenbeck

### Bổ đề 5.2. [Đầy đủ]
Cho $z_t$ thuần nhảy, $|\Delta z|\le\Delta$, trôi $\beta_t$, biến phân $q_t\le Q$, $\text{sign}(z_t)\beta_t\le-m|z_t|+E$. Đặt $\beta=\min\{1/\Delta,\sqrt{m}/(2eQ)\}$. Khi đó:
$$\mathbb{E}f(z_t)\le f(z_0)e^{-mt/4}+\frac{4C_2}{m},\qquad \mathbb{P}(|z_t|\ge s)\le 2e^{-\beta s}\Big(f(z_0)e^{-mt/4}+\frac{4C_2}{m}\Big).$$

### Bổ đề 5.3 (Từ đuôi ra đóng băng). [Đầy đủ]
Nếu $\min_i\ln x_i\ge-s$ và $e^{-s}(1-2w/\ell)>e^{b-F}$: mọi cung dài $\ge\ell$ bị từ chối. Nếu $F\ge b+\eta_0$, $s\le\eta_0/2$: đóng băng từ $\ell^*=2w/(1-e^{-\eta_0/2})$.

### 5.3. Mô hình mức tất định

**Mô hình $P(M,\gamma)$.** Thay $\Gamma_{b^-}$ bằng hàm tất định $\gamma(b)$; $R=M\varepsilon$.

### Định lý 5.3. [Dựa trích dẫn]
Trong $P(M,\gamma)$, với mọi $\gamma$ đo được, mọi cung $I$:
$$\text{Var}(\hat Q_{\varphi_t}(I))\le C_P\varepsilon(\|I\|+\varepsilon).$$

---

## §6. KHÉP VÒNG BẤT BIẾN TỈ LỆ VÀ ĐỊNH LÝ KIỂU OU

### 6.1. Độ sâu: đơn vị chung

Đặt $x_r(y)=\ln\rho_r(y)$, phòng $\eta_s=F_s-b$, $\ln\theta_s=-\eta_s$.
$$S(y,r)\text{ chấp nhận được}\;\Longleftrightarrow\; x_r(y)\le-\eta_s.$$
Hồ sơ hoạt động $a_s(r)=\|\{y:x_r(y)\le-\eta_s\}\|$; khối lượng hoạt động $D_s=\int_\varepsilon^R a_s(r)dr$.

### Bổ đề 6.1 (Trung bình theo dịch lưới). [Đầy đủ]
$$\frac{1}{\eta}\int_0^\eta F_\eta(u)du=F(\eta/2).$$

### 6.2. Bổ đề khép vòng

### Bổ đề 6.2 (Khép vòng bất biến tỉ lệ). [Đầy đủ]
Cho $a:[\varepsilon,R]\to[0,1]$, $D=\int a>0$, $\Psi$ không tăng, $J=\int_0^\infty\min\{1,\Psi(u)\}du$. Nếu $a(r)\le\Psi(r/D)$ trên $[M\varepsilon,R]$ và $J<1$:
$$D\le\frac{M\varepsilon}{1-J},\quad \int^{M\varepsilon}a\ge(1-J)D,\quad a(r)\le\Psi\Big(\frac{(1-J)r}{M\varepsilon}\Big)\;(r\ge M\varepsilon).$$

### Mệnh đề 6.3 (Điều kiện $J<1$ không bỏ được). [Đầy đủ]
Với $\Psi(u)=e^{-u/\gamma}$, $\gamma>1$ ($J=\gamma$): tồn tại $a$ thoả $a(r)\le\Psi(r/D)$ và $\int a=D$. Khi $J>1$, giả thiết dạng đuôi không chặn được $D$.

### Mệnh đề 6.4 (Sụp hồ sơ buộc $J\ge 1$). [Đầy đủ]
Nếu $a(r)=\Psi(r/D)$ trên $[\varepsilon,R]$: $\int_0^\infty\min\{1,\Psi\}\ge 1$. Bổ đề 6.2 không áp được.

### Hệ quả 6.5 (Hồ sơ Gauss). [Đầy đủ]
$\Psi_G(u)=\bar\Phi(\eta\sqrt{u}/K)$: $J(\Psi_G)=K/(2\eta^2)$. Nếu $a(r)=\bar\Phi(\eta\sqrt{r}/(KD))$: $\eta^2\le K/2$.

### 6.3–6.4. Giả thiết OU và Định lý có điều kiện

**Giả thiết (P):** $\eta_s\ge\eta_0>0$ trên $[t_1,t_2]$.

**Giả thiết (OU):** Với mọi $s$, $r\in[M\varepsilon,R]$, $\beta\in[0,\eta_0 r/(KD_s)]$:
$$\int_{\mathbb{T}}\rho_r(y)^{-\beta}dy\le\exp\Big(\frac{\beta(\beta+1)KD_s}{2r}\Big).$$

### Định lý 6.6 (Định lý OU). [Đầy đủ, dưới (P), (OU), $J<1$]
Đặt $\gamma=2K/\eta_0^2$, $J=\gamma(1+\eta_0/2)$, $\bar D=M\varepsilon/(1-J)$.
- **(i)** $a_s(r)\le e^{\eta_0/2}\exp(-\eta_0^2 r/(2KD_s))$.
- **(ii)** $D_s\le\bar D$; phần hoạt động ở $r\le M\varepsilon$ chiếm $\ge(1-J)$; $a_s(r)\le e^{\eta_0/2}\exp(-(1-J)r/(\gamma M\varepsilon))$.
- **(iii)** (Đóng băng) Nếu $r_0\ge M\varepsilon/(1-\delta)$ và điều kiện (6.1): không cung nào $\in[r_0,R]$ chấp nhận được.
- **(iv)** (Làm phẳng) $F(r)_s\le K\bar D/(2r)$. Trung bình dịch lưới: $\frac{1}{\eta}\int F_\eta(u)du\le\frac{KM}{1-J}\cdot\frac{\varepsilon}{\eta}$.

---

## §7. ĐỘNG LỰC CỦA THẾ NĂNG VÀ PHÒNG DƯƠNG CÓ ĐIỀU KIỆN

### 7.1. Ký hiệu
$$a_s(r)=|\{y:\rho_r(y)\le\theta_s\}|,\quad G^\circ_s(r)=\int\mathbf{1}_{\{\rho_r\le\theta_s\}}\rho_r\,dy,$$
$$A_s=\int_\varepsilon^R a_s(r)\frac{dr}{r},\quad G_s=\int_\varepsilon^R G^\circ_s(r)\frac{dr}{r},\quad D_s=\int_\varepsilon^R a_s(r)dr.$$
Khi $A_s>0$: $g_s=G_s/A_s$ (mật độ trung bình cung nhận). Luôn $g_s\le\theta_s$.

### 7.2. Phân rã của thế năng

### Bổ đề 7.1 (Phần trôi và phần martingale của $F$). [Đầy đủ, dựa [B7]]
$$F_t=F_{t_1}+\int_{t_1}^t\beta_s\,ds+(M_t-M_{t_1}),$$
$M$ martingale bình phương khả tích, và
$$2\lambda(cG_s-LA_s)-2\lambda c^2\theta_s^2 D_s\le\beta_s\le 2\lambda(cG_s-LA_s).$$
$$\mathbb{E}[(M_t-M_{t_1})^2]\le 4\lambda c^2\bar\delta^2\,\mathbb{E}\int_{t_1}^t D_s\,ds.$$

### Hệ quả 7.2 (Luật $L/c$ theo trung bình thời gian). [Đầy đủ]
$$\Big|\frac{1}{t_2-t_1}\mathbb{E}\int_{t_1}^{t_2}2\lambda(cG_s-LA_s)ds\Big|\le\frac{B^*}{t_2-t_1}+\frac{2\lambda c^2\bar\delta^2}{t_2-t_1}\mathbb{E}\int_{t_1}^{t_2}D_s\,ds.$$

### 7.3. Đơn điệu theo ngưỡng

### Bổ đề 7.3 (Đơn điệu). [Đầy đủ]
$\Phi(\theta)=cG(\theta)-LA(\theta)$:
- **(a)** $A$, $G$, $g$ không giảm; $g(\theta)\le\theta$.
- **(b)** $\Phi$ không tăng trên $[0,L/c]$, không giảm trên $[L/c,\infty)$.
- **(c)** $\theta_s\ge\kappa^*=L/c$ luôn. Nếu $F_{s^-}\ge b$: $\Phi_s(\theta_s)\le\Phi_s(1)$; nếu $F_{s^-}\le b$: ngược lại.

### 7.4. Phòng dương có điều kiện

**Giả thiết (H):** Trên $[t_1,t_2]$, với $\eta_0,\kappa_1,C_0,p_H$: với xác suất $\ge 1-p_H$, mọi $u<v$ có $F_{s^-}\le b+\eta_0$ trên $(u,v]$:
$$\int_u^v\Phi_s\,ds\ge\kappa_1(v-u)-C_0.$$

### Định lý 7.4 (Phòng dương có điều kiện). [Đầy đủ, dưới (H)]
Đặt $\tau=(b+\eta_0)/(2\lambda\kappa_1)$. Với mọi $t\in[t_1+\tau,t_2]$:
$$\mathbb{P}(F_t\le b+\eta_0/2)\le p_H+\lambda c^2\bar\delta^2\Big(\frac{16}{\eta_0}+\frac{1024}{\eta_0^2}\Big)\mathbb{E}\int_{t_1}^t D_s\,ds.$$

### Hệ quả 7.5. [Đầy đủ]
Nếu (H) với hằng không phụ thuộc $\varepsilon$, $p_H\to 0$, $\mathbb{E}\int D\to 0$: $\mathbb{P}(F_t\ge b+\eta_0/2)\to 1$. Đây là (L) của Hệ quả 4.3 và (P) của Định lý 6.6.

### 7.5. Phòng âm có điều kiện

**Giả thiết (H⁻):** Tương tự (H) nhưng $\int_u^v\Phi_s\,ds\le-\kappa_1(v-u)+C_0$ khi $F_{s^-}\ge b-\eta_1$.

### Định lý 7.6 (Phòng âm có điều kiện). [Đầy đủ, dưới (H⁻)]
Đặt $\tau^-=(B^*-b+\eta_1)/(2\lambda\kappa_1)$:
$$\mathbb{P}(F_t\ge b-\eta_1/2)\le p_H+\frac{256\lambda c^2\bar\delta^2}{\eta_1^2}\mathbb{E}\int_{t_1}^t D_s\,ds.$$

---

## §8. GIẢ THUYẾT A VÀ CÁC BÀI TOÁN MỞ

### Giả thuyết A.
Cố định $c,\bar\delta,\lambda,R$. Tồn tại $t_c<\infty$ sao cho với mọi $t\ge t_c$, $\varepsilon\to 0$:
- **(a)** $\forall r_0>0$: $\mathbb{P}(\tilde\Phi^\varepsilon_t\text{ đóng băng từ }r_0)\to 1$.
- **(b)** $\exists C(t)$: $\mathbb{E}F_\eta(\tilde\Phi^\varepsilon_t)\le C(t)\varepsilon/\eta$.

---

## §9. MÔ HÌNH KHOÁ PHÒNG: CHUYỂN PHA

### 9.1. Định nghĩa

**Mô hình khoá phòng $K(\eta)$.** Luật nhận: $S$ được nhận $\Leftrightarrow$ $\rho_S\le\theta:=e^{-\eta}$, $\eta$ hằng số.

**Giả thuyết B (Chuyển pha).** $\exists\eta_c(c)\in(0,\ln(c/L))$: trong $K(\eta)$:
- $\eta>\eta_c$: $D=O(\varepsilon)$, không cung $\ge r_0$ được nhận (xác suất $\to 1$).
- $\eta<\eta_c$: $D$ không tiến về 0.

### 9.2. Chế độ dưới tới hạn mạnh

### Định lý 9.1. [Đầy đủ]
Trong $K(\eta)$ với $\theta=e^{-\eta}<L/c$, mọi dãy ứng viên, mọi $t_0$:
$$(L-c\theta)\sum_{S\text{ nhận sau }t_0}\|S\|\le F_{t_0}.$$
Hệ quả: (a) số cung $\ge r_0$ nhận sau $t_0$ không vượt $F_{t_0}/(2r_0(L-c\theta))$; (b) $2\lambda\mathbb{E}\int_{t_0}^\infty A_s\,ds\le\mathbb{E}F_{t_0}/(L-c\theta)$; (c) nếu từ GEOM: $F_{t_0}\le B^*$.

### 9.3. Hõm sâu chứa dày đặc chỗ nhận

### Bổ đề 9.2. [Đầy đủ]
Cho cung $S$ dài $\ell$, $\rho_S\le\theta e^{-x}$, $x>\ln 2$. Với mọi $r'\le\ell/4$: tỉ lệ tâm $y$ có $\rho_{r'}(y)\le\theta$ ít nhất $1-e^{-x}\frac{\ell}{\ell-2r'}\ge 1-2e^{-x}$.

### Hệ quả 9.3 (Lấp tích luỹ trong hõm sâu). [Đầy đủ]
Tại mọi $s$ có $\rho_S\le\theta_s e^{-x}$:
- **(a)** tốc độ bù của tổng độ dài cung nhận nằm trọn trong $S$ $\ge\lambda\ell(1-2e^{-x})\ln\frac{\ell}{4\varepsilon}$.
- **(b)** tốc độ trôi của $\bar\varphi_S-\Gamma\ge\lambda L[(1-2e^{-x})\ln\frac{\ell}{4\varepsilon}-2A_s]$.

### 9.4. Không có trận lở

### Bổ đề 9.4. [Đầy đủ]
Khi nhận $S'$:
- **(a)** $\Delta\ln\rho_S\ge-\ln(1+c\hat Q(S'))\ge-c\theta\|S'\|$ (dấu bằng khi $S\cap S'=\emptyset$).
- **(b)** $\Delta\ln\rho_{S'}=\ln(1+c)-\ln(1+c\hat Q(S'))\ge L-c\theta\|S'\|$.

### 9.5. Độ nhạy của các tầng mịn

### Bổ đề 9.5 (Đồng vùng). [Đầy đủ]
Gọi $y_1,\dots,y_N$ là các điểm cắt mức $\theta$ của $g(y)=\rho_{r'}(y)$:
$$\liminf_{x\downarrow 0}\frac{\|\{y:\theta<g(y)\le\theta e^x\}\|}{x}\ge\frac{2\theta r'}{N}\sum_i\frac{1}{\rho(y_i+r')+\rho(y_i-r')}.$$

### Bổ đề 9.6 (Thành phần ngắn). [Đầy đủ]
Nếu mọi cung tâm $y\in I$ dài $\Lambda\ge 4r'$ đều có $\rho_{r'}(y)\le\theta$: cung $J\subset I$ dài $\Lambda-2r'$ thoả $\rho_J\le\theta\frac{\Lambda}{\Lambda-2r'}$.

### Hệ quả 9.7 (Đóng băng có lề $\Rightarrow$ độ nhạy ở tầng mịn). [Đầy đủ]
Nếu mọi cung dài $\ge\lambda_0$ có $\rho_J>\theta(1+\delta)$: mọi thành phần liên thông của $\{\rho_{r'}\le\theta\}$ dài $<\Lambda_0$; số điểm cắt $\ge 2a(r')/\Lambda_0$; độ nhạy $\ge\frac{4\theta r'a(r')}{\Lambda_0\bar\rho_{\text{cắt}}}$.

### 9.6. Nhiễu của một hộp

### Bổ đề 9.8 (Bước nhảy của một hộp). [Đầy đủ]
$z_t=\ln(\hat Q_t(I)/(\|I\|\theta))$.
- **(a)** $\Delta z\ge-\ln(1+c\hat Q(S'))\ge-c\theta\|S'\|$.
- **(b)** Nếu $S'\cap I=\emptyset$: $\Delta z=-\ln(1+c\hat Q(S'))\in[-c\theta\|S'\|,0]$.
- **(c)** Nếu $\hat Q(I)>\theta\|I\|$: $\Delta z\le c\|S'\|/\ell$.
- **(d)** Tốc độ bù của $\sum(\Delta z)^2$ trên bước xuống $\le 4c^2\theta^2\lambda D$.

### Bổ đề 9.9 (Siêu martingale mũ một phía). [Đầy đủ]
$h(z)=e^{-\beta z}$, mọi bước xuống $\le\Delta_d$:
$$Ah(z_t)\le h(z_t)\Big[-\beta b_t+\frac{\beta^2}{2}e^{\beta\Delta_d}Q_t\Big].$$

### Định lý 9.10 (Đuôi một phía của một hộp, có điều kiện). [Đầy đủ]
Giả sử (R) lực lấp $b_t\ge\kappa_R$ khi $0<z_t\le z_1$; nhiễu $Q_t\le\bar Q$, $|b_t|\le b_{\max}$; bước xuống $\le\Delta_d$. Đặt $\beta=\min\{1/\Delta_d,\kappa_R/(e\bar Q)\}$, $\sigma=\inf\{t:z_t\le 0\}$:
$$\mathbb{P}(\sigma\le T\wedge\tau)\le e^{-\beta z_0}+Te^{-\beta z_1}(\beta b_{\max}+\tfrac{e}{2}\beta^2\bar Q).$$

### 9.7. Hộp như một cung lớn: tái chuẩn hoá theo khối

### Bổ đề 9.11 (Tương đương với bên ngoài). [Đầy đủ]
Quyết định nhận $S'$ và tác động lên mọi hộp rời $I$ chỉ phụ thuộc cấu hình bên trong $I$ qua $\hat Q(I)$.

### Bổ đề 9.12 (Đệ quy theo khối). [Đầy đủ]
$$\tilde b_I=\sum_{k=1}^n\frac{\hat Q(J_k)}{\hat Q(I)}\tilde b_{J_k}+\tilde b_I^{\text{nối}},\quad \tilde b_I^{\text{nối}}\ge 0.$$

### Bổ đề 9.13 (Khoảng Jensen). [Đầy đủ]
$$\sum_k w_k z_k=z_I+\mathrm{KL}(w\|U_n),\quad 0\le\mathrm{KL}(w\|U_n)\le\frac{1}{2}e^{2M}V.$$

### Bổ đề 9.14 (Bước trung bình). [Đầy đủ]
Nếu $\tilde b_{J_k}\ge G-mz_k+\xi_k$: $\tilde b_I\ge G-mz_I-m\frac{1}{2}e^{2M}V+\sum_k w_k\xi_k+\tilde b_I^{\text{nối}}$.

### Hệ quả 9.15 (Lặp qua các thang). [Đầy đủ]
$$\tilde b_I\ge G-mz_I-m\sum_{i=1}^j K_i(I)+\Xi_I.$$

### Bổ đề 9.16 (Lấp là hàm đơn điệu của mức). [Đầy đủ]
- **(a)** $\tilde b_I=c\Psi_I(e^{-z_I})$.
- **(b)** $\tilde b_I$ không tăng theo $z_I$ khi hình dạng cố định.
- **(c)** Hộp cơ sở ($\ell\le 2\varepsilon(1+\delta)$): mọi $S\in S(I)$ có $1-e^{\omega_I\delta}\le\nu_I(S)\le 1+\delta$; $\tilde b_I=0$ khi $z_I>\ln(1+\delta)$; $\Psi_I(\infty)\le\lambda\delta^2/\varepsilon$.

### Bổ đề 9.17 (Đệ quy cho hàm phân phối). [Đầy đủ]
$$\Psi_I(t)=\sum_{k=1}^n w_k\Psi_{J_k}(te^{z_I-z_k})+\Psi_I^{\text{nối}}(t).$$

### Hệ quả 9.18 (Truyền chặn dưới lồi qua các thang). [Đầy đủ]
Nếu $g$ lồi, không tăng, mọi hộp con thoả $\tilde b_{J_k}\ge g(z_k)$: $\tilde b_I\ge g(z_I+\mathrm{KL}(w\|U_n))+\tilde b_I^{\text{nối}}$. Lặp: $\tilde b_I\ge g(z_I+\sum_i K_i(I))$.

### Bổ đề 9.19 (Nón ánh sáng). [Đầy đủ]
Trong $P(M,\gamma)$, $\text{dist}(A,B)\ge d$:
$$|\text{Cov}(f,g)|\le 2\|f\|_\infty\|g\|_\infty(p_A+p_B),\quad p_A\le\lambda t\Big(\frac{\|A\|}{\varepsilon}+2\ln M\Big)\frac{(e^{\beta t})^{k_0}-1}{k_0-1}.$$

### 9.9. Thế năng là tổng độ gồ ghề qua các thang

### Bổ đề 9.20 (Phân rã đa thang của $F$). [Đầy đủ]
$$F=\sum_{j\ge 0}\sum_{I\in P_j}\|I\|\,J_I,\quad 0\le J_I\le\frac{1}{2}e^{2M_I}M_I^2.$$

### Bổ đề 9.21. [Đầy đủ]
Với $\theta>1$: $a\ge 1-1/\theta$; $G^\circ\ge a\exp(-(F+1/e)/a)$.

### Mệnh đề 9.22 (Pha nóng sâu không kéo dài). [Đầy đủ]
Giả sử $h(0)<\ln(c/L)$, $F^*\in(0,F_e)$, $K>0$, $\Delta=F^*/(\lambda K)$:
$$\mathbb{P}(F_s\le F^*\;\forall s\in[t_1,t_1+\Delta])\le\frac{4c^2\bar\delta^2 R}{KF^*}.$$
Cả $\Delta$ lẫn xác suất $\to 0$ khi $\varepsilon\to 0$, cỡ $1/\ln(1/\varepsilon)$.

### Bổ đề 9.23 (Đồng vùng theo dải). [Đầy đủ]
$$\frac{\|Y_B\|}{x}\ge\frac{2r'}{\sqrt{M_B}}\cdot\frac{1}{\theta x}\int_B N(s)ds\ge\frac{2r'\min_{s\in B}N(s)}{\sqrt{M_B}}.$$

### 9.10. Điểm cao bị chặn: động học của độ lệch điểm–vùng

### Bổ đề 9.24 (Vượt trần tối đa một lớp; đỉnh trong cung nhận phải hẹp). [Đầy đủ]
- **(a)** $|\{x\in S:\rho(x)\ge K\theta\}|\le\|S\|/K$.
- **(b)** Ngay sau nhận: $\rho'_S\le(1+c)\theta$; mọi cung con $J\subseteq S$, $\|J\|\ge\|S\|/m$: $\rho'_J\le m(1+c)\theta$.

### Hệ quả 9.25 (Đồng vùng theo dải, dạng toàn cục). [Đầy đủ]
$$\|Y_B\|\ge\frac{r'^2\|\rho\|_2^2\big(\int_B N(s)ds\big)^2}{1}\ge\frac{r'^2\theta^2 x^2(\min_B N)^2}{\|\rho\|_2^2}.$$

### Bổ đề 9.26 (Động học của độ lệch điểm–vùng). [Đầy đủ]
$D(x)=\varphi(x)-\frac{1}{2\varepsilon}\int_W\varphi$. Khi nhận $S$: $\Delta_S=L(\mathbf{1}_{x\in S}-\|S\cap W\|/(2\varepsilon))$.
- **(a)** $\Delta_S=0$ nếu $S\supseteq W$ hoặc rời.
- **(b)** $0\le\Delta_S\le L/2$ nếu $x\in S$; $-L/2\le\Delta_S\le 0$ nếu $x\notin S$.
- **(c)** Tổng cường độ $\le 4\lambda$.

**Giả thuyết E (Hạ gai).** $\exists a,\kappa>0$: mọi trạng thái có $D(x)\ge a$: $A_D(x)\le-\kappa$.

### Mệnh đề 9.27 (Giả thuyết E $\Rightarrow$ đuôi mũ đều). [Đầy đủ, có điều kiện]
$\beta=\min\{2/L,\kappa/(e\lambda L^2)\}$:
$$\mathbb{E}e^{\beta D_t(x)}\le\max\{\mathbb{E}e^{\beta D_0(x)},e^{\beta a}(1+2(2+e)\lambda L/\kappa)\}.$$

**Giả thuyết E' (Hạ gai tuyến tính).** $A_D(x)\le-\kappa(D(x)-a)$.

### Mệnh đề 9.28 (Giả thuyết E' $\Rightarrow$ mọi mô-men mũ bị chặn đều). [Đầy đủ, có điều kiện]
Với mọi $\beta>0$: $\mathbb{E}e^{\beta D_t(x)}\le\max\{\mathbb{E}e^{\beta D_0(x)},e^{\beta b}(1+(2\lambda L+C(\beta))/\kappa)\}$.

### Bổ đề 9.29 (Phân rã Haar). [Đầy đủ]
$$\varphi(x)-\varphi(W_0)=\frac{1}{2}\sum_{j\ge 0}\sigma_j(x)d_j.$$

### Bổ đề 9.30 (Động học Haar). [Đầy đủ]
- **(a)** Nhận $S^-(e,r)$: $d$ tăng $L\tau(e)$; nhận $S^+(e,r)$: giảm $L\tau(e)$.
- **(b)** $A_d=\lambda L\int_B\tau(e)\int_\varepsilon^R(\mathbf{1}_{S^-\text{ nhận}}-\mathbf{1}_{S^+\text{ nhận}})\frac{dr}{r^2}de$.
- **(c)** $|\Delta d|\le L$; tổng cường độ $\le 4\lambda b/\varepsilon$; biến phân bậc hai $\le\frac{4}{3}\lambda L^2 b/\varepsilon$.

---

## §10. KHUNG KHỞI ĐỘNG HỢP NHẤT VÀ ĐỊNH LÝ TRUNG TÂM CÓ ĐIỀU KIỆN

### 10.1. Đóng băng kéo theo hoạt động nhỏ

**Giả thiết (Đ$_{\lambda_0}$):** với xác suất $\ge 1-p$, mọi cung dài $\ge\lambda_0$ có $\rho_S>\theta_s$.

### Bổ đề 10.1. [Đầy đủ]
Trên biến cố của (Đ$_{\lambda_0}$): $D_s\le\lambda_0/2$. Luôn $D_s\le R$.

### 10.2. Định lý trung tâm có điều kiện

### Định lý 10.2. [Đầy đủ, dưới (H) và (Đ)]
$$\mathbb{P}(\eta_t\le\eta_0/2)\le p_H+C(\eta_0)(t-t_1)\Big(\frac{\lambda_0}{2}+Rp\Big).$$

### Hệ quả 10.3. [Đầy đủ]
Nếu (H) với hằng không phụ thuộc $\varepsilon$, $p_H\to 0$; (Đ$_{\lambda_0}$) với $\lambda_0\to 0$, $p\to 0$: $\mathbb{P}(\eta_t\le\eta_0/2)\to 0$. Đây là Giả thuyết A(a).

### 10.6. Bước cục bộ–toàn cục

### Bổ đề 10.4 (Bất biến quay). [Đầy đủ]
$\mathbb{E}D_s=\int_\varepsilon^R p_s(r)dr$, với $p_s(r)=\mathbb{P}(\rho_{S(0,r)}\le\theta_s)$.

**Giả thiết (Đ'):** $\exists g(u)\to 0$: $p_s(r)\le g(r/\varepsilon)$.

### Định lý 10.5 (Định lý trung tâm, dạng cục bộ). [Đầy đủ, dưới (H) và (Đ')]
$\mathbb{P}(\eta_t\le\eta_0/2)\to 0$.

### Bổ đề 10.6 (Hệ quả 9.7, dạng cục bộ). [Đầy đủ]
$N\ge 2(a-\|Bad\|)/\Lambda_0$.

### 10.7. Đuôi trên của hộp cỡ $\varepsilon$

### Mệnh đề 10.7 (Đuôi trên của hộp cỡ $\varepsilon$, có điều kiện). [Đầy đủ, trong khuôn khổ khởi động]
$$\mathbb{E}[e^{\beta\zeta_t};\tau>t]\le e^{-\alpha(t-t_1)}\mathbb{E}e^{\beta\zeta_{t_1}}+e^{\beta\zeta^*}\Big(\frac{2\Lambda_M(e^{\beta L}-1)}{\lambda\beta\gamma_0}+1\Big).$$

### 10.8. Khi nào hệ có thể đóng băng hoàn toàn

### Bổ đề 10.8 (Đóng băng hoàn toàn cần độ xốp dưới $\varepsilon$ lớn). [Đầy đủ]
- **(a)** $\int_{\{\rho_\varepsilon\le\theta\}}\ln\frac{\theta}{\rho_\varepsilon}dy\ge\ln\bar\delta-F_{<\varepsilon}$.
- **(b)** Nếu không cung $\varepsilon$ nào hợp lệ: $F_{<\varepsilon}>\ln\bar\delta$.

### 10.9. Nhiễu theo luật

**Giả thuyết D' (Tương quan tắt dần).** $|\text{Cov}(\chi_k(s),\chi_l(s'))|\le X^2(e^{-|s-s'|/\tau_D}h(|k-l|)+\delta_\varepsilon)$.

### Bổ đề 10.9 (Luật số lớn cho nhiễu tái chuẩn hoá). [Đầy đủ, dưới D']
$$\text{Var}(\Xi_{u,v})\le\frac{2X^2\tau_D H}{n(v-u)}+X^2\delta_\varepsilon.$$

### Mệnh đề 10.10 (Đuôi một phía, dạng trung bình theo thời gian). [Đầy đủ]
$$\mathbb{P}(z_t\le z_1/2)\le p_R+\frac{64}{z_1^2}\mathbb{E}(N_t-N_{t_1})^2.$$

### Hệ quả 10.11 (Từ D' tới lực lấp trung bình: bước phủ lưới). [Đầy đủ]
$p_R\le\frac{X^2}{x^2}\Big(\frac{2\tau_D H}{n\delta}T(1+\ln(T/\delta))+\frac{T^2}{\delta^2}\delta_\varepsilon\Big)$.

### Bổ đề 10.12 (Nhiễu của một hộp nhỏ dần khi hộp lớn). [Đầy đủ]
$$\mathbb{E}Q\le\int_{t_1}^t\Big[8\lambda c^2 e^{2z_b}\frac{1}{\ell}\Big(\mathbb{E}D_s+\frac{2}{\ell}\int_\varepsilon^R r\,p_s(r)dr\Big)+8\lambda L^2\mathbb{E}D_s\Big]ds.$$

### 10.10. Hai kết quả về cấu trúc

### Bổ đề 10.13 (Đối xứng gương và đồng nhất thức năng lượng). [Đầy đủ]
- **(a)** $\mathbb{E}[A_d(s)f(d(s))]=-\mathbb{E}[A_d(s)f(-d(s))]$. Trôi có điều kiện là hàm lẻ.
- **(b)** $\frac{d}{ds}\mathbb{E}[d(s)^2]=2\mathbb{E}[d(s)A_d(s)]+\mathbb{E}V(s)$.
- **(c)** Nếu $\sup_s\mathbb{E}d(s)^2\le\Sigma$: $\frac{1}{T}\int_0^T\mathbb{E}[dA_d]ds\le-\frac{1}{2T}\int_0^T\mathbb{E}V\,ds+\frac{\Sigma}{2T}$.

### Nhận xét 10.14. (H) không thể là tính chất tất định của cấu hình.

### Bổ đề 10.16 ((H) như một "ngân sách độ sâu"). [Đầy đủ]
Đặt $h=B^*-F=\ln(c/L)-\eta$:
$$\Phi_r=L\int_{\{\rho_r\le\theta\}}(e^{h-dep_r(y)}-1)dy\ge L\,a(r)(e^{h-dep_r}-1).$$

### 10.12. Giả thuyết 5: đồng hồ lớp

### Bổ đề 10.17 (Chặn kiểu nhiễu bắn, theo từng quỹ đạo). [Đầy đủ]
$$Y_t\le Y_{t_1}e^{-L(\Gamma_t-\Gamma_{t_1})}+\frac{cM}{2}\sum_i e^{-L(\Gamma_t-\Gamma_{\tau_i^-})}.$$

**Giả thuyết 5'' (Không có điểm nóng theo đồng hồ lớp).** $\mathbb{E}[N_k(t)^\beta;\text{đóng băng gần }W]\le\bar N_\beta$.

### Hệ quả 10.18 (Đuôi trên, không cần "hoạt động còn"). [Đầy đủ, dưới 5'']
$$\mathbb{E}[Y_t^\beta;\cdot]\le 2^{\beta-1}\Big(\mathbb{E}Y_{t_1}^\beta+\Big(\frac{M(1+c)}{2}\Big)^\beta\bar N_\beta\Big).$$

### 10.13–10.14. Khép vòng theo thang; dạng mũ trong đồng hồ lớp

### Mệnh đề 10.19 (Mệnh đề 10.10 trên cửa sổ trượt). [Đầy đủ]
$$\mathbb{P}(z_t\le z_1/2)\le p_R+\mathbb{P}(z_{t-\tau_R}<-z_b)+\frac{64}{z_1^2}\mathbb{E}(N_t-N_{t-\tau_R})^2.$$

### Bổ đề 10.20 (Hộp quá thưa, chặn đa thức). [Đầy đủ]
$\mathbb{P}(z_I(t)\le-z)\le(B^*+1/e)/(z-\ln\bar\delta)$.

### Mệnh đề 10.21 (Bền vững mũ của một hộp). [Đầy đủ, dưới (S), (R̄Γ), (VΓ)]
$$\mathbb{P}(\exists s\in[t_1,t]:z_s\le z_1/2)\le p_R+p_V+p_S+\Big(1+\frac{\mathbb{E}[\text{Fill}_t]}{a}\Big)\exp\Big(-\min\Big\{\frac{5\kappa z_1}{16v_\Gamma},\frac{25z_1^2}{512C_V}\Big\}\Big).$$

### Hệ quả 10.22 (Đuôi mũ theo thang, và vòng khép). [Đầy đủ]
$$\mathbb{P}(\exists s:z_s\le z_1/2)\le p_R+p_V+p_S+\Big(1+\frac{f_0(1+\mathbb{E}\Gamma_t)}{z_1}\Big)\exp(-c_1\ell/\varepsilon).$$

### Bổ đề 10.24 (Đồng nhất thức lấp). [Đầy đủ]
$\text{Fill}_v-\text{Fill}_u=(z_v-z_u)+L(\Gamma_v-\Gamma_u)$.

### 10.15. Lõi 1: đuôi dưới mỏng ở thang vừa

### Bổ đề 10.25 (Cung hợp lệ nông khi đuôi dưới mỏng). [Đầy đủ]
Nếu $\|\{y:X(y)\le-t\}\|\le K_r e^{-(\mu_r+t)^2/(2s_r^2)}$:
$$\int_{\{X\le 0\}}dep\,dy\le K_r\frac{s_r^2}{\mu_r}e^{-\mu_r^2/(2s_r^2)},\quad \Phi_r\ge L\Big(ha_r-K_r\frac{s_r^2}{\mu_r}e^{-\mu_r^2/(2s_r^2)}\Big).$$

### 10.16. Độc lập gần theo không gian: dạng chặt

### Bổ đề 10.26 (Ba cách nhìn $W_r$). [Đầy đủ]
$W_r=\int(\rho_r(y)-1)^2dy$.
- **(a)** (Fourier) $W_r=\sum_{k\ne 0}|\hat Q_k|^2\big(\frac{\sin 2\pi kr}{2\pi kr}\big)^2$; $W_{r_1}\le\sum_{k\ne 0}|\hat Q_k|^2\min(\ln\frac{R}{r_1},\frac{1}{8\pi^2 k^2 r_1^2})$.
- **(b)** (Kỳ vọng) $\mathbb{E}[\rho_r(y)|\mathcal{E}]=1$; $\mathbb{E}[W_r|\mathcal{E}]=\text{Var}(\rho_r(0)|\mathcal{E})$.
- **(c)** (Điều kiện đủ theo khối) Nếu $\sum_{|d|<n}|\text{Cov}(m(0),m(db)|\mathcal{E})|\le\sigma_b^2$: $\mathbb{E}[W_r|\mathcal{E}]\le\sigma_b^2 b/n$.

**Giả thiết (Vρ):** $\mathbb{E}[W_r|\mathcal{E}]\le\sigma^2\varepsilon/r$.

### Mệnh đề 10.27 (Lực đẩy ở đáy, từng quỹ đạo). [Đầy đủ]
Tại thời điểm có $\theta\ge\theta_1>1$:
- **(i)** $\Phi_r\ge c-L-cA(\theta_1)W_r$.
- **(ii)** $\Phi_r\ge c-L-cF_r/\kappa(\theta_1)$.
- **(iii)** $\Phi_r\ge-L$.
$$\Phi\ge(c-L)\ln\frac{R}{r_1}-L\ln\frac{r_1}{\varepsilon}-cA(\theta_1)W_{r_1};\quad \Phi\ge\Big(c-L-\frac{cF}{\kappa(\theta_1)}\Big)\ln\frac{R}{\varepsilon}.$$

### Hệ quả 10.28 (Thoát khỏi đáy). [Đầy đủ]
Nếu $\Phi_s\ge\kappa^*\ln(R/\varepsilon)+c^2\bar\delta^2 R$ trên $\{F_{s^-}\le f\}$: $\mathbb{P}(\tau_f>t_1+T)\le\mathbb{P}(G^c)+\frac{4c^2\bar\delta^2 R}{\kappa^* f\ln(R/\varepsilon)}$.

### Bổ đề 10.29 (Hoạt động khi ngưỡng dưới trung bình). [Đầy đủ]
- **(a)** $a(r)\le W_r/(1-\theta)^2$; $D\le\int\min(1,W_r/(1-\theta)^2)dr$.
- **(b)** Dưới (Vρ): $\mathbb{E}[D_s;\eta_s\ge\eta_2]\le K_2(1+\ln^+(R/K_2))$.

### 10.17. Chống tập trung từ hai phía của độ gồ ghề

### Bổ đề 10.30 (Paley–Zygmund từng quỹ đạo). [Đầy đủ]
$$a(r)\ge\frac{((U_r/2-x)^+)^2}{W_r},\quad x=(1-\theta)^+.$$

**Giả thiết (W±, ND):** $w^-\varepsilon/r\le W_r\le w^+\varepsilon/r$; $U_r\ge\gamma\sqrt{W_r}$.

### Mệnh đề 10.31 ((H) từng quỹ đạo, kể cả dải tới hạn). [Đầy đủ]
$$\Phi\ge\varphi_0\min\Big(\ln\frac{\Lambda_b}{x^2},\ln\frac{R}{\Lambda_a\varepsilon}\Big)-L\ln^+\Lambda_a-\frac{16c\theta'w^+}{u^2\gamma^2 w^-}x^2=:\Phi_{\min}(x).$$
Với mọi $\kappa>0$, $\exists x_0$: $\Phi\ge\kappa$ tại mọi thời điểm có $\eta\le\eta_0$.

### Định lý 10.32 (Định lý trung tâm dưới (W±, ND)). [Đầy đủ]
Nếu (W±, ND) đúng với $p_W\to 0$: $\mathbb{P}(\eta_t\le\eta_0/2)\to 0$. Không cần (Đ').

### Bổ đề 10.34 (Đóng băng chỉ xảy ra khi phòng dương). [Đầy đủ]
Nếu không cung $r$ nào hợp lệ: $\theta<1$, $U_r<2(1-\theta)$, $\eta>-\ln(1-U_r/2)\ge U_r/2$.

### Bổ đề 10.35 (Chuỗi nhảy). [Đầy đủ]
$(X_n)$ là xích Markov; cung tiếp theo có mật độ $\frac{\mathbf{1}_{\rho^{X_n}\le\theta}}{Z(X_n)}\frac{dy\,dr}{r^2}$; thời gian chờ $\sim\text{Exp}(\lambda Z(X_n))$.

### 10.18. Độ gồ ghề theo từng mode Fourier

### Bổ đề 10.37 (Cập nhật một mode là chính xác). [Đầy đủ]
$\hat Q'_k=(1-\mu)\hat Q_k+\mu B_k$; $|\hat Q'_k|^2=(1-\mu)^2|\hat Q_k|^2+2\mu(1-\mu)\text{Re}(\hat Q_k\bar B_k)+\mu^2|B_k|^2$.

### Mệnh đề 10.38 (Cân bằng mode theo kỳ vọng). [Đầy đủ, dưới (LRk), (Nk)]
$$\mathbb{E}v_n\ge\frac{m^-}{m^+}\cdot\frac{\nu^-}{\kappa}(1-(1-\kappa m^+)^n);\quad \limsup_n\mathbb{E}v_n\le\frac{m^+}{m^-}\cdot\frac{\nu^+}{\kappa'}.$$

### Hệ quả 10.39 ((W±) theo kỳ vọng). [Đầy đủ]
$\mathbb{E}W_r(X_n)\gtrsim\varepsilon/r$ sau cỡ một lớp.

### Nhận xét 10.42. (LRk) không thể đúng cho mọi trạng thái.

### Bổ đề 10.43 (Cú hích tất định). [Đầy đủ]
$\max(|\hat Q_k(X_n)|,|\hat Q_k(X_{n+1})|)\ge\frac{1}{2}\mu_{n+1}|B_k^{(n+1)}|$; $|B_k|\ge\cos(2\pi kr')\ge 1/\sqrt{2}$ khi $r'\le 1/(8|k|)$.

### Mệnh đề 10.44 ((W−) theo kỳ vọng, không cần phản ứng tuyến tính). [Đầy đủ, dưới (A+), (Nk)]
$u_n\ge u^*(1-(1-2m^+)^n)$; nếu $\nu^-\ge\nu_0\varepsilon$: $u^*=g^2\varepsilon$, $g>0$.

### Mệnh đề 10.41 (Tập trung của $W_r$ qua các mode). [Đầy đủ]
$$\frac{\text{Var}(W_r)}{(\mathbb{E}W_r)^2}\le\frac{2C^2 M_r}{\mathbb{E}W_r}+\zeta.$$

### 10.20. (L$_{\text{loc}}$) trong mô hình mức tất định

### Mệnh đề 10.46 ((L$_{\text{loc}}$) trong $P(M,\gamma)$ tại mỗi $t$ cố định). [Đầy đủ]
$\mathbb{E}|\hat G_k|^2\le C_G\varepsilon$, $C_G=\|G\|_\infty^2[4M_G+8M(e^{2\beta t}+1)+32MP_0 e^{-e^{2\beta t}}]$.

### Mệnh đề 10.48 (So sánh với ngưỡng tất định). [Đầy đủ]
- **(a)** Trên $E_\delta$: $\varphi^{(1)}_t=\varphi^{(2)}_t$ ngoài $D_t$.
- **(b)** $\mathbb{E}\|D_t\|\le 2M\varepsilon e^{\beta t}\lambda\int_0^t\int_\varepsilon^{M\varepsilon}\pi_\delta(r,b)\frac{dr}{r^2}db$.
- **(c)** Dưới (B): $\mathbb{E}\|D_t\|\le 2M\lambda t e^{\beta t}\kappa_B\delta$.

### Hệ quả 10.49 ((L$_{\text{loc}}$) dạng $L^1$ cho mức ngẫu nhiên). [Đầy đủ, dưới (B)]
$$\mathbb{E}|\hat G_k^{(2)}|\le\sqrt{C_G\varepsilon}+4(1+M_G)\|G\|_\infty M\lambda t e^{\beta t}\kappa_B\delta+2\|G\|_\infty\mathbb{P}(E_\delta^c).$$

### Mệnh đề 10.52 (Quên theo thời gian cộng tốc độ lan hữu hạn). [Đầy đủ, dưới (F)]
$$\mathbb{E}|\hat G_k(t)|^2\le C_G(T)\varepsilon+\rho(T)^2\|G\|_\infty^2.$$
Nếu $\rho(T)\le e^{-T/\tau}$: $\mathbb{E}|\hat G_k(t)|^2=O(\varepsilon\ln\frac{1}{\varepsilon})$ đều theo $t$.

### 10.22. Biến chậm toàn cục

### Hệ quả 10.54 (Chỉ cần quên phần cục bộ). [Đầy đủ]
Thay (F) bằng (F'): $E[G(y,t)|\mathcal{F}_{t-T}]=A_T+B_T(y)$, $\sup_{y,y'}|\text{Cov}(B_T(y),B_T(y'))|\le\rho(T)^2\|G\|_\infty^2$. Kết luận vẫn đúng.

### 10.23. Mode là trung bình trượt mũ của các cục đắp

### Bổ đề 10.55 (Biểu diễn chính xác). [Đầy đủ]
$$\hat Q_k(X_n)=e^{-s_n}\hat Q_k(X_0)+\sum_{j=1}^n(e^{-(s_n-s_j)}-e^{-(s_n-s_{j-1})})B_k^{(j)}.$$

### Mệnh đề 10.56 (Mode quên trạng thái đầu tới sai số $\sqrt\varepsilon$). [Đầy đủ]
$\|Z_n\|\le(1-\hat m)^n\|\hat Q_k(X_0)\|+\sqrt\varepsilon\frac{(m^+-m^-)\sqrt{v^+}+2m^+\sqrt\xi}{m^++m^-}$.

### 10.24. Sóng ngắn nhớ lâu hơn

### Hệ quả 10.58 (Tách chính xác theo mode). [Đầy đủ]
$\mathbb{E}|\hat G_k(t)|^2\le C_G(T)\varepsilon+\mathbb{E}|\hat H_k^{(T)}|^2$.

**Giả thiết (F$_k$):** $\mathbb{E}|\hat H_k^{(T)}|^2\le h(T)\varepsilon$.

### Bổ đề 10.59 (Phản ứng trơn tru truyền nội dung mode tuyến tính). [Đầy đủ]
$|\hat u_k|^2\le 2\Lambda'(0)^2|\hat d_k|^2+\lambda_2^2/4$.

### Bổ đề 10.60 (Quên cho một hệ mode ghép). [Đầy đủ]
$\|E[Y_n|X_0]\|\le(1-a)^n\|Y_0\|+\sqrt\varepsilon\frac{\delta_A\sqrt{v^+}+\eta}{a}$.

### Bổ đề 10.61 (Một cung làm khối phẳng đi hay gồ ghề thêm). [Đầy đủ]
$$\Delta V=2cp\,m_S(m_S-m)+c^2p(1-p)m_S^2+(2c+c^2)p\,v_S.$$

### 10.25. Ba bước hoàn thiện

### Mệnh đề 10.62 (Trôi của độ gồ ghề và khối lượng một khối, chính xác). [Đầy đủ]
- **(a)** Gần trần thì lấp.
- **(b)** $\partial_m\mathbb{E}_X[\Delta V_B;S\subseteq B]\le 0$.
- **(c)** Gồ ghề thì nhận nhiều: tỉ lệ tâm hợp lệ $\ge((U_B/2-x_B)^+)^2/W_B$.

### Hệ quả 10.63 ((W+) theo kỳ vọng dưới (A+)). [Đầy đủ]
$\limsup_n u_n\le u^*$; $\sqrt{u^*}=O(\sqrt\varepsilon)$.

### Định lý 10.64 (Tự khởi động: (A+) đều theo thời gian). [Đầy đủ, dưới (S), (C)]
Nếu $q:=4pL_T^2 c_2<1$: $A(t)\le\max(A(T),\frac{C^*+r_0'+4pL_T^2 c_1+\lambda_2'}{1-q})$.

### Hệ quả 10.65 (Định lý trung tâm dạng "chặt chẽ theo xác suất"). [Đầy đủ]
Nếu $p_W(w)\le C_1 e^{-w/C_2}$: $\forall p>0$, $\exists\eta_0(p)>0$: $\limsup_\varepsilon\mathbb{P}(\eta_t\le\eta_0(p)/2)\le p$.

### 10.26. Cung lớn: tắt nhanh hơn mọi luỹ thừa của $\varepsilon$

### Bổ đề 10.66 (Cung lớn tắt dưới đuôi dưới dưới-Gauss). [Đầy đủ]
Số kỳ vọng cung bán kính $\ge r_b$ nhận trong cửa sổ $T$ $\le\lambda TK\frac{r_b}{\cdot}e^{-x_2^2 2r_b/(2w\varepsilon)}\to 0$ nhanh hơn mọi luỹ thừa.

### Mệnh đề 10.67 (Đếm theo lần lật: nón ánh sáng không phụ thuộc tầm). [Đầy đủ, dưới (Bloc) và (Δ)]
$\mathbb{E}\|D_t\|\le e^{\Lambda t}\mathbb{E}\|D_0\|$, $\Lambda=\lambda A(8I_1+3I_0)$, không phụ thuộc $\varepsilon$ và $R$.

### 10.27. Mô hình khối log-Gauss của vòng xoáy

### Mệnh đề 10.68 (Vòng xoáy luôn co trong mô hình; xoáy khi và chỉ khi $a<1/2$). [Đầy đủ trong mô hình]
Ma trận $A=-\alpha\binom{1\;\;z}{z+1/r\;\;1+z(z+1/r)}$:
- **(a)** mọi trị riêng có phần thực âm, $\forall z$.
- **(b)** trị riêng phức $\Leftrightarrow$ $z<0$ $\Leftrightarrow$ $a<1/2$.
- **(c)** $|\text{Im}/\text{Re}|=\sqrt{4-(2+w)^2}/(2+w)$, không tham số.
- **(d)** $A_{\mu s}>0$ khi $z<0$; $A_{s\mu}<0$ $\forall z$.

### Mệnh đề 10.69 (Tính co không cần Gauss). [Đầy đủ trong mô hình tổng quát]
- **(a)** $\det(A/\alpha)=-H(z)/g(z)>0$ $\forall$ mật độ trung bình 0.
- **(b)** $\text{tr}(A/\alpha)<0$ khi $e(z)\le G(z)/g(z)$.
- **(c)** (LC) đúng với mọi $z$ khi $g$ lõm theo log.

### 10.29. Bài A: từ động lực vi mô tới động lực khối

### Bổ đề 10.70 (Trôi chính xác của mức log và độ rộng log của một khối). [Đầy đủ]
$\Delta\mu_B=Lp$; $\Delta V_B=2Lp(\bar\varphi_{S\cap B}-\mu_B)+L^2p(1-p)$. Công thức bù trừ tường minh cho $D\mu_B^{\text{trong}}$, $DV_B^{\text{trong}}$.

### 10.30. Định lý lắp ráp: A(a) trên một cửa sổ cố định

### Bổ đề 10.71 (Nón ánh sáng dạng $L^2$). [Đầy đủ]
$|\text{Cov}(f,g)|\le 4m^2(p_A^{1/4}+p_B^{1/4})$.

### Mệnh đề 10.72 (Luật số lớn cho phiếm hàm không bị chặn). [Đầy đủ]
$\text{Var}(\hat G_k)\le 2\sigma_G^2(2M_G\varepsilon+d^*)+256m_G^2 M\varepsilon P_0^{1/4}e^{-e^{2\beta t}/4}$.

### Mệnh đề 10.73 (Lắp các cửa sổ). [Đầy đủ dưới giả thiết; phần bậc hai là giả thiết]
- **(a)** $\sup|\Gamma^{\text{GEOM}}-\gamma_j^{\bar{}}|\le 2\sup|\Gamma^P-\gamma_j^{\bar{}}|$ ngoài biến cố $O(\varepsilon^{1/2})$.
- **(b)** $\mathbb{E}|\hat G_k^{\text{GEOM}}(t)|^2\le C_n\varepsilon$.

### Mệnh đề 10.74 ((W±) trên từng quỹ đạo, trên cả cửa sổ). [Đầy đủ dưới giả thiết]
Với xác suất $\ge 1-p-o(1)$: $W_r(s)\ge\frac{1}{2}w^-\varepsilon/r$ ($r\in[\varepsilon,\Lambda_{\text{cap}}\varepsilon]$); $W_{\Lambda_{\text{cap}}\varepsilon}(s)\le\eta_{\text{cap}}$.

### Bổ đề 10.75 ((ND) từ độ nhọn). [Đầy đủ]
$U_r\ge\sqrt{W_r}/\sqrt{Q_r/W_r^2}$.

### Định lý 10.76 (A(a) trên cửa sổ cố định, chỉ dưới giả thiết hình dạng). [Đầy đủ]
Dưới 7 giả thiết (Bloc), (Δ), (Reach), (D2), (R), (N), (K∞), đuôi mũ vĩ mô:
$$\forall p>0,\;\exists\eta_0(p)>0:\;\limsup_{\varepsilon\to 0}\mathbb{P}(\eta_t\le\eta_0(p)/2)\le p.$$

### 10.31. Kiểm chặt Bước 3

### Bổ đề 10.77 ((N) từ độ sâu của cung được nhận). [Đầy đủ]
$$\frac{2c\varepsilon\theta e^{-\bar D}}{1+2c\bar\delta R}\le\bar m(X)\le\frac{4c\theta\varepsilon A}{a_\varepsilon};\quad \mu_{\max}\le 2c\bar\delta R.$$

### Bổ đề 10.78 ((K∞) và (ND) ở thang vi mô quy về mô-men tuyệt đối). [Đầy đủ]
Dưới (M∞) và $W_r\ge w^-\varepsilon/r$: (K∞) đúng; (ND) đúng với $\gamma=(w^-/(4\Lambda_{\text{cap}}\sqrt{C'_4}))^{1/2}$.

### 10.32. Phép phân đôi

### Bổ đề 10.79 (Phân đôi Paley–Zygmund). [Đầy đủ]
Ít nhất một trong hai: (i) $a_\varepsilon\ge a_0$; (ii) $x\ge U_\varepsilon/2-\sqrt{a_0 W_\varepsilon}$. Nếu thêm $W_\varepsilon\ge w_0$, $U_\varepsilon\ge\gamma\sqrt{W_\varepsilon}$, $\sqrt{a_0}<\gamma/2$: $\eta\ge\eta_{\text{low}}>0$.

### Hệ quả 10.80 (Giả thiết hoạt động chỉ cần ở nơi phòng nhỏ). [Đầy đủ]
Tại các thời điểm $\eta\le\eta_0$: (N) đúng theo Bổ đề 10.77.

### 10.33. Đuôi dưới của mật độ trên cung

### Bổ đề 10.81 (Maurer). [Đầy đủ]
$Z_i\ge 0$ độc lập, $T=\sum Z_i$: $\mathbb{P}(T\le\mathbb{E}T-u)\le\exp(-u^2/(2\sum_i\mathbb{E}Z_i^2))$.

### Mệnh đề 10.82 (Đuôi dưới dưới-Gauss của mật độ trên cung, trong $P(M,\gamma)$). [Đầy đủ, dưới (M2)]
$$\mathbb{P}(Y_S\le(1-x)\bar e)\le 2\exp\Big(-\frac{x^2(\ell/g-2)}{256C^2}\Big)+\frac{\ell}{g}p(g).$$

### Hệ quả 10.83 (Ba cách dùng). [Đầy đủ]
- **(a)** Lệch vừa: dưới-Gauss đúng tỉ lệ $x^2\ell/\varepsilon$.
- **(b)** Lệch lớn: tắt nhanh hơn mọi luỹ thừa.
- **(c)** (Rad) trong nhánh hoạt động: $EX_r\lesssim\varepsilon(1+\ln\frac{1}{x^2})/a_0$.

### 10.34. Hai loại hõm

### Nhận xét 10.84 (Hõm bị che). Hõm hẹp hơn $\varepsilon$ hoặc rộng đúng $\varepsilon$ kẹp giữa hai gai cao có thể không bao giờ nằm trong cung hợp lệ. Độ sâu tương đối tăng mãi.

### Bổ đề 10.85 (Vùng sâu đủ rộng thì lấp được). [Đầy đủ]
- **(a)** Trung bình $\rho_{S'}$ theo vị trí $\le 2\rho_S$.
- **(b)** Ít nhất một nửa số vị trí có $\rho_{S'}\le 4\rho_S$.
- Cường độ cung hợp lệ bên trong $\ge\lambda\ell/(4\varepsilon)$ khi $\ell\ge 4\varepsilon$.

### 10.35. Gai tự xẹp

### Bổ đề 10.86 (Cập nhật chính xác của một hộp). [Đầy đủ]
$\rho'_y=(\rho_y+c\tilde h_y)/(1+cq)$.
- **(i)** $0\le\tilde h_y\le\min(\rho_y,q/w)$; **(ii)** $\int\tilde h_y\,dy=q$; **(iii)** $\int\tilde h_y G(\rho_y)dy=\int_S M_G(z)d\hat Q(z)$.

### Bổ đề 10.87 (Mô-men của mật độ vi mô là chuẩn $L^m$). [Đầy đủ]
- **(a)** $\mathbb{E}\rho_\varepsilon(0)^m=\mathbb{E}\Psi_m(X_t)$.
- **(b)** $\Psi_1\equiv 1$.
- **(c)** $\Psi_2=1+W_{w/2}$.

### Định lý 10.88 ((M∞) dưới (HSm) và (Radm)). [Đầy đủ]
$$\mathbb{E}\rho_\varepsilon(0)^m\le 1+C_m\mathbb{E}\mathcal{M}_t;\quad \mathbb{E}\mathcal{M}_t\le\frac{1+c}{c}\mathbb{E}s_t.$$
Nếu (HSm) theo từng cung: $\sup_t\Psi_m(X_t)\le\max(1,2C_m/a_m)+C_m$ đều theo thời gian.

### Bổ đề 10.89 (Hõm rộng hơn $\varepsilon$ một chút thì lấp được từ bên trong). [Đầy đủ]
Cường độ cung hợp lệ bên trong $H$ dài $(1+x)\varepsilon$, $u\ge\ln 4$: $\ge\lambda x^2/4$. Không phụ thuộc mật độ hai bên.

### Bổ đề 10.90 (Bỏ được (Radm)). [Đầy đủ]
- **(a)** Chỉ dưới (HSm): $\mathbb{E}\Psi_m(X_t)\le 1+\tilde C_m\mathbb{E}\mathcal{M}_t$.
- **(b)** (HSm) từng cung: $\sup_t\Psi_m\le(1+c)^m\max(1,(\tilde\beta_m/a_m)^m)$.

### 10.37. Lộ trình sáu mắt xích

### Bổ đề 10.91 (Răng cưa). [Đầy đủ]
$\int_0^T\mathbf{1}_{\{|X_S(t)|\le\delta\}}dt\le\frac{2\delta}{\dot\gamma}(1+N_S(T))$.

### 10.38–10.39. Gói kiểm thử 4, 5

### Bổ đề 10.92 (Độ sâu không vượt tuổi đầy). [Đầy đủ]
$dep_S(t)\le A_S^*$. Đẳng thức: $dep_S(t)=A_S^*-z_S(\tau_S)-\sum_{\text{chạm}}\ln(1+c\hat Q(S'\cap S)/\hat Q(S))$.

### 10.40. Viết chặt

### Bổ đề 10.93 (Răng cưa, dạng tổng quát). [Đầy đủ]
$\int_I\mathbf{1}_{\{X_S(s)\in[a,a+\delta]\}}ds\le\frac{\delta}{\dot\gamma}(1+N_S(I))\mathbf{1}_{\{\sup X_S\ge a\}}$.

### Bổ đề 10.94 (Tập khuyết tật tích luỹ). [Đầy đủ]
$\tilde D_t=D_0\cup\bigcup\{S:S\text{ bị lật}\}$: (1) $D_t\subseteq\tilde D_t$, $\tilde D$ không giảm; (2) mỗi thành phần dài $\ge\varepsilon$; (3) lật chỉ khi $S\cap D_{s^-}\ne\emptyset$ và $X_S^{(1)},X_S^{(2)}$ khác dấu.

### Mệnh đề 10.95 (Đếm lần lật trên cửa sổ ngắn). [Đầy đủ, dưới (Δ) và (FARM)]
Nếu $\Theta<1$: $\mathbb{E}\|\tilde D_{t+\tau}\|\le\mathbb{E}\|\tilde D_t\|/(1-\Theta)$. Nếu $\Theta\le 1/2$: $\mathbb{E}\|\tilde D_T\|\le 2^{\lceil T/\tau\rceil}\mathbb{E}\|D_0\|$.

### Mệnh đề 10.96 (Gieo kiểu Poisson và (D2)). [Đầy đủ]
- **(a)** Phần gieo có kỳ vọng $\le\frac{2\lambda\sigma_M}{\dot\gamma}\delta_{lv}$.
- **(b)** $\mathbb{E}\|\tilde D_{t+\tau}\|^2\le\frac{\mathbb{E}\|\tilde D_t\|^2+C\varepsilon\mathbb{E}\|\tilde D_{t+\tau}\|+C\mathbb{E}\|\tilde D_{t+\tau}\|\delta_{lv}+C\delta_{lv}^2}{1-2\Theta}$.

### Bổ đề 10.97 ((Δ) quy về tỉ số khối lượng). [Đầy đủ]
$|X_S^{(1)}-X_S^{(2)}|\le\ln(1+\max_i Q^{(i)}(S\cap D)/Q(S\setminus D))$. Dưới (MR): (Δ) đúng với $A=2\Lambda_D$.

### Mệnh đề 10.98 (Đuôi mũ của từng mode Fourier). [Đầy đủ, dưới (ACk), (μ̄)]
$\mathbb{E}e^{s\|Z_n\|^2}\le 1+\frac{a\kappa v_1 e^{\kappa v_1}}{\cdot}\mathbb{E}[\sum_j\mu_j]$; $\mathbb{P}(|\hat Q_k(t)|^2>x)\le(1+C\mathbb{E}s_t)e^{-\kappa x/\varepsilon}$.

### Định lý 10.99 (Định lý lắp ráp, danh sách giả thiết mới). [Đầy đủ]
Kết luận 10.76 đúng với danh sách: (FARM), $\sigma_M<\infty$, luật số lớn cho số cú chạm; (MR) dạng mô-men; (HSm); $\mathbb{E}_{\text{nhận}}A^*<\infty$; (ACk), (μ̄).

### 10.41. Bốn chỗ kỹ thuật

### Mệnh đề 10.100 (Bỏ (Δ) từng quỹ đạo). [Đầy đủ, chỉ dưới (FARM*)]
$\Theta=2\lambda\tau(\ln(2M)+2M)+\frac{4\lambda}{\dot\gamma}\varphi_M^*$.

### Mệnh đề 10.101 ((Reach) dạng mũ). [Đầy đủ, dưới (FARM*$_{M,\theta}$)]
$$\mathbb{P}(D_T\cap A\ne\emptyset)\le 2^{\lceil T/\tau\rceil}\frac{\|D_0\|}{\varepsilon}e^\theta\exp\Big(-\theta\frac{d-\ell_A/2}{\varepsilon}\Big).$$

### Mệnh đề 10.102 (Từ mode tới $W$ vĩ mô, cực đại trên cửa sổ). [Đầy đủ]
$$\mathbb{P}\Big(\sup_{t\le t_2}W_{r_1}(t)\ge x\Big)\le(1+G)\exp\Big(-\frac{\kappa x}{4\varepsilon C_{\text{tot}}}\Big).$$

### Bổ đề 10.103 (GEOM là mô hình mức với mức ngẫu nhiên $L\Gamma$). [Đầy đủ]
- **(a)** GEOM nhận $S$ khi $\ln(Q(S)/\|S\|)\le g_t$, $g_t=g_0+L\Gamma_t$.
- **(b)** $|\Gamma_t^G-\Gamma_t^P|\le FL_t$.

### 10.42. Vòng tự hợp ở Bước 3

### Bổ đề 10.104 (Mức của GEOM bị ghim vào trường). [Đầy đủ]
$g_t=\ln\bar\delta+\int_{\mathbb{T}}\varphi_t\,dy$. Mỗi cung nhận làm $\int\varphi$ tăng đúng $L\|S\|$.

### 10.44. Soát phần (b) của 10.73; khai triển lai

### Mệnh đề 10.106 (10.73(b), viết lại). [Đầy đủ, dưới giả thiết]
$$\mathbb{E}|\hat G_k^{\text{GEOM}}(t)|^2\le C n^2(1+\rho_G/\varepsilon)^2\varepsilon.$$

### 10.45. Thử chứng minh lối (1b)

### Bổ đề 10.108 (Đếm thành phần). [Đầy đủ]
- **(i)** $C_t$ không tăng.
- **(ii)** Phần tăng do cung nhỏ $\le 8\lambda M\varepsilon C_t$.
- **(iii)** Nếu $\frac{4\lambda}{\dot\gamma}\varphi^*_{[0,T]}\le\frac{1}{2}$: $\mathbb{E}\|\tilde D_T\|\le 2\|D_0\|(1+8\lambda MT)$.

### Bổ đề 10.109 (Phòng âm không ở lâu). [Đầy đủ, dưới (W+) vĩ mô]
$$\mathbb{E}|\{t\le T:\eta_t\le-x''\}|\le\frac{\delta_{\max}e^{-x''}+T(C_{\text{neg}}+C_Q)}{2\lambda[\kappa\ln\frac{R}{M\varepsilon}-L\ln(2M)-(\kappa+L)\frac{w}{Mx'^2}]-C_Q}=O\Big(\frac{1}{\ln(1/\varepsilon)}\Big).$$

### 10.46. Đồng nhất thức trôi theo tầng

### Bổ đề 10.110 (Đồng nhất thức trôi theo tầng). [Đầy đủ]
$$D=2\lambda\int_{\varepsilon/2}^R\frac{dr}{r}\Phi_r,\quad \Phi_r=a_r(cE_r-L)+e_r,\quad |e_r|\le c^2\bar\delta^2 r.$$

### Hệ quả 10.110' ("Có hại", phát biểu chính xác).
$\Phi_r\ge a_r(c-L)-c\sqrt{W_ra_r}-c^2\bar\delta^2 r$. Tầng $r$ chắc chắn đẩy lên khi $a_r>c^2W_r/(c-L)^2$.

### Bổ đề 10.111 (Chặn tiên nghiệm cho độ gồ ghề). [Đầy đủ, không giả thiết]
$\int\psi(\rho_r)dy\le F\le\ln(c\bar\delta/L)$; $\int\psi(\rho_r)dy\le\ln\bar\delta+\eta$.

### 10.47. Phá vòng hằng số

### Mệnh đề 10.112 (Trôi theo độ sâu). [Đầy đủ]
$\Phi_r\ge a_r(c\theta e^{-D_r}-L)-c^2\bar\delta^2 r/a_r$.

### Định lý 10.113 (Dải tới hạn, không cần (W+)). [Đầy đủ]
Dưới (ND), (W−), (Sâu$_{u_1}$):
$$D\ge 2\lambda\Big[\frac{\gamma^2\varphi_D}{8}\ln^+\frac{r_b}{u_1\varepsilon}-L\ln(2u_1)-c^2\bar\delta^2 R\Big].$$
$x_c^2=\frac{\gamma^2 w^-}{16u_1}\exp(-\frac{8(L\ln(2u_1)+c^2\bar\delta^2 R+\kappa)}{\gamma^2\varphi_D})$, không phụ thuộc $w^+$.

### Hệ quả 10.114 (Thời gian ở dải tới hạn; vòng hằng số bị phá). [Đầy đủ]
$$\mathbb{E}|\{t\le T:\eta_t\le\eta_c\}|\le\frac{\bar\delta e^{\eta_c}+T(C_{\text{neg}}+C_Q)}{2\lambda\kappa-C_Q}.$$

### 10.48. Định lý trung tâm quy về bốn bài toán

### Bổ đề 10.115 (Răng cưa tinh). [Đầy đủ]
$|\{s\in I:X(s)\in[a,a+\delta]\}|\le\frac{\delta+G}{\dot\gamma}$.

### Định lý 10.116 (Định lý trung tâm dưới bốn bài toán). [Đầy đủ, dưới (B1)–(B4)]
$\forall p>0$, $\exists\eta^*>0$: $\limsup_\varepsilon\mathbb{P}(\eta_t\le\eta^*)\le p$.

### 10.49. (B4) chỉ cần ở dạng kỳ vọng

### Bổ đề 10.117 (Bước nhảy độ sâu bị chặn). [Đầy đủ]
$\Delta u\in[-L,L/2]$.

### Bổ đề 10.118 (Đồng nhất thức $\Psi_m$). [Đầy đủ]
$\int M_{m-1}d\hat Q=\Psi_m$.

### Bổ đề 10.119 (Tiêu chí tầng không cần độ sâu). [Đầy đủ]
$\psi(E_r)\le F(r)/a_r$. Nếu $F(r)<a_r\psi(L/c)$: $cE_r>L$.

### Bổ đề 10.120 (Cantelli, đối ngẫu). [Đầy đủ]
Nếu $a_r\ge\alpha$: $W_r\ge\frac{\alpha}{1-\alpha}x^2$.

### Mệnh đề 10.121 (Trôi với $a_r\ge\alpha$ trực tiếp). [Đầy đủ]
$$\frac{D}{2\lambda}\ge\alpha\varphi\ln\frac{r_b}{u_1\varepsilon}-[\alpha(\varphi+L)C_{\text{xấu}}+L\ln(2u_1)]-c^2\theta^2\int a_r\,dr.$$

### Bổ đề 10.122 (Đồng nhất thức hồi phục, V6). [Đầy đủ]
$\mathbb{E}_X[q(W_r+\sigma)]=\mathbb{E}_X[q]\cdot C(r)W_r$.

### Mệnh đề 10.123 (Cập nhật chính xác của $W_r$ và chặn kỳ vọng). [Đầy đủ]
- **(a)** $\Delta W_r=\frac{-2cq(W_r+\sigma)+c^2(\int\tilde h^2-q^2(1+W_r))}{(1+cq)^2}$.
- **(b)** Dưới (C$^+$$_{tp}$) và (Cỡ): $\mathbb{E}W_r(s)\le\mathbb{E}W_r(t_1)+\frac{C_c\nu\varepsilon}{r}\mathbb{E}[\mathcal{M}_s-\mathcal{M}_{t_1}]$.

### Định lý 10.124 ((B4) chỉ cần theo kỳ vọng). [Đầy đủ]
Dưới (B4$^E$): $\mathbb{P}(\eta_t\le\eta^*)\to 0$. Mạnh hơn 10.116.

### 10.50. Cấu trúc phân tích cho O1–O3

### Bổ đề 10.125 (Dạng hộp của hiệp phương sai). [Đầy đủ]
$C_{\ell,\ell'}=-\frac{\text{Cov}_\pi(\rho_\ell,\bar\Xi)}{\mathbb{E}_\pi[\rho_\ell-1]\mathbb{E}_\pi[\bar\Xi]}$. $C\ge 0$ $\Leftrightarrow$ hộp càng đặc càng ít bị cung hợp lệ phủ.

### 10.51. Bỏ hẳn (Sâu)

### Định lý 10.130 (Trôi trong dải tới hạn, không cần độ sâu). [Đầy đủ]
Dưới (F1), (F2), (ND), (W−) trên $[\Lambda_1\varepsilon,R]$:
$$D\ge 2\lambda\Big[\frac{\gamma^2\varphi}{8}\ln^+\frac{r_b}{\Lambda_1\varepsilon}-L\ln(2\Lambda_1)-\frac{LC_F}{\psi(e^\varphi)}-c^2\bar\delta^2 R\Big].$$
$x_c$ không phụ thuộc $\varepsilon$, $w^+$ hay độ sâu.

### 10.52. Tình trạng của Định lý 10.130

### Bổ đề 10.132 (Chặn $F(r)$ không cần $\min\rho$). [Đầy đủ]
$F(r)\le 2W_r+2\sqrt{W_r}\|\ln\rho_r\|_{L^2}$.

### 10.53. Trộn trong GEOM

### Hệ quả 10.133 (Tự khởi động không cần cấu trúc (S)). [Đầy đủ, dưới (QT), (VT)]
$A(t)\le\max(A(T),\frac{c_0+C^*}{1-q})$.

### 10.54. Cung vĩ mô phá (VT) đúng ở cửa sổ $\sqrt\varepsilon$ quanh $\eta=0$

### Bổ đề 10.135 (Rào chắn theo dải). [Đầy đủ]
$\beta=\min(\kappa/\sigma^2,1/j)$: $\mathbb{P}(\exists t:\eta_t<\eta_a|\eta_{t_1}\ge\eta_b)\le\mathbb{E}[N_\downarrow]e^{-\beta(\eta_b-\eta_a-j)}$.

### Hệ quả 10.136 (Dạng rào chắn của A(a)). [Đầy đủ]
$\mathbb{P}(\exists t\in[t_1,t_2]:\eta_t<\eta_a)\to 0$.

### 10.57. Bước 1: (VT) qua bất đẳng thức Poincaré

### Bổ đề 10.138 (Poincaré có điều kiện). [Đầy đủ]
$\text{Var}(F|\mathcal{F}_{t-T})\le\mathbb{E}[\int|D_w F|^2\mu(dw)|\mathcal{F}_{t-T}]$.

### Bổ đề 10.139 (Chỉ ứng viên được nhận mới có ảnh hưởng). [Đầy đủ]
$D_w F=\mathbf{1}_{\{w\text{ hợp lệ tại }X_{b^-}\}}\cdot\Delta_w F$.

### Mệnh đề 10.140 ((VT) dưới hai giả thiết). [Đầy đủ, dưới (DL), (M4)]
$$\mathbb{E}|\hat G_k(t)-\hat H_k^{(T)}(t)|^2\le 4\lambda T D_T\|G\|_\infty^2(1+M_G)^2\Big(\Lambda+\frac{M_4}{\Lambda x_a^4}\Big)\varepsilon.$$
Chọn $\Lambda=\max(1/2,\sqrt{M_4}/x_a^2)$: $C^*=\frac{8\lambda T D_T\|G\|_\infty^2(1+M_G)^2\sqrt{M_4}}{x_a^2}$.

### 10.58. Bước 1 (tiếp): chứng minh (DL)

### Bổ đề 10.141 (GEOM là mô hình mức với mức bằng trung bình). [Đầy đủ]
$X_S=\ln(\frac{1}{\|S\|}\int_S e^\varphi)-\Gamma-\ln\bar\delta$; $X_S=\ln(\rho_S/\theta)$.

### Bổ đề 10.142 (Cấu trúc của sai khác sau một cú ép nhận). [Đầy đủ]
- **(a)** $\varphi'-\varphi=L\sum_j\sigma_j\mathbf{1}_{S_j}$; $\Gamma'-\Gamma=\gamma_d$, $|\gamma_d|\le LZ$.
- **(b)** Nếu $S'\cap U=\emptyset$: $X'_{S'}-X_{S'}=-\gamma_d$; ngược lại $|X'_{S'}-X_{S'}+\gamma_d|\le Ln_{S'}$.
- **(c)** Lật chỉ khi $S'\cap U\ne\emptyset$ và hợp lệ ở ít nhất một hệ; hoặc $|\gamma_d|$ nhỏ.
- **(d)** $\|\Delta_w\hat G_k\|\le 2C_g LZ_t$.

### Mệnh đề 10.143 (Mô-men của khối lượng sai khác). [Đầy đủ, dưới (LV), (B')]
$\mathbb{E}[Z_t|\mathcal{F}_b]\le(\|S_w\|+\ell_G)e^{\gamma_1 T}$; $\mathbb{E}[Z_t^2|\mathcal{F}_b]\le e^{2\gamma_1 T}(1+\gamma_2 T/\ell_G)(\|S_w\|+\ell_G)^2$. $\gamma_1$, $\gamma_2/\ell_G$ không phụ thuộc $\varepsilon$.

### Định lý 10.144 ((VT) cho phiếm hàm Lipschitz). [Đầy đủ, dưới (LV), (B')]
$\mathbb{E}|\hat G_k(t)-\hat H_k^{(T)}(t)|^2\le C^*\varepsilon$.

### Hệ quả 10.145 ((L$_{\text{loc}}$) đều theo thời gian). [Đầy đủ, dưới (QT), (LV), (B')]
$\sup_t\mathbb{E}|\hat G_k(t)|^2\le\max(A(t_1+T)\varepsilon,\frac{c_0+C^*}{1-q}\varepsilon)$.

### 10.59. (C0): bất đẳng thức tất định ở thang trung và thang thô

### Định lý 10.146 (Cung hợp lệ dài thấy mật độ trơn thấp). [Đầy đủ, tất định]
$\theta\le 1$, $\ell'\ge 2\ell$: $S_{\ell'}\le(-x+2\ell/\ell')\mu_{\ell'}+\ell' W_\ell+2\ell(1+W_\ell)$.

### Hệ quả 10.147 (C0 ở thang trung). [Đầy đủ, dưới (NS)]
$C_\ell\ge 1-\eta_s$ nếu $\frac{x}{2}\sum_G\omega\mu\ge\sum_\mathcal{B}\omega(\ell'W_\ell+5\ell)$.

### Định lý 10.148 (Thang thô: phân tích cân bằng cục bộ). [Đầy đủ]
$-\text{Cov}_\pi(\rho_\ell,\bar\Xi)\ge\frac{\theta\varphi_I}{2(1+\delta)^2}\mathbb{E}_\pi[(\rho-\rho')^2;\rho,\rho'\in I]-|\text{Cov}_\pi(\rho_\ell,\bar\Xi-\Xi_{LE})|$.

### 10.60. Soát từ phiên độc lập

### Bổ lệ (chặn $L^2$). [Đầy đủ]
$\int(\ln\rho_r)_-^2\le\text{Var}(u)+F^2=:L^2$. Kiểm số: tỉ số $\le 0{,}74$.

### 10.61. Gói 16

### Định lý 10.167 (Tập trung của mức). [Đầy đủ]
$\mathbb{E}[\delta(t)^2|\mathcal{F}_{t_0}]\le\lambda T L^2 e^{2\gamma_1 T}C_D\varepsilon$; $\mathbb{E}[\delta(t)^4|\mathcal{F}_{t_0}]\le C(T)\varepsilon^2$.

### Định lý 10.168 (Mô-men của khuyết tật khi ghép với $P(\gamma)$). [Đầy đủ]
$\mathbb{E}[Z_t^P]\le C_1\sqrt\varepsilon$; $\mathbb{E}[(Z_t^P)^2]\le C_2\varepsilon$; $\mathbb{E}[(Z_t^P)^4]\le C_4\varepsilon^2$.

### Định lý 10.169 ((MIX) bậc bốn quy về giả thiết tĩnh). [Đầy đủ]
$\mathbb{E}|\hat G_k(t)-\hat H_k^{(T)}(t)|^4\le C\varepsilon^2$; cùng (QT) bậc bốn: $\sup_t\mathbb{E}|\hat G_k|^4\le C\varepsilon^2$.

### 10.64. Khối 3: độ sâu của hõm

### Bổ đề 10.170 (Độ sâu trung bình bị chặn đều). [Đầy đủ]
$\int u_+^2\le 2e^{B^*}$; $m^-=\int u^+\le\sqrt{2e^{B^*}}$.

### Bổ đề 10.171 (Tuổi của một điểm). [Đầy đủ]
$u^-(y;t)\le A(y):=\Gamma_t-\Gamma_{\sigma(y)-}$; $I\le\int A^2$.

### Mệnh đề 10.172 (Trôi của $I$). [Đầy đủ]
$\frac{d}{dt}\mathbb{E}I\le\mathbb{E}[-2\lambda L\text{Cov}(u^-,\Xi)+2\lambda L^2 A]$. Theo đồng hồ $\Gamma$: $dI/d\Gamma\le-2C_{\log}I+L$.

### Hệ quả 10.173. [Đầy đủ]
Nếu $C_{\log}\ge\kappa$: $I(\Gamma)\le e^{-2\kappa\Gamma}I(0)+L/(2\kappa)$.

### Hệ quả 10.175 (Chặn $L^2$). [Đầy đủ]
$L^2\le 2e^{B^*}+B^{*2}+I$.

### 10.66. Đồng nhất thức chính xác cho bề rộng

### Mệnh đề 10.176 (Cân bằng bề rộng, dạng đẳng thức). [Đầy đủ]
$\frac{dV}{d\Gamma}=-2C_u V+L(1-2D/A)$, $C_u=-\text{Cov}(u,\Xi)/(2AV)$.

### 10.67. Kiểm định phiên 22/11

### Mệnh đề 10.178 (Đẳng thức hồi phục theo tầng). [Đầy đủ]
$$\frac{dV_r}{d\Gamma}=-2C_{u,r}V_r+\nu_r,$$
$C_{u,r}=-\int M_r\Xi/(2AV_r)$; $\nu_r\ge 0$ (công thức tường minh theo hai nhánh $r'<r$ và $r'\ge r$). Dạng phổ: $\nu_r=\frac{2L}{A}\sum_{k\ne 0}|m_k(r)|^2 D_k$.

### Bổ đề 10.180 (Đơn điệu theo tầng: chỉ đúng cho bội nguyên). [Đầy đủ]
Với $n$ nguyên, $2nr\le 1$, $f$ lồi: $\int f(\bar u_{nr})\le\int f(\bar u_r)$.

### Bổ đề 10.181. [Đầy đủ]
$\int e^{\bar u_r}\le e^F$; $V_r\le 2e^{B^*}+I_r$.

### Bổ đề 10.187 (Đổi đồng hồ bộ bù). [Đầy đủ]
Nếu $b_X\le(-2\kappa X+\nu)\dot H$: $e^{2\kappa H_t}(X_t-\nu/(2\kappa))$ là siêu martingale. $\Gamma-H$ là martingale, $\mathbb{E}(\Gamma_t-H_t)^2\le 4\lambda L^2 Rt$.

### Mệnh đề 10.184 (Rice + lượng tử hoá). [Đầy đủ]
Tại điểm cắt ngưỡng: $n_r\le\nu_r\le\frac{1+c}{c}n_r$. (B+) và (B−) là hai phía của cùng một đại lượng.

### Mệnh đề 10.214 (Ràng buộc cứng). [Đầy đủ]
Mọi cung được nhận: $\frac{1}{\|S\|}\int_S N\le\int N+b/L$.

### Bổ đề 10.190 (Đệ quy nhị phân). [Đầy đủ]
$W_{2r}=\frac{1}{2}(W_r+c_r)$; $Q_{2r}=\frac{1}{8}Q_r+\frac{1}{4}(T_r+T'_r)+\frac{3}{8}V_r$.

### Bổ đề 10.196 (Sửa). [Đầy đủ]
$\kappa_4(2r)\le\frac{1/2+\zeta_T}{(1+\theta_r)^2}\kappa_4(r)+\frac{3/2(1+\zeta_V)}{(1+\theta_r)^2}$. Điều kiện co: $\zeta_T<1/2$ khi $\theta\ge 0$.

### Mệnh đề 10.212 (Đồng nhất thức theo mode của trường log). [Đầy đủ]
$\frac{d}{dt}\mathbb{E}|\hat u_k|^2=2\lambda L\mathbb{E}\text{Re}(\bar{\hat u}_k\hat\Xi_k)+4\lambda L^2\mathbb{E}D_k$. Cộng theo $k\ne 0$: ra đúng 10.176.

### Định lý 10.213. [Đầy đủ]
$\mathbb{E}|\hat u_k(t)|^2\le 2(\lambda Lt)\int_0^t\mathbb{E}|\hat\Xi_k|^2 ds+8\lambda L^2\int_0^t\mathbb{E}D\,ds$.

### Mệnh đề 10.211 (Điều kiện đủ cho (AC+)). [Đầy đủ]
Nếu $\text{Var}(\tilde h)\le v_{\max}$: $|\hat Q_k\bar{\tilde\Psi}_k|\le v_k+\frac{1}{2}\text{Var}(\tilde h)$.

---

## CÁC GIẢ THUYẾT CHÍNH (tổng hợp)

| # | Giả thuyết | Nội dung tóm tắt |
|---|-----------|-----------------|
| A | Đóng băng và làm phẳng không điều kiện | Mục 8 |
| B | Chuyển pha của mô hình khoá phòng | Mục 9.1 |
| D / D' | Hấp thụ theo luật / tương quan tắt dần | Mục 9.7, 10.9, 10.16 |
| E, E', E'' | Hạ gai / hạ gai tuyến tính / hạ đồi theo thang | Mục 9.10 |
| (H), (H⁻) | Phòng dương / âm có điều kiện | Mục 7 |
| (P), (OU) | Phòng và giả thiết kiểu OU | Mục 6.3 |
| (W±, ND) | Độ gồ ghề đúng cỡ $\sqrt{\varepsilon/r}$, không suy biến | Mục 10.17 |
| (LRk), (Nk), (A+) | Phản ứng tuyến tính theo mode / khối lượng cục đắp / tập hợp lệ phẳng | Mục 10.18–19 |
| (L$_{\text{loc}}$) | Luật số lớn cho phiếm hàm cục bộ | Mục 10.19–20 |
| (F), (F'), (F$_k$) | Quên theo thời gian / phần cục bộ / theo mode | Mục 10.20–24 |
| (S), (C) | Cấu trúc trí nhớ / chặn trường thô | Mục 10.25 |
| (HSm), (Radm) | Cung không rơi cạnh gai / cung không mang khối lượng quá lớn | Mục 10.35 |
| (Vρ) | $\mathbb{E}[W_r|\mathcal{E}]\le\sigma^2\varepsilon/r$ | Mục 10.16 |
| (B±), (Bloc), (B') | Mật độ quanh ngưỡng / cục bộ / chặn trên | Mục 10.20, 10.40, 10.58 |
| (LV), (LV-Palm) | Đuôi dưới quanh tập sai khác | Mục 10.58, 10.60 |
| (QT), (VT) | Phần nhớ co / phần mới sinh $O(\varepsilon)$ | Mục 10.53, 10.57 |
| (C0), (C+) | Hệ số hồi phục dương / $C\ge C_0>0$ | Mục 10.43, 10.52 |
| (D4) | Khử tương quan bậc bốn giữa hai nửa kề nhau | Mục 10.67 |
| (MIX) | Trộn: $\int\|\text{Cov}(G(0),G(z))\|dz\le C\varepsilon$ | Mục 10.60 |
| (AC), (LE), (NS) | Chống tập trung tại ngưỡng / cân bằng cục bộ / cung ngắn không chọn ngược | Mục 10.59 |

---

> **Ghi chú.** Bản tổng hợp này bao gồm toàn bộ các phát biểu được đánh số (Bổ đề, Định lý, Mệnh đề, Hệ quả, Nhận xét có nội dung định lý) và các định nghĩa/giả thuyết chính từ bản thảo ~200 trang. Phần chứng minh chi tiết, điểm cần kiểm, số liệu mô phỏng và các nhận xét heuristic được lược bỏ để giữ trong một lượt. Các nhãn trạng thái ([Đầy đủ], [Dựa trích dẫn], [Heuristic], [Hướng]) được giữ nguyên.