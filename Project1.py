

class information:
    kind = "Human"

    def __init__(self, name : str, age : int, gender : str):
        #initialize object / instance attributes
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce_self(self):
        return f"Welcome,{self.name} you are here in Diabetic program\n"


#to create a new object/instance from the class Person
person1 = information("Mohammed", 20, 55)

#to read an isntance attribute
print("\n\n\n", person1.name)

#calling a method
print(person1.introduce_self())


user_want=input("For watch our services in diabetic program type 'services'\n")
if user_want=='services':
 print("Before we show our services ,We need your information\n")

 age = input("Can we know your age:)\n")
 Weight=input("enter your weight: ")
print("Okay your age is",age,"Years old , your weight is:",Weight ,"kg\n") 

from Services import*
















'''
name = input("please enter your name here : \n")

print("Welcome",name,",you are here in Diabetic program\n")

user_want=input("For quick inquiry type 'quick' or watch our services in diabetic program type 'services'\n")
if user_want.lower =='quick\n':
        print("what is your quick inquiry")
elif user_want.lower=='services':
        print("Before we show our services ,We need your information\n")
        
age = input("Can i know your age:)\n")

Weight=input("enter your weight: ")
print("Okay your age is",age,"Years old and your weight is:",Weight ,"kg\n") 
'''












    










