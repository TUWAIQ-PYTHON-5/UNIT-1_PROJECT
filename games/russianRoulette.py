from random import randrange
from art import *
from users import Users




def gameInfo():
    tprint("Russian Roulette is a game of loading a bullet into one\nchamber of a revolver, spinning the cylinder, and then\npulling the trigger while pointing\nthe gun at one's own head.",font="fancy95")

def startGame():
    while True:
        tprint(f"If you want to quite press 0.",font="fancy95")
        number = int(input("How many tries do you want? "))
        points = number
        if number == 0:
            break
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
                Users.addPoints(Users.get_userID(),points)
            else:
                tprint(str(number) + " tries to go",font="fancy95")
