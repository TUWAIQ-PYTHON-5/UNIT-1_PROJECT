from art import *
from colorama  import *
import emoji



# HERE WE CALL THE GAME TO START 

user_name= ""
user_answer= ""

def greeting()-> str:
    print(emoji.emojize(":person_raising_hand:"))
    user_name = input('Hey There ! , Please Enter your Name: ')
    try:
        if not user_name.isalpha() or user_name == '':
            raise ValueError('input must be string ! ')
    except ValueError as e:
        print(f'Error , please enter your name : {e}')

    else:
        hello =text2art( "Welcome to TicTacToe Game ! " , font='small',chr_ignore=True)
        UserNameDesign =text2art(  user_name , font='small',chr_ignore=True)
        print(Fore.BLUE + hello  , Fore.GREEN + UserNameDesign   )
    



greeting()


# ask the user if want to play or not 
#_______________________________________________

while True:
    user_answer=input("Would you Like to Play TicTacToe with me ? if your answer is yes , you can choose your player (X,O) or exit to end ." )
    if user_answer.lower() == "X" and "O":
        from TicTacToe import start_new_game 
        break
    elif user_answer.lower() == 'exit' :
        print(Fore.RED + "Ohh that's bad 😥 , nice to know you tho !!", emoji.emojize(":handshake:"))
        break
    else:
        print('Please enter a valid input ! ')


    
#_______________________________________________






