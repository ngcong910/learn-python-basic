def main():
    n=int(input("Nhap 3 so nguyen: "))
    print_tang_dan(n)
    print_giam_dan(n)
def print_tang_dan(n):
    a=n//100
    b=(n//10)-a*10
    c=n%10
    if a<b:
        a,b=b,a
    if a<c:
        a,c=c,a
    if b<c:
        b,c=c,b
    print(a,b,c)
def print_giam_dan(n):
    a=n//100
    b=(n//10)-a*10
    c=n%10
    if a>b:
        a,b=b,a
    if a>c:
        a,c=c,a
    if b>c:
        b,c=c,b
    print(a,b,c)
main()


    