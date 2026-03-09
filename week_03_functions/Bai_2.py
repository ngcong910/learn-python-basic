def main():
    CK=float(input("Diem chuyen can: "))
    BTL=float(input("Diem bai tap tren lop: "))
    BTN=float(input("Diem bai tap ve nha: "))
    GK=float(input("Diem giua ki: "))
    CKN=float(input("Diem cuoi ki: "))
    diem_tong(CK,BTL,BTN,GK,CKN)
    tong= diem_tong(CK,BTL,BTN,GK,CKN)

    print(f"Điểm tổng cần tính:{tong}")

    xep_loai(tong)
def diem_tong(CK,BTL,BTN,GK,CKN):
    tong=CK*0.1+BTL*0.1+BTN*0.1+GK*0.2+CKN*0.5
    return tong

def xep_loai(tong):
    if tong>9:
        print("Gioi")
    else:
        print("Ngu")
main()