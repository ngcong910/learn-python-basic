n = int(input("Nhập số nguyên n: "))  
a = True  # Cho no la so nguyen to
if n < 2:
    a = False # khong co so nguyen nho hơn 2

i = 2
while i * i <= n: # dung vong lap de kiem tra tu 2 den can n  
    if n % i == 0:  # neu n chia het cho i no khong phai la so nguyen to
        a = False
        break  # khong can kiemtra dung vong lap
    i += 1  # tang 1 neu if khong thoa

if a:
    print("{0} là số nguyên tố.".format(n))
else:
    print("{0} không phải là số nguyên tố.".format(n))