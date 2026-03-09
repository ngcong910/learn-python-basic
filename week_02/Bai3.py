n=int(input("Nhap n="))
a=0 #cho bien dem=0
while n>0: # khi nao n= ket thuc vong lap
    n//=10  # giam so cuoi
    a+=1    # tang bien dem len 1
print("Có {0} chữ số. ".format(a))