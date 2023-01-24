import users
import random
from art import *
from colorama import Fore,Back

def gameInfo():
    tprint("Odd or Even is a game in which one the Console selects an odd or even number and the player guesses which it is.",font="fancy95")

def startGame():
    while True:
        tprint(f"If you want to quite press 0.",font="fancy95")
        while True:
            try:
                userChoice = int(input("Please choose 1.Odd or 2.Even.\nWrite 1 or 2: "))
            except ValueError:
                print("Please write a Number.")
            except userChoice == 0:
                break
            else:
                if userChoice == 1:
                    userChoice = "Odd"
                    break
                elif userChoice == 2:
                    userChoice = "Even"
                    break
                else:
                    print("wrong input")
        if userChoice == 0:
            break
        numberResult=random.choice(range(10))
        print(f"It's {numberResult}")
        if numberResult%2 == 0:
            numberResult = "Even"
        else:
            numberResult = "Odd"

        if userChoice == numberResult:
            tprint("\nYOU WON",font="music2",decoration="star25")

        else:
            tprint("\nBETTER LUCK\nNEXT TIME",font="music2",decoration="star25")