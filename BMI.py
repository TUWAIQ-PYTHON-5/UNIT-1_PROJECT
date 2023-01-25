from art import *
from colorama import Fore, Back, Style


tprint("BMI",font="random")
print(Back.BLUE + 'is an estimate of body fat that is based on your weight and height.This calculation helps determine whether you are underweight, at a healthy weight, overweight, or obese.')
print(Style.RESET_ALL)



class BMI_calculatre:
    def __init__(self, name: str, weight : int, height : int):
        self.name = name
        self.weight = weight
        self.height = height

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



food_list = {Fore.BLUE + "apple": 52, "banana": 89, "carrot": 45, "donut": 200,}
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

