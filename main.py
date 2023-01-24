from art import *
from games import headsOrTale,ticTacToe,russianRoulette,oddOrEven
import users
tprint(f"\nWELCOME\nARE YOU\nREADY FOR\nFOR PLAYING",font="big",decoration="star25")
tprint(f"HERE WHAT\nCAN YOU DO",font="star11")
tprint(f"-SEE THE\nAVAILABLE\nGAME",font="crawford")
tprint(f"-GET THE\nGAME INFO",font="crawford")
tprint(f"-PLAY SOLO\nOR MULTIPLE",font="crawford")
tprint(f"-GATHER POINTS",font="crawford")

tprint(f"PRESS 1 TO LOG IN\n2 TO BE A VISITOR",font="crawford")

while True:
    try:
        command = int(input(""))
    except ValueError:
        tprint("Please write a Number.",font="crawford")
    else:
        if command == 1 or command == 2:
            userinfo = users.user(command)
            break
        else:
            tprint("please choose 1 or 2",font="crawford")
        


tprint(f"PLAESE SELECT A\nGAME\n1.heads Or Tale\n2.TicTacToe\n3.Russian\nRoulette\n4.Odd Or Even",font="crawford")
while True:
    try:
        command = int(input(""))
    except ValueError:
        tprint("Please write a Number.",font="crawford")
    else:
        if command == 1:
            while True:
                tprint("PRESS 1 TO\nGET GAME INFO\n2 TO START\nTHE GAME",font="crawford")
                try:
                    command = int(input(""))
                except ValueError:
                    tprint("please choose 1 or 2",font="crawford")
                else:
                    if command == 1:
                        headsOrTale.gameInfo()
                    elif command == 2:
                        headsOrTale.startGame()
                        break
                    else:
                        tprint("please choose 1 or 2",font="crawford")
    break
