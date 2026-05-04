import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.animation import FuncAnimation

# Menggunakan backend TkAgg agar jendela interaktif muncul
matplotlib.use('TkAgg')

class RefleksiPro:
    def __init__(self, x_target, y_target, jenis):
        self.jenis = jenis
        self.x_final = list(x_target)
        self.y_final = list(y_target)
        self.n = len(x_target) - 1
        
        # Titik Awal Animasi (Offset luar)
        offset = 15
        self.x_start_asal = [x + offset for x in self.x_final]
        self.y_start_asal = [y + offset for y in self.y_final]
        
        xr_f, yr_f = self.get_full_refleksi(self.x_final, self.y_final)
        self.x_start_pantul = [x - offset for x in xr_f]
        self.y_start_pantul = [y - offset for y in yr_f]

        # Setup Figure
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        
        # Set awal sumbu
        self.ax.set_xlim(-15, 15)
        self.ax.set_ylim(-15, 15)
        self.ax.axhline(0, color='black', lw=1)
        self.ax.axvline(0, color='black', lw=1)
        self.ax.grid(True, linestyle=':', alpha=0.6)
        
        self.plot_cermin()

        self.line_asal, = self.ax.plot([], [], 'bo-', lw=2, label="Asal (Tarik Titik)")
        self.line_bayangan, = self.ax.plot([], [], 'ro--', lw=2, alpha=0.6, label="Bayangan")
        
        self.dragging_point = None

        # Jalankan Animasi
        self.ani = FuncAnimation(self.fig, self.animate, frames=101, interval=20, blit=False, repeat=False)
        
        # Event Mouse
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_drag)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        
        plt.legend()
        plt.title("Tarik titik biru ke tepi layar untuk memperluas map")
        plt.show()

    def hitung_refleksi(self, x, y):
        j = self.jenis
        if j == "1": return x, -y
        elif j == "2": return -x, y
        elif j == "3": return y, x
        elif j == "4": return -y, -x
        elif j == "5": return -x, -y
        return x, y

    def get_full_refleksi(self, x_list, y_list):
        res = [self.hitung_refleksi(xi, yi) for xi, yi in zip(x_list, y_list)]
        return zip(*res)

    def plot_cermin(self):
        if self.jenis == "1": self.ax.axhline(0, color='green', lw=2, zorder=1)
        elif self.jenis == "2": self.ax.axvline(0, color='green', lw=2, zorder=1)
        elif self.jenis in ["3", "4"]:
            v = np.array([-100, 100]) # Garis cermin panjang agar tidak putus saat zoom out
            self.ax.plot(v, v if self.jenis=="3" else -v, 'g-', lw=1, alpha=0.5)

    def animate(self, frame):
        alpha = frame / 100
        cx = [(1-alpha)*s + alpha*f for s, f in zip(self.x_start_asal, self.x_final)]
        cy = [(1-alpha)*s + alpha*f for s, f in zip(self.y_start_asal, self.y_final)]
        
        xr_f, yr_f = self.get_full_refleksi(self.x_final, self.y_final)
        cxr = [(1-alpha)*s + alpha*f for s, f in zip(self.x_start_pantul, xr_f)]
        cyr = [(1-alpha)*s + alpha*f for s, f in zip(self.y_start_pantul, yr_f)]
        
        self.line_asal.set_data(cx, cy)
        self.line_bayangan.set_data(cxr, cyr)
        return self.line_asal, self.line_bayangan

    def on_click(self, event):
        if event.inaxes != self.ax: return
        for i in range(self.n):
            dist = np.hypot(self.x_final[i] - event.xdata, self.y_final[i] - event.ydata)
            if dist < 0.8:
                self.dragging_point = i
                break

    def on_drag(self, event):
        if self.dragging_point is None or event.inaxes != self.ax: return
        
        # Update posisi
        self.x_final[self.dragging_point] = event.xdata
        self.y_final[self.dragging_point] = event.ydata
        if self.dragging_point == 0:
            self.x_final[-1], self.y_final[-1] = event.xdata, event.ydata
        
        xr, yr = self.get_full_refleksi(self.x_final, self.y_final)
        self.line_asal.set_data(self.x_final, self.y_final)
        self.line_bayangan.set_data(xr, yr)

        # --- LOGIKA PERLUASAN MAP MANUAL ---
        # Ambil semua koordinat yang ada (asal + bayangan)
        semua_x = self.x_final + list(xr)
        semua_y = self.y_final + list(yr)
        
        margin = 5
        xmin, xmax = min(semua_x) - margin, max(semua_x) + margin
        ymin, ymax = min(semua_y) - margin, max(semua_y) + margin
        
        # Update limit sumbu secara dinamis jika titik mendekati tepi
        curr_xmin, curr_xmax = self.ax.get_xlim()
        curr_ymin, curr_ymax = self.ax.get_ylim()

        if xmin < curr_xmin or xmax > curr_xmax or ymin < curr_ymin or ymax > curr_ymax:
            self.ax.set_xlim(min(xmin, curr_xmin), max(xmax, curr_xmax))
            self.ax.set_ylim(min(ymin, curr_ymin), max(ymax, curr_ymax))

        self.fig.canvas.draw_idle()

    def on_release(self, event):
        self.dragging_point = None

# --- Main ---
try:
    pilih = input("Pilihan Refleksi (1:Sumb X, 2:Sumb Y, 3:y=x, 4:y=-x, 5:Pusat): ")
    n = int(input("Jumlah titik: "))
    xi_list, yi_list = [], []
    for i in range(n):
        xi_list.append(float(input(f"Titik {i+1} x: ")))
        yi_list.append(float(input(f"Titik {i+1} y: ")))
    xi_list.append(xi_list[0])
    yi_list.append(yi_list[0])
    RefleksiPro(xi_list, yi_list, pilih)
except ValueError:
    print("Input harus berupa angka!")