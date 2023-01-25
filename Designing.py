from art import *
from colorama  import *


# HERER WE CALL THE GAME TO START 

user_name= ""
user_answer= ""

def greeting()-> str:

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
    user_answer=input("Hello,  Would you Like to Play TicTacToe with me ? (Y/N) " )
    if user_answer.lower() == 'y':
        from TicTacToe import start_new_game 
        break
    elif user_answer.lower() == 'n':
        print(Fore.RED + "oh that's bad :( , nice to know you tho !! ^-^ " )
        break
    else:
        print('Type Y/N')


    
#_______________________________________________






