from art import *
from users import Users




board = ["-","-","-","-","-","-","-","-","-"]
game_on = True
current_player = "X"

def gameInfo():
    tprint("Tic Tac Toe is a game in which two players seek in\nalternate turns to complete a row, a column, or a\ndiagonal with either three O's or three X's drawn in\nthe spaces of a grid of\nnine squares; noughts and crosses.",font="fancy95")

def display_board():
    tprint(board[6] + " | " + board[7] + " | " + board[8] + "      " + "7|8|9",font="big")
    tprint(board[3] + " | " + board[4] + " | " + board[5] + "      " + "4|5|6",font="big")
    tprint(board[0] + " | " + board[1] + " | " + board[2] + "      " + "1|2|3",font="big")

def players():
    tprint("Select Player - X or O",font="big")
    artInput = text2art("Player1: ",font="star25" )
    p1 = input(artInput).upper()
    p2 = ""
    if p1 == "X":
        p2 = "O"
        tprint("Player2: " + p2,font="big")
    elif p1 == "O":
        p2 = "X"
        tprint("Player2: " + p2,font="big")
    elif p1 != "O" or p1 != "X":
        tprint("Sorry,invalid input. Type X or O",font="big")
        startGame()

def player_position():
    global current_player
    tprint("Current Player: " + current_player,font="big")
    artInput = text2art("Choose position from 1 - 9: ",font="soft" )
    position = input(artInput)

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            artInput = text2art("Choose position from 1 - 9: ",font="soft" )
            position = input(artInput)
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            tprint("Position already selected, choose another position!",font="big")
    board[position] = current_player
    display_board()

def startGame():
    tprint("\nWelcome to Tic Tac Toe",font="big",decoration="star23")
    display_board()
    players()
    
    while game_on:
        player_position()
        
        def check_winner():
            global game_on
            point = 0
            #Check rows if there is a win 
            if board[0] == board[1] == board[2] != "-":
                game_on = False
                tprint("\nCongratulations " + board[0]+" you WON!",font="big",decoration="star23")
            elif board[3] == board[4] == board[5] != "-":
                game_on = False
                point = 1
                return 1
                tprint("\nCongratulations " + board[3]+" you WON!",font="big",decoration="star23")
            elif board[6] == board[7] == board[8] != "-":
                game_on = False
                point = 1
                return 1
                tprint("\nCongratulations " + board[6]+" you WON!",font="big",decoration="star23")
             #Check columns if there is a win
            elif board[0] == board[3] == board[6] != "-":
                game_on = False
                point = 1
                return 1
                tprint("\nCongratulations " + board[0]+" you WON!",font="big",decoration="star23")
            elif board[1] == board[4] == board[7] != "-":
                game_on = False
                point = 1
                return 1
                tprint("\nCongratulations " + board[1]+" you WON!",font="big",decoration="star23")
            elif board[2] == board[5] == board[8] != "-":
                game_on = False
                point = 1
                return 1
                tprint("\nCongratulations " + board[2]+" you WON!",font="big",decoration="star23")
             #Check diagonals if there is a win
            elif board[0] == board[4] == board[8] != "-":
                game_on = False
                point = 1
                return 1
                tprint("\nCongratulations " + board[0]+" you WON!",font="big",decoration="star23")
            elif board[2] == board[4] == board[6] != "-":
                game_on = False
                point = 1
                return 1
                tprint("\nCongratulations "+ board[6]+" you WON!",font="big",decoration="star23")
             #Check if it's a tie
            elif "-" not in board:
                game_on = False
                point = 0
                tprint("\nIt's a Tie",font="big",decoration="star23")
                return 0
            Users.addPoints(Users.get_userID(),point)    

        def flip_player():
            global current_player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        flip_player()
        if check_winner() == 0:
            break
        else:
            continue
        
