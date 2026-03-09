N=int(input("Nhap gia tien can do (1) hay Nhap so lit xang can do (2), yeu cau nhap so: "))
Gia_Tien_VND=21510
if N==1:
    C=float(input("Nhap so tien can do (USD): "))
    A=(C*25540)
    B=float(A/Gia_Tien_VND)
    B=round(B,2)
    print("So lit xang se do duoc:{0}L".format(B))
elif N==2:
    A=float(input("Nhap so lit xang can do: "))
    B=A*Gia_Tien_VND
    C=float(B/25540)
    C=round(C,1)
    print("So tien can tra la:{0}USD".format(C))
else:
    print("Nhap loi, Yeu cau nhap lai!!!")