
from tkinter import *
import random 


x_score = 0
o_score = 0


def next_turn(row,col):
    global player, x_score, o_score
    if game_buttons[row][col]["text"]== "" and check_winner()== False:
        if player== players[0]:

            game_buttons[row][col]["text"]=player

            if check_winner() == False :

                player=players[1]
                label.config(text=(players[1] + " turn "))

            elif check_winner() == True :
                x_score += 1
                label.config(text=(players[0] + " Winner !! "))
            
            
            elif check_winner() == "Tie " :
                label.config(text=(" No Winner :( "))



        elif player== players[1]:
            game_buttons[row][col]["text"]=player
            
            
            if check_winner() == False :
                player=players[0]
                label.config(text=(players[0] + " turn "))

            elif check_winner() == True :
                o_score += 1
                label.config(text=(players[1] + " Winner !! "))
            
            
            elif check_winner() == "Tie " :
                label.config(text=( " No Winner :( "))

def check_winner():
    for row in range (3):
        if game_buttons[row][0]["text"]== game_buttons[row][1]["text"] == game_buttons[row][2]["text"]  != "":
            game_buttons[row][0].config(bg="green")
            game_buttons[row][1].config(bg="green")
            game_buttons[row][2].config(bg="green")

            return True

    for col in range (3):
        if game_buttons[0][col]["text"]== game_buttons[1][col]["text"] == game_buttons[2][col]["text"]  != "":
            game_buttons[0][col].config(bg="cyan")
            game_buttons[1][col].config(bg="cyan")
            game_buttons[2][col].config(bg="cyan")

            return True


    if game_buttons[0][0]["text"]== game_buttons[1][1]["text"] == game_buttons[2][2]["text"]  != "":
            game_buttons[0][0].config(bg="red")
            game_buttons[1][1].config(bg="red")
            game_buttons[2][2].config(bg="red")
            return True

    elif game_buttons[0][2]["text"]== game_buttons[1][1]["text"] == game_buttons[2][0]["text"]  != "":
            game_buttons[0][2].config(bg="blue")
            game_buttons[1][1].config(bg="blue")
            game_buttons[2][0].config(bg="blue")
            return True

    if check_empty_space()==False :
        for row in range (3):
            for col in range(3):
                game_buttons[row][col].config(bg = "yellow")

        return "Tie , no winners for this day *-* "

    else :

        return False 


def check_empty_space():
    spaces = 9 

    for row in range(3):
        for col in range(3):
            if game_buttons[row][col]["text"] != "":
                spaces-= 1 
    if spaces == 0 :
        return False 

    else :
        return True 


def start_new_game():
    global player 
    player = random.choice(players)

    label.config (text=(player + " Turn "))
    for row in range (3):
        for col in range(3):
            game_buttons[row][col].config(text= "",bg="#e9b9ff")



window = Tk()
window.title("TicTacToe")

players = ["x","o"]
player = random.choice(players)
game_buttons = [
[0,0,0], 
[0,0,0], 
[0,0,0]
]
label = Label(text =(player+ " turn "), font=("consolas", 40))
label.pack(side="top")
restart_button = Button(text = "Restart ", font=("consolas", 20), command=start_new_game)
restart_button.pack(side="top")

button_frame = Frame(window)
button_frame.pack()

for row in range (3):
    for col in range(3):
        game_buttons[row][col] = Button(button_frame,text="", font=("consolas", 50) , width=4 , height=1,command= lambda row=row ,col=col: next_turn (row,col))
        game_buttons[row][col].grid(row=row,column=col)


window.mainloop()



print("          THE SCORES BORD           ")
print("************************************")
print("X ", "       =          " , x_score )
print("O ", "       =          " , o_score )
print("************************************")


# players scores in CLI 
#______________________________________________
def checkWinner():
    global x_score, o_score
    if x_score > o_score :
        print("Good Work X !! , You are the winner  ")
        print("************************************")
        x_score += 0 

    elif o_score >  x_score:
        print("Winner Winner Checken Dinner , O is winning !  ")
        print("************************************")
        o_score += 0  
    else  : 
        print(" Oops it's a Tie *-*" )
        print("************************************")
        
    return (x_score , o_score)


checkWinner()

