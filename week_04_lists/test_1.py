#number=[1,2,3]
#number.append(4)
#print(number)

#fruits=["táo","Chuối","Cam"]
#fruits.append("Xoài")
#print(fruits)

#even_numbers=[]
#for i in range(2,11,2):
#    even_numbers.append(i) #append them so sau list
#print(even_numbers)

numbers=[11,2,3,4,5,6,7,7,54,5,54,654,0,20,30,40]

numbers.extend([9,10,11])   # them nhieu phan tu vao danh sach
print(numbers)
numbers.insert(2,99)    # chen 99 vao vi tri 2
print(numbers)
numbers.remove(20)  # xoa phan tu dau tien co gia tri 20
print(numbers)
numbers.pop(6) # xoa phan tu tai vi tri 9 ( hoac cuo neu khong co 9 )
print(numbers)   #tra ve chi muc dau tien cua x trong danh sach 
print(numbers.index(9)) 
# dem so lan suat hien cua 40 trong danh sach
print(numbers.count(40))
numbers.sort()# xap sep danh sach tang dan
print(numbers)
numbers.reverse() # dao nguoc danh sach
print(numbers)

try:
    numbers.remove(2)
except:
    print("not exist")
print (numbers)


