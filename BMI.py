from art import *
from colorama import Fore, Back, Style

tprint("welcome to my project :)",font="random")
tprint("BMI",font="random")
print(Back.BLUE + 'is an estimate of body fat that is based on your weight and height.This calculation helps determine whether you are underweight, at a healthy weight, overweight, or obese.')
print(Style.RESET_ALL)




class BMI_calculatre:
    def __init__(self, name: str, weight : int, height : int):
        self.name = name
        self.weight = weight
        self.height = height

    def set_name(self,name):
        self.name = name 
    def get_name(self):
        return self.get_name

    def set_weight(self,weight):
        self.weight = weight 
    def get_weight(self):
        return self.get_weight

    def set_height(self,height):
        self.height = height
    def get_height(self):
        return self.get_height

    

    def custmer_add(self):
        print(f"your name is:{self.name} || Enter your height in cm: {self.height} || Enter your Weight in Kg:{self.weight}")

name = input("Enter your name: ")
Height=float(input("Enter your height in cm: "))
Weight=float(input("Enter your Weight in Kg: "))

H = lambda Height, Weight: Weight/Height/Height
BMI= H(Height, Weight)*10000
print(Fore.GREEN + "your Body Mass Index is: ",BMI)



if(BMI>0):
	if(BMI<=16):
		print(Fore.RED + "you are severely underweight")
	elif(BMI<=18.5):
		print(Fore.RED + "you are underweight")
	elif(BMI<=25):
		print(Fore.RED + "you are Healthy")
	elif(BMI<=30):
		print(Fore.RED + "you are overweight")
	else: print(Fore.RED + "you are severely overweight")
else:(Fore.RED + "enter valid details")



food_list = {Fore.BLUE + "apple": 52, "banana": 89, "carrot": 45, "donut": 200, }
def check_food(food):

    try:
        calories = food_list[food]
        if calories > 100 and BMI > 18.5 :
            raise ValueError("Too many calories")
        print("you can eat this food")
    except KeyError:
        print("this food is not in the list.")



while True:
    userInput=input("do you want to see the list of foods and their calories ? (y/n)")
    if userInput.lower() == 'y':
        for food, calories in food_list.items():
            print(f"{food}: {calories} calories")
             
        userFoodInput=input("Type in an item from the list: ")
        try:
            check_food(userFoodInput.lower())
        except ValueError as e:
            print(e)
    elif userInput.lower() == 'n':
        print("okay, have a great day!")
        break
    else:
        print("invalid input. please enter y or n.")



class Rmr_Calculatre(BMI_calculatre):

    def __init__(self, name: str, weight : int, height : int, age : int, gender : str):
        super().__init__(name, weight, height)
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender

    def set_age(self,age):
        self.age = age    
    def get_age(self):
        return self.get_age

    def set_gender(self,gender):
        self.gender = gender    
    def get_gender(self):
        return self.get_gender


    
    def check_rmr(self):
        gender_rteturn=0
        try:
            if self.gender == "male":
                gender_rteturn=88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
                return gender_rteturn
            elif self.gender== "female":    

                gender_rteturn= 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)
                return gender_rteturn
        except:
            print("invalid gender. please enter 'male' or 'female'.")


name = input("Enter your name: ")
Height=float(input("Enter your height in cm: "))
Weight=float(input("Enter your Weight in Kg: "))
age = int(input("Enter your age in years: "))
gender = input("Enter your gender (male or female):")
 

rmr = Rmr_Calculatre(name, Weight, Height, age, gender)
print("your resting metabolic rate is:", rmr.check_rmr() , "calories per day.")



