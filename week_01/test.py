CURRENT_YEAR=2025
first_name= input("Your first name is: ")
year_born= int(input("When were your born: "))
age =CURRENT_YEAR - year_born
print(age)
print(type(age))
print(("You are "+str(age)+" year old.")+ str( CURRENT_YEAR))
print("Your name is {1} with {2} year old in {0}".format( CURRENT_YEAR,first_name,age))
