m=int(input("Nhap m="))
n=int(input("Nhap n="))
for i in range(m,0,-1): # vong lap chay tu m den 0
    if m%i==0 and n%i==0:   # neu m va n chia het cho so lon nhat
        break # dung vong lap
print("UCLN cua {0} va {1} la: {2}".format(m,n,i)) # ham format de la m n va i cho nhanh 
        