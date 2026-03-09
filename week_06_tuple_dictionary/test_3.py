student={
    "name": "Pham ngoc cong",
    "age":18,
    "major": "computer science"
}

#cach 2
student2= dict(name="Le Thi B", age=22,major="mathematics")

print(student)
print(student2)

# cách chiếc xuất dictiionary

print(student["name"])
print(student.get("age"))

# sự khác biệt giữa [], get:
# [] báo lỗi nếu khóa không tồn tai
# get() trả về NONE nếu khóa không tồn tại

# thêm cập nhập giá trị mới 

student["age"]=19
student["email"]="phamngocong910@gmail.com"# thêm key

print(student)

# xóa phần tư trong dictionary

# cách 1

del student["email"]
print(student)
#del chỉ xóa phần tử 

# cách 2

age=student.pop("age")
print(f"Are has been deleted:{age}")
print(student)
#pop() vừa xóa vừa trả về vị trí 

# Duyệt qua DICtionary

# duyệt qua các khóa 
for key in student.keys():
    print(key)

# duyệt qua các giá trị 
for value in student.values():
    print(value)

# duyệt qua các khóa và giá trị 
for key, value in student.items():
    print(f"{key}: {value}")

# kiểm tra sự tồn tại của khóa 
if "age" in student:
    print("Co key 'age' trong dictionary")

#Dictionary Lồng nhau
students={
    "student1": {"name":"Pham Ngoc Cong", "age":31},
    "student2": {"name":"Critiano Ronaldo", "age": 40}
}
print (students["student1"]["name"])