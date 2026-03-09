class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"Hello, my name is {self.name}, {self.age} yearold")

p1=Person("Pham Ngoc Cong",18)
p1.introduce()