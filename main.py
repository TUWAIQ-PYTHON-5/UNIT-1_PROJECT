from art import *
from games import headsOrTale,ticTacToe,russianRoulette,oddOrEven
from users import Users


tprint(f"\nWELCOME\nARE YOU\nREADY FOR\nFOR PLAYING",font="big",decoration="star25")
tprint(f"HERE WHAT\nCAN YOU DO",font="star11")
tprint(f"-SEE THE\nAVAILABLE\nGAME",font="crawford")
tprint(f"-GET THE\nGAME INFO",font="crawford")
# tprint(f"-PLAY SOLO\nOR MULTIPLE",font="crawford")
tprint(f"-GATHER POINTS",font="crawford")

tprint(f"PRESS 1 TO LOG IN\n2 TO BE A VISITOR",font="colossal")

while True:
    try:
        command = int(input(""))
    except ValueError:
        tprint("Please write a Number.",font="colossal")
    else:
        if command == 1 or command == 2:
            userinfo = Users.user(command)
            break
        else:
            tprint("please choose 1 or 2",font="colossal")
        

while True:
    tprint(f"If you want to quite press 0.",font="fancy95")
    
    while True:
        tprint(f"PLAESE SELECT A\nGAME\n1.heads Or Tale\n2.TicTacToe\n3.Russian\nRoulette\n4.Odd Or Even",font="colossal")
        try:
            command = int(input(""))
        except ValueError:
            tprint("Please write a Number.",font="colossal")
        else:
            if command == 0:
                break
            elif command == 1:
                while True:
                    tprint("PRESS 1 TO\nGET GAME INFO\n2 TO START\nTHE GAME",font="colossal")
                    try:
                        command = int(input(""))
                    except ValueError:
                        tprint("please choose 1 or 2",font="colossal")
                    else:
                        if command == 1:
                            headsOrTale.gameInfo()
                        elif command == 2:
                            headsOrTale.startGame()
                            break
                        elif command == 0:
                            break
                        else:
                            tprint("please choose 1 or 2",font="colossal")
            elif command == 2:
                while True:
                    tprint("PRESS 1 TO\nGET GAME INFO\n2 TO START\nTHE GAME",font="colossal")
                    try:
                        command = int(input(""))
                    except ValueError:
                        tprint("please choose 1 or 2",font="colossal")
                    else:
                        if command == 1:
                            ticTacToe.gameInfo()
                        elif command == 2:
                            ticTacToe.startGame()
                            break
                        elif command == 0:
                            break
                        else:
                            tprint("please choose 1 or 2",font="colossal")
            elif command == 3:
                while True:
                    tprint("PRESS 1 TO\nGET GAME INFO\n2 TO START\nTHE GAME",font="colossal")
                    try:
                        command = int(input(""))
                    except ValueError:
                        tprint("please choose 1 or 2",font="colossal")
                    else:
                        if command == 1:
                            russianRoulette.gameInfo()
                        elif command == 2:
                            russianRoulette.startGame()
                            break
                        elif command == 0:
                            break
                        else:
                            tprint("please choose 1 or 2",font="colossal")
            elif command == 4:
                while True:
                    tprint("PRESS 1 TO\nGET GAME INFO\n2 TO START\nTHE GAME",font="colossal")
                    try:
                        command = int(input(""))
                    except ValueError:
                        tprint("please choose 1 or 2",font="colossal")
                    else:
                        if command == 1:
                            oddOrEven.gameInfo()
                        elif command == 2:
                            oddOrEven.startGame()
                            break
                        elif command == 0:
                            break
                        else:
                            tprint("please choose 1 or 2",font="colossal")   
    if command == 0:
        break
if userinfo == 1:
    tprint(f"YOU HAVE{Users.showPoints(userinfo)} POINTS",font="colossal")


tprint(f"\nTHANK YOU\nFOR PLAYING\nTILL NEXT TIME",font="big",decoration="star25")