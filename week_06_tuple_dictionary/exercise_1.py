# a)
n=(1,2,3,4,5)
print(sum(n))
print(max(n))

# b)
def Ten():
    danh_sach=[]
    while True:
        name=input("Nhập tên: ")
        if name=="STOP":
            break
        danh_sach.append(name)
    return tuple(danh_sach)
ten=tuple(sorted(Ten()))
print(ten)

# c)
nhap_input=input("Nhập danh sách điểm, cách nhau bởi dấu cách: ")
nhap=tuple(map(int,nhap_input.split()))
max_nhap=max(nhap)
count_nhap=nhap.count(max(nhap))  
print(f"Điểm cao nhất: {max_nhap}, và số lần xuất hiện là: {count_nhap}")