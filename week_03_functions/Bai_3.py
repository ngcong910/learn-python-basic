import math# goi de tinh toan như dung can
def chu_vi_tam_giac(a, b, c):
    return a+b+c
def dien_tich_tam_giac(a, b, c):
    p = (a + b + c) / 2  # Nửa chu vi
    return math.sqrt(p * (p - a) * (p - b) * (p - c))  # Công thức
def chu_vi_vuong(a):
    return 4 * a
def dien_tich_vuong(a):
    return a * a
def chu_vi_chu_nhat(a, b):
    return 2 * (a + b)
def dien_tich_chu_nhat(a, b):
    return a * b
def chu_vi_tron(r):
    return 2 * math.pi * r
def dien_tich_tron(r):
    return math.pi * r * r
def main():
    print("Chọn hình để tính toán:")
    print("1. Hình tam giác")
    print("2. Hình vuông")
    print("3. Hình chữ nhật")
    print("4. Hình tròn")   
    mode = int(input("Nhập lựa chọn (1-4): "))
    if mode == 1:
        a = float(input("Nhập cạnh a: "))
        b = float(input("Nhập cạnh b: "))
        c = float(input("Nhập cạnh c: "))
        print(f"Chu vi tam giác: {chu_vi_tam_giac(a, b, c)}")
        print(f"Diện tích tam giác: {dien_tich_tam_giac(a, b, c):.2f}")# .2f đề lam tron 2 chữ số thập phân
    elif mode == 2:
        a = float(input("Nhập cạnh hình vuông: "))
        print(f"Chu vi hình vuông: {chu_vi_vuong(a)}")
        print(f"Diện tích hình vuông: {dien_tich_vuong(a)}")  
    elif mode == 3:
        a = float(input("Nhập chiều dài: "))
        b = float(input("Nhập chiều rộng: "))
        print(f"Chu vi hình chữ nhật: {chu_vi_chu_nhat(a, b)}")
        print(f"Diện tích hình chữ nhật: {dien_tich_chu_nhat(a, b)}")    
    elif mode == 4:
        r = float(input("Nhập bán kính hình tròn: "))
        print(f"Chu vi hình tròn: {chu_vi_tron(r):.2f}")
        print(f"Diện tích hình tròn: {dien_tich_tron(r):.2f}")
    else:
        print("Lựa chọn không hợp lệ!")

main()
