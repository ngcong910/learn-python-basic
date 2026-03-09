class Student:
    def __init__(self,name,student_id,gpa):
        self.name=name
        self.student_id=student_id
        self.gpa=gpa
    def display_info(self):
        print(f"SV: {self.name}, MSSV: {self.student_id}, GPA: { self.gpa}")
student1=Student(input("Name: "), input("MSSV: "), float(input("GPA: ")))

student1.display_info()