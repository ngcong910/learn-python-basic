numbers=(1,2,3,4,5,6)
print(numbers)


fruits="Táo","Cam","Xoài"
print(fruits)

letters=tuple(["a","b","c"])
print(letters)


# nếu có 1 phần tử 
single_element=(10,) # phải có dấu phảy
print(single_element)

# truy cập phần tử trong tuple
color=("a","b","c")
print(color[0]) # in ra :a
print(color[1]) # in ra :b
print(color[-1]) # in ra :c

#cắt tuple (slicing tuple)
numbers=(1,2,3,4,5,6)
print(numbers[1:4]) # output: (2,3,4)
print(numbers[:3])  #output:(1,2,3)
print(numbers[-3:]) #output:(40,50,60)

#Tính bất biến của Tuple
color=("red","green","blue")
#color[1]="black"# báo lỗi

temp=list(color)
temp[1]="black"
color=tuple(temp)
print(color)# output: "red","black","blue"


#duyệt qua tuple

animals="gấu","Chó","Concac"
for animal in animals:
    print(animal)

#MỘT SỐ PHƯƠNG THỨC QUANG TRỌNG 
numbers=(1,2,3,4,5,6,7,8,9,10)
numbers_1=[1,2,3,5,6,7,8,10]
ten="Cong"
print(numbers.count(2)) #output:1
print(numbers.index(2)) #output:1
print(len(numbers)) #output:10
print(max(numbers)) #outpit:10
print(min(numbers)) #output: 1
print(sum(numbers)) #output:éo biết
print(sorted(numbers)) #output:[1,2,3,4,5,6,7,9,10]
print(list(numbers_1)) # chuyển list thành tuple
#print(tuple(string(ten))) # chuyển chuổi sang từng kí tự  #LỖI KHÚC NÀY

tuple1=(1,2,3)
tuple2=(4,5,6)
resuls=tuple1+tuple2
print(resuls) #output: 1,2,3,4,5,6

