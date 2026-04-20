# revisi MK II


---

## Bagian A: Menghitung Determinan dengan Ekspansi Baris
**Rumus:** $\det(A) = \sum_{k=1}^{n} (-1)^{i+k} a_{ik} M_{ik}$

### 1. Matriks $A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}$
Ekspansi baris pertama ($i=1$):
* $a_{11} = -7, M_{11} = |4| = 4$
* $a_{12} = -5, M_{12} = |1| = 1$

**Perhitungan:**
$\det(A) = (-7)(-1)^{1+1}(4) + (-5)(-1)^{1+2}(1)$
$\det(A) = (-7)(1)(4) + (-5)(-1)(1)$
$\det(A) = -28 + 5 = \mathbf{-23}$

---

### 2. Matriks $A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}$
Ekspansi baris ketiga ($i=3$) karena memiliki angka nol terbanyak:
* $a_{31} = 0, a_{32} = 0$
* $a_{33} = 1, M_{33} = \begin{vmatrix} 0 & 2 \\ 1 & -2 \end{vmatrix} = (0 \cdot -2) - (2 \cdot 1) = -2$

**Perhitungan:**
$\det(A) = 0 + 0 + (1)(-1)^{3+3}(-2)$
$\det(A) = 1 \cdot 1 \cdot (-2) = \mathbf{-2}$

---

### 3. Matriks $A = \begin{bmatrix} 1 & -3 & 1 & 1 \\ -3 & 1 & 1 & 1 \\ 1 & 1 & -3 & 1 \\ 1 & 1 & 1 & -3 \end{bmatrix}$
Jika kita menjumlahkan semua baris ke baris pertama, kita akan mendapatkan baris nol (karena $1-3+1+1=0$). Maka secara teoretis determinannya adalah **0**.
Secara manual dengan ekspansi baris pertama:
* $M_{11} = 16, M_{12} = -16, M_{13} = 16, M_{14} = -16$ (berdasarkan perhitungan submatriks 3x3)

**Perhitungan:**
$\det(A) = 1(-1)^{1+1}(16) + (-3)(-1)^{1+2}(-16) + 1(-1)^{1+3}(16) + 1(-1)^{1+4}(-16)$
$\det(A) = 16 - 48 + 16 + 16 = \mathbf{0}$

---

## Bagian B: Menghitung Invers dengan Matriks Adjoin
**Rumus:** $A^{-1} = \frac{1}{\det A} \text{adj } A$ di mana $(\text{adj } A)_{ij} = (-1)^{i+j} M_{ji}$

### 4. Matriks $A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}$
$\det(A) = -23$
* $(\text{adj } A)_{11} = (-1)^{1+1}M_{11} = 4$
* $(\text{adj } A)_{12} = (-1)^{1+2}M_{21} = -(-5) = 5$
* $(\text{adj } A)_{21} = (-1)^{2+1}M_{12} = -(1) = -1$
* $(\text{adj } A)_{22} = (-1)^{2+2}M_{22} = -7$

**Hasil:**
$A^{-1} = \frac{1}{-23} \begin{bmatrix} 4 & 5 \\ -1 & -7 \end{bmatrix} = \mathbf{\begin{bmatrix} -4/23 & -5/23 \\ 1/23 & 7/23 \end{bmatrix}}$

---

### 5. Matriks $A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}$
$\det(A) = -2$
Elemen Adjoin $(\text{adj } A)_{ij}$ (transpos dari tanda minor):
* Baris 1: $M_{11}=-2, -M_{21}=-2, M_{31}=-8$
* Baris 2: $-M_{12}=-1, M_{22}=0, -M_{32}=-3$
* Baris 3: $M_{13}=0, -M_{23}=0, M_{33}=-2$

**Hasil:**
$A^{-1} = \frac{1}{-2} \begin{bmatrix} -2 & -2 & -8 \\ -1 & 0 & -3 \\ 0 & 0 & -2 \end{bmatrix} = \mathbf{\begin{bmatrix} 1 & 1 & 4 \\ 0.5 & 0 & 1.5 \\ 0 & 0 & 1 \end{bmatrix}}$

---

### 6. Matriks $A = \begin{bmatrix} 1 & -3 & 1 & 1 \\ -3 & 1 & 1 & 1 \\ 1 & 1 & -3 & 1 \\ 1 & 1 & 1 & -3 \end{bmatrix}$
Karena nilai determinan $\det(A) = 0$ (seperti dihitung pada nomor 3), maka matriks ini **tidak memiliki invers** (Matriks Singular). Pembagian dengan nol tidak terdefinisi dalam operasi matriks.