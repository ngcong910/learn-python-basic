def main():
    with open("Danh_sach.txt","w",encoding="utf-8") as file: # encoding dùng để gõ chữ có dấu
        tong_homnay=0 # dùng để tính tống số tiền
        danh_sach=[]
        while True:     # cho vòng lập chạy đúng
            Ten=input("Tên khách hàng: ")
            if Ten=="STOP":
                break # khi nao minh gõ stop thì thoát vòng lap
            time_on=input("Thời gian lên xe: ")
            time_off=input("Thời gian xuống xe: ")
            so_km=float(input("Số km đi được là: "))
            print("\n")

            danh_sach.append(Ten)
            tong=tinh_tien(so_km)

            tong_homnay+=tong

            file.write(f"{Ten},{time_on},{time_off},{so_km:.2f}\n")
        ket_qua(tong_homnay,danh_sach)    


def tinh_tien(so_km):       
    with open("Danh_sach.txt","r",encoding="utf-8") as file:
        if so_km==1:
            return 13000
        if so_km>1 and so_km<=35:
            return 13000+(so_km-1)*12000
        if so_km>35:
            return 13000+12000*34+(so_km-35)*11000

def ket_qua(tong_homnay,danh_sach):
    with open("Danh_sach.txt","r",encoding="utf-8") as file:
        print(f"Tổng số tiền hôm nay thu được: {tong_homnay}")
        print(f"Tổng số khách hàng hôm nay:{len(danh_sach)}")

main()
