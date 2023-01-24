from random import randrange
from art import *



def gameInfo():
    tprint("Russian Roulette is a game of loading a bullet into one chamber of a revolver, spinning the cylinder, and then pulling the trigger while pointing the gun at one's own head.",font="fancy95")

def startGame():
    number = int(input("How many tries do you want? "))
    while number != 0:
        predection = int(input("Choose a bullet: 1,2,3,4,5,6? "))
        shot = randrange(6) + 1
        if predection > 6 or predection < 1:
            print("Wrong Bullet")
        elif shot == predection:
            tprint("\n*BANG*\nYOU ARE DEAD!x_x",font="big",decoration="star25")
            break
        else:
            tprint("\n*CLICK*\nYOU SURViVED",font="big",decoration="star23")
        number = number - 1
        if number == 0:
            tprint("\nCongratulations you WIN \o/",font="big",decoration="star23")
        else:
            tprint(str(number) + " tries to go",font="fancy95")
