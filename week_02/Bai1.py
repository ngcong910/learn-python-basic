n=int(input("Nhap n: "))
a=0
for i in range(len(str(n))):# lấy sô lượng cua vòng lap n 
    a=a*10+n%10  # de dich so sang trai va cong them chu so cuoi cua n
    n//=10# xoa chu so cuoi cua n
print(" So sau khi hoan doi la: ",a)

