import random
from art import *
from users import Users




def gameInfo():
    tprint("Coin flipping, coin tossing, or heads or tails is\nthe practice of throwing a coin in the air and checking \nwhich side is showing when it lands, in order to choose\n between two alternatives, heads or tails.",font="fancy95")
    return

def startGame():
    while True:
        tprint(f"If you want to quite press 0.",font="fancy95")
        while True:
            try:
                userChoice = int(input("Please choose 1.Heads or 2.Tails.\nWrite 1 or 2: "))
            except ValueError:
                print("Please write a Number.")
            else:
                if userChoice == 1:
                    userChoice = "heads"
                    break
                elif userChoice == 2:
                    userChoice = "tails"
                    break
                elif userChoice == 0:
                    break
                else:
                    print("wrong input")
        if userChoice == 0:
            break
        tossResult=random.choice(["heads", "tails"])
        tprint(f"It's {tossResult}",font="fancy95")
        if userChoice == tossResult:
            tprint("\nYOU WON",font="big",decoration="star25")
            Users.addPoints(Users.get_userID(),1)
        else:
            tprint("\nBETTER LUCK\nNEXT TIME",font="big",decoration="star25")
