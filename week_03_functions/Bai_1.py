def print_tinh_tong(km):
    if km==1:
        print("Gia tinh ban tra la 13000 VND")
    if km>=1 and km<=35:
        tien=13000+(km-1)*12000
        print("Gia tien ban phai tra la:{0} VND ".format(tien))
    if km>35:
        tien=13000+34*12000+(km-35)*11000
        print("Gia tien ban phai tra la:{0} VND ".format(tien))
def main():
    km=float(input("So km di duoc la: "))
    print_tinh_tong(km)
main()
