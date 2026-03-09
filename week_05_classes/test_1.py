class student:
    def __init__(self):
        self.name=None
        self.age=None
        self.math_score=None
        self.literature_score=None
        self.english_score=None
    def avarage_score(self):
        ava_score=(self.math_score+self.literature_score+self.english_score)/3
        return ava_score
    def rank(self):
        avarage=self.avarage_score()
        print("avarage score is: "+str(avarage))
        if avarage>=9:
            print("Loại A")
        elif avarage<9:
            print("Loai B")
student1=student()
student1.name="Ngoc Cong"
student1.age=18
student1.math_score=9
student1.literature_score=8
student1.english_score=9
student1.rank()
print(f"Điểm trung bình của {student1.name}: {student1.avarage_score():.2f}")

student2=student()
student2.name="Ngoc Duy"
student2.age=19
student2.math_score=10
student2.literature_score=9
student2.english_score=10
student2.rank()
print(f"Điểm trung bình của {student2.name}: {student2.avarage_score():.2f}")



class Student:
    def __init__(self,name, age,math_score,literature_score,english_score):
        self.name=name # thuộc tính name
        self.age=age
        self.math_score=math_score
        self.literature_score=literature_score
        self.english_score=english_score
    def avarage_score(self):
        ava_score=(self.math_score+self.literature_score+self.english_score)/3
        return ava_score
    def rank(self):
        avarage=self.avarage_score()
        print("avarage score is: "+str(avarage))
        if avarage>=9:
            print("Loại A")
        elif avarage<9:
            print("Loai B")
    def introduce(self): # phương thức hành động
        print(f"Hello, my name is {self.name},with điểm trung bình {self.avarage_score():.2f}")

students=[]
    
student1=Student("Cong",18,8,9,8)
student2=Student("Duy",19,3,6,9)

student2.math_score=8

students.append(student1)
students.append(student2)

for i in range(len(students)):
    students[i].rank()