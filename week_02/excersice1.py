sum=0
for i in range(3,100,2):
    N=float(1/i**i)
    sum+=N
S=float(1/sum)
S=round(S,2)
print(S)