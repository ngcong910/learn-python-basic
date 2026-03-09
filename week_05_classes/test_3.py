class FatherDog:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return "Gaugau"
class BabyDog(FatherDog):
    pass
    # def speak(self):
    # return"Gau gau"

dog=BabyDog("Buddy")
print(dog.speak())