#Phamn_Ngoc_Cong_24119116
def giai_thua(n):
    if n==0:
        return 1
    return (n*giai_thua(n-1))
def tong(dau,cuoi,bnhay):
    kq=0
    for i in range(dau,cuoi,bnhay):
        kq+=(1/giai_thua(i))
    return kq
a=int(input("Nhap a="))
s=tong(3,a,2)
print(1/s)
