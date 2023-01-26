import classes_menu
from colorama import Fore, Back, Style
from art import *
from stringcolor import * 


def intro():
    title1=(Fore.BLUE + "Healthy food , Happy mood :D")
    title2 = (Style.DIM+"Healthy food restaurant")
    tprint("Healthy food , Happy mood :D",font="cybermedum")
    print(Style.RESET_ALL)
    a = title1.center(90)
    b = title2.center(90)
    print(a)
    print(b)
    print("\t\t\t---------------------------------------------")

# Start of the program
user_input = ''
num = 0
intro()
# While for Error Handling :
while True:
    try:
        user_input = input(cs("\tWelcome to our resturant , please enter 1 to disply the menu :", "Wheat", "White"))
        user_input = int(user_input)

        while user_input != 4:
        
        # while for choose :
            print(Style.RESET_ALL + "Choose from the menu your diet:")
            print("\t1. keto diet ")
            print("\t2. Cutting diet")
            print("\t3. Bulking diet ")
            print("\t4. EXIT")
            user_input = input(underline("\tSelect what you want from (1-4), So let's start : "))
        
        # If the user choose number 1
            if user_input == '1':

                # Objects :
                print(cs("* Note : Keto diet : 1300 cal .", "red", "White"))
                menu_item1 = classes_menu.keto('beef 200 g + rice 50g + 30 fat ', '433 Calories', 35)
                menu_item2 = classes_menu.keto('salmon 200g + rice 50g +30 fat', '433 Calories', 40)
                menu_item3 = classes_menu.keto('salmon 200g + salad + 30 fat ', '433 Calories', 30)
                menu_item4 = classes_menu.keto('Orange Juice', '30 cal', 15)
                menu_item5 = classes_menu.keto('Diet Pepsi ', '0 cal', 5)

                menu_items = [menu_item1, menu_item2, menu_item3, menu_item4, menu_item5]

                index = 0
                # For to print all index :

                for menu_item in menu_items:
                    print(str(index) + ' - ' + menu_item.info())
                    index += 1

                print('--------------------')

                order = int(input(underline('Enter menu item number: ')))
                selected_menu = menu_items[order]
                print('Selected item: ' + selected_menu.name ," : $ " , selected_menu.price)

                # Receive input from user :
                side_dish_index = int(input(underline('Enter another meal or drink :')))

                # Sum two index from user : 

                side_dish = menu_items[side_dish_index]
                result = (selected_menu.price + side_dish.price) 

                # Output 'Your total is $' :
                print('Your total is $' + str(result))
                print(cs("\tThanks for using Healthy food, Happy mood :D and come back again.", "Wheat", "White"))

                print(cs("..We are glad you invested in yourself, keep going..", "Wheat", "White"))
                break

        # If the user choose number 2

            elif user_input == '2':
                print(cs("* Note : Cutting diet : 1200 cal . ", "red", "White"))
                menu_item1 = classes_menu.Cutting('chicken 150 g + rice 100 g + 5 fat ', '400 Calories ', 26)
                menu_item2 = classes_menu.Cutting('chicken 150 g + Pasta 150 g + 3 fat', '400 Calories ', 20)
                menu_item3 = classes_menu.Cutting('beef 150 g + rice 150 g + 3 fat ', ' 400 Calories', 30)
                menu_item4 = classes_menu.Cutting('Orange Juice', '30 Calories', 15)
                menu_item5 = classes_menu.Cutting('Diet Pepsi ', '0 Calories', 5)
                menu_items = [menu_item1, menu_item2, menu_item3, menu_item4, menu_item5]
                
                index = 0
                for menu_item in menu_items:
                    print(str(index) + ' - ' + menu_item.info())
                    index += 1

                print('--------------------')
                
                order = int(input(underline('Enter menu item number: ')))
                selected_menu = menu_items[order]
                print('Selected item: ' + selected_menu.name ," : $ " , selected_menu.price)
                
                side_dish_index = int(input(underline('Enter another meal or drink :')))

                side_dish_index = lambda x , y : selected_menu.price + side_dish.price
                side_dish = menu_items[side_dish_index]
                print(side_dish)
            
                print('Your total is $' + str(result))
                print(cs("\tThanks for using Healthy food, Happy mood :D and come back again.", "Wheat", "White"))

                print(cs("..We are glad you invested in yourself, keep going..", "Wheat", "White"))
                break

        # If the user choose number 3

            elif user_input == '3':
                print(cs("* Note : Bulking diet : 1800 cal .", "red", "White"))
                menu_item1 = classes_menu.Bulking('chicken 200 g + rice 200 g + 5 fat ', '600 Calories', 26)
                menu_item2 = classes_menu.Bulking('chicken 200g + Pasta 200 g +30 fat', '600 Calories', 40)
                menu_item3 = classes_menu.Bulking('beef 200g + rice 200 g + 3 fat ', '600 Calories', 30)
                menu_item4 = classes_menu.Bulking('Orange Juice', '30 Calories', 15)
                menu_item5 = classes_menu.Bulking('Diet Pepsi ', '0 Calories', 5)
                menu_items = [menu_item1, menu_item2, menu_item3, menu_item4, menu_item5]

                index = 0
                for menu_item in menu_items:
                    print(str(index) + ' - ' + menu_item.info())
                    index += 1

                print('--------------------')
                order = int(input(underline('Enter menu item number: ')))
                selected_menu = menu_items[order]
                print('Selected item: ' + selected_menu.name ," : $ " , selected_menu.price)

                side_dish_index = int(input(underline('Enter another meal or drink :')))
                side_dish = menu_items[side_dish_index]
                result = (selected_menu.price + side_dish.price) 

                print('Your total is $' + str(result))
                print(cs("\tThanks for using Healthy food, Happy mood :D and come back again.", "Wheat", "White"))

                print(cs("..We are glad you invested in yourself, keep going..", "Wheat", "White"))
                break

        # If the user choose number 4

            elif user_input == '4':
                print(cs("\tThanks for using Healthy food, Happy mood :D and come back again.", "Wheat", "White"))
            
            else:
                print("Invalid choice")

            user_input = input("Enter your choice : ")

    except ValueError:
        print("No valid Enter! Must be integer, Please try again ...")
