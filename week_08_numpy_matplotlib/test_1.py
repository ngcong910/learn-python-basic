import numpy as np 
#arr=np.array([1,2,3,4,5,6])
#print(arr)

#a=np.linspace(0,1,5) # chạy từ 0 đến 1 có 5 số 
#print(a)

#b=np.random.rand(2,3)
#print(b)
#np.full((2,3),7) # tạo mảng 2x3 với số 7 không 
#np.eye # tạo đường chép trong ma trận với 4 hàng 4 cột và đường chéo là giá trị 1

#a=np.random.rand(3,3)
#c=np.random.randint(1,50,(3,3))
#d=np.random.randn(3,3)

#print(a)
#print(c)
#print(d)

#arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(arr[0,2])

#arr[1,2]=99

#print(arr)

#print(arr[:,1])
#print(arr[0,:])

##arr=np.array([10,20,30,40,50,60,70])
 
#print(arr[1]) # lấy phần tử số 1 
#print(arr[:3]) # lấy từ phần tử thứ 3 trở xuống
#print(arr[-3:]) # lấy 3 phần tử ngoài cùng

#a=np.array([1,2,3])
#b=np.array([4,5,6])

#print(a+b)
#print(a*b)
#print(a/2)
#print(np.dot(a,b)) # tính tích vô hướng 

# ma trận

#A=np.array([1,2],[3,4])
#B=np.array([5,6],[7,8])

#print(A@B) #AxB
#print(np.dot(A,B)) 
#print(np.linalg.inv(A)) #1/A ( nghịch đảo ma trận)
#print(np.linalg.det(A)) # lấy đường chéo chính trừ  đường chéo phụ (định thức )

# thống kê với numpy

#arr=np.array([1,2,3,4,5,6])
#print(np.mean(arr))
#print(np.median(arr))
#print(np.var(arr))
#print(np.std(arr))
#rint(np.sum(arr))
#print(np.max(arr))
#print(np.min(arr))

#thay đổi kích thước 
#arr=np.arange(1,7)
#new_arr=arr.reshape((2,3))

#print(arr)
#print(new_arr)

a=np.array([[1,2],[4,5]])
b=np.array([7,8])

np.vstack((a,b))
np.hstack((a,b.T))
