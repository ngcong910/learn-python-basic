#Phạm Ngọc Công 24119116
# b)

Quan_ly={
    "Ngoc Cong": "034646340",
    "Tan Tai": "3257834"
}
Quan_ly["Gia Huy"]="03483487"
name=input("Nhap tên bạn muốn tìm kiếm ")
if name in Quan_ly:
    print(f"Số điện thoại bạn muốn tìm là:{Quan_ly[name]}")
else:
    print("Không tìm thấy số điện thoại của tên bạn tìm")
name_1=input("Nhập tên bạn muốn xóa ")
if name_1 in Quan_ly:
    del Quan_ly[name_1]
    print("Đã xóa khỏi danh bạ")
else:
    print("Số điện thoại bạn yêu cầu không tìm thấy")


ten=input("Nhập tên: ")
tuoi=int(input("Nhập tuổi: "))
ĐTB=float(input("Nhập điểm trung bình: "))

student={
    "name":ten,
    "age": tuoi,
    "DTB": ĐTB
}
print(student)
