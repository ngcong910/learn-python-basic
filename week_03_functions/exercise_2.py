def main():
    a=int(input("Nhap so a= "))
    b=int(input("Nhap so b= "))
    mode=input("Nhap che do(even,old): ")
    if mode =="even":
        print_even(a,b)
    elif mode=="old":
        print_old(a,b)
def print_even(a,b):
    for i in range(a+1,b):
        if i%2==0:
            print(i) 
def print_old(a,b):
    for i in range(a+1,b):
        if i%2==1:
            print(i)
main()
