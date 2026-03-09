import tkinter as tk
import math

class CasioCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Máy tính Casio")

        # Các ô nhập liệu
        tk.Label(root, text="Số thứ nhất:").grid(row=0, column=0)
        self.entry1 = tk.Entry(root)
        self.entry1.grid(row=0, column=1)

        tk.Label(root, text="Số thứ hai (nếu cần):").grid(row=1, column=0)
        self.entry2 = tk.Entry(root)
        self.entry2.grid(row=1, column=1)

        tk.Label(root, text="Kết quả:").grid(row=2, column=0)
        self.result_entry = tk.Entry(root)
        self.result_entry.grid(row=2, column=1)

        # Các nút chức năng
        tk.Button(root, text="+", width=6, command=self.cong).grid(row=3, column=0)
        tk.Button(root, text="-", width=6, command=self.tru).grid(row=3, column=1)
        tk.Button(root, text="*", width=6, command=self.nhan).grid(row=3, column=2)
        tk.Button(root, text="/", width=6, command=self.chia).grid(row=3, column=3)
        tk.Button(root, text="√x", width=6, command=self.can_bac_2).grid(row=4, column=0)
        tk.Button(root, text="√n(x)", width=6, command=self.can_bac_n).grid(row=4, column=1)
        tk.Button(root, text="x!", width=6, command=self.nut_giai_thua).grid(row=4, column=2)
        tk.Button(root, text="x²", width=6, command=self.binh_phuong).grid(row=4, column=3)
        tk.Button(root, text="x³", width=6, command=self.bac_3).grid(row=5, column=0)
        tk.Button(root, text="xⁿ", width=6, command=self.luy_thua_n).grid(row=5, column=1)

    def show_result(self, value):
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, str(value))

    def get_values(self):
            x = float(self.entry1.get())
            y = float(self.entry2.get()) if self.entry2.get() else None
            return x, y

    def cong(self):
        x, y = self.get_values()
        if y is not None: self.show_result(x + y)

    def tru(self):
        x, y = self.get_values()
        if y is not None: self.show_result(x - y)

    def nhan(self):
        x, y = self.get_values()
        if y is not None: self.show_result(x * y)

    def chia(self):
        x, y = self.get_values()
        if y is not None:
            if y != 0:
                self.show_result(x / y)
            else:
                self.show_result("Lỗi chia 0")

    def can_bac_2(self):
        x, _ = self.get_values()
        if x is not None: self.show_result(math.sqrt(x))

    def can_bac_n(self):
        x, y = self.get_values()
        if y is not None:
            self.show_result(x ** (1 / y))

    def giai_thua(self,n):
        if n<=1:
            return 1
        else:
            return n*self.giai_thua(n-1)
        
    def nut_giai_thua(self):
        x, _ = self.get_values()
        if x is not None and x >= 0 and x == int(x):
            kq = self.giai_thua(int(x))
            self.show_result(kq)

    def binh_phuong(self):
        x, _ = self.get_values()
        if x is not None: self.show_result(x ** 2)

    def bac_3(self):
        x, _ = self.get_values()
        if x is not None: self.show_result(x ** 3)

    def luy_thua_n(self):
        x, y = self.get_values()
        if y is not None:
            self.show_result(x ** y)

# Chạy chương trình
root = tk.Tk()
app = CasioCalculator(root)
root.mainloop()

