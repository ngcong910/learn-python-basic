#Phạm Ngọc Công 24119116
# a)
ten=input("Nhập tên: ") 
tuoi=int(input("Nhập tuổi: "))
ĐTB=float(input("Nhập điểm trung bình: "))

student={  # tạo dictionary
    "name":ten,
    "age": tuoi,
    "DTB": ĐTB
}
print(student) # in ra 

# b)
Quan_ly={ # tạo dictionary
    "Ngoc Cong": "034646340",
    "Tan Tai": "3257834"
}
Quan_ly["Gia Huy"]="03483487" # thêm một liên hệ mới 
name=input("Nhap tên bạn muốn tìm kiếm ")
if name in Quan_ly: # kiếm tên trong dictionary không 
    print(f"Số điện thoại bạn muốn tìm là:{Quan_ly[name]}")
else:
    print("Không tìm thấy số điện thoại của tên bạn tìm")
name_1=input("Nhập tên bạn muốn xóa ")
if name_1 in Quan_ly:
    del Quan_ly[name_1]
    print("Đã xóa khỏi danh bạ")
else:
    print("Số điện thoại bạn yêu cầu không tìm thấy")

# c)
def Nhap():   # tạo hàm nhập sinh viên
    sinh_vien_ds={} # tạo 1 dict rỗng
    n=int(input("Nhập số lượng sinh viên cần ghi là: "))
    for i in range(n):
        name=input(f"Nhập tên sinh viên {i+1}: ")
        diem=float(input(f"Nhập điểm: "))
        sinh_vien_ds[name]=diem # lưu vào dict
    return sinh_vien_ds

def trung_binh(sinh_vien_ds):
    if sinh_vien_ds:
        return sum(sinh_vien_ds.values())/len(sinh_vien_ds) # tính giá trị trung bình bằng hàm sum và len
    return 0

def hien_thi(sinh_vien_ds, diem_tb):
    print("Danh sach hoc sinh va diem: ")
    for name,diem in sinh_vien_ds.items():
        print(f"{name}:{diem}")
    print(f"Điểm trung bình của lớp là : {diem_tb:.2f}")

sinh_vien_ds=Nhap()
diem_tb=trung_binh(sinh_vien_ds)
hien_thi(sinh_vien_ds, diem_tb)    
