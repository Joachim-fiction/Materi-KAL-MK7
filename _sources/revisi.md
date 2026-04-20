# revisi

## Bagian A: Menghitung Determinan dengan Ekspansi Baris

**Rumus Umum:** $$\det(A) = \sum_{k=1}^{n} (-1)^{i+k} a_{ik} M_{ik}$$

### 1. Matriks 2x2
$A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}$

**Proses:**
Menggunakan ekspansi baris pertama ($i=1$):
* $a_{11} = -7, M_{11} = |4| = 4$
* $a_{12} = -5, M_{12} = |1| = 1$

**Perhitungan:**
$$\det(A) = (-7)(-1)^{1+1}(4) + (-5)(-1)^{1+2}(1)$$
$$\det(A) = (-7)(1)(4) + (-5)(-1)(1)$$
$$\det(A) = -28 + 5 = \mathbf{-23}$$

---

### 2. Matriks 3x3
$A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}$

**Proses:**
Memilih ekspansi pada **baris ketiga** ($i=3$) karena memiliki elemen nol terbanyak:
* $a_{31} = 0, a_{32} = 0$
* $a_{33} = 1, M_{33} = \begin{vmatrix} 0 & 2 \\ 1 & -2 \end{vmatrix} = (0 \cdot -2) - (2 \cdot 1) = -2$

**Perhitungan:**
$$\det(A) = 0 + 0 + (1)(-1)^{3+3}(-2)$$
$$\det(A) = 1 \cdot 1 \cdot (-2) = \mathbf{-2}$$

---

### 3. Matriks 4x4
$A = \begin{bmatrix} 1 & -3 & 1 & 1 \\ -3 & 1 & 1 & 1 \\ 1 & 1 & -3 & 1 \\ 1 & 1 & 1 & -3 \end{bmatrix}$

**Proses:**
Menggunakan ekspansi baris pertama. Kita hitung kofaktor $C_{1k} = (-1)^{1+k}M_{1k}$:
* $C_{11} = 1 \cdot \begin{vmatrix} 1 & 1 & 1 \\ 1 & -3 & 1 \\ 1 & 1 & -3 \end{vmatrix} = 16$
* $C_{12} = -1 \cdot \begin{vmatrix} -3 & 1 & 1 \\ 1 & -3 & 1 \\ 1 & 1 & -3 \end{vmatrix} = 16$
* $C_{13} = 1 \cdot \begin{vmatrix} -3 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & -3 \end{vmatrix} = 16$
* $C_{14} = -1 \cdot \begin{vmatrix} -3 & 1 & 1 \\ 1 & -3 & 1 \\ 1 & 1 & 1 \end{vmatrix} = 16$

**Perhitungan:**
$$\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13} + a_{14}C_{14}$$
$$\det(A) = 1(16) + (-3)(16) + 1(16) + 1(16)$$
$$\det(A) = 16 - 48 + 16 + 16 = \mathbf{0}$$
*(Matriks ini bersifat singular karena jumlah setiap barisnya adalah 0).*

---

## Bagian B: Menghitung Invers dengan Matriks Adjoin

**Rumus Umum:** $$A^{-1} = \frac{1}{\det A} \text{adj}(A)$$

### 4. Matriks 2x2
$A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}, \det(A) = -23$

**Proses:**
1. Tukar elemen diagonal utama, beri tanda negatif pada diagonal samping.
2. $\text{adj}(A) = \begin{bmatrix} 4 & 5 \\ -1 & -7 \end{bmatrix}$

**Hasil:**
$$A^{-1} = \frac{1}{-23} \begin{bmatrix} 4 & 5 \\ -1 & -7 \end{bmatrix} = \mathbf{\begin{bmatrix} -4/23 & -5/23 \\ 1/23 & 7/23 \end{bmatrix}}$$

---

### 5. Matriks 3x3
$A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}, \det(A) = -2$

**Proses:**
Menghitung matriks kofaktor $C$:
* $C_{11} = -2, C_{12} = -1, C_{13} = 0$
* $C_{21} = -2, C_{22} = 0, C_{23} = 0$
* $C_{31} = -8, C_{32} = -3, C_{33} = -2$

Transpos kofaktor untuk mendapat Adjoin:
$\text{adj}(A) = \begin{bmatrix} -2 & -2 & -8 \\ -1 & 0 & -3 \\ 0 & 0 & -2 \end{bmatrix}$

**Hasil:**
$$A^{-1} = \frac{1}{-2} \begin{bmatrix} -2 & -2 & -8 \\ -1 & 0 & -3 \\ 0 & 0 & -2 \end{bmatrix} = \mathbf{\begin{bmatrix} 1 & 1 & 4 \\ 0.5 & 0 & 1.5 \\ 0 & 0 & 1 \end{bmatrix}}$$

---

### 6. Matriks 4x4
$A = \begin{bmatrix} 1 & -3 & 1 & 1 \\ -3 & 1 & 1 & 1 \\ 1 & 1 & -3 & 1 \\ 1 & 1 & 1 & -3 \end{bmatrix}$

**Hasil:**
Berdasarkan perhitungan di nomor 3, **$\det(A) = 0$**. 
Sesuai syarat syarat matriks, jika determinan sama dengan nol, maka matriks tersebut tidak memiliki invers (**Matriks Singular**).