from colorama import Fore, Back, Style
from art import *
import methodes
import Resturant_data

print(Back.WHITE )
print(Fore.BLACK)
tprint("WELCOMe",font="block")
print(Style.RESET_ALL)
tprint("Resturants  Analysis  Tool ",font="standerd")


print("To display resturants names enter 1 :")
print("For sales information enter 2 :")
print("To display all resturants details enter 3 :")
print("To add a new resturant enter 4 : ")
print("To exit enter 0 : ")
selection = int(input("Your selection :"))
try :
    while selection != 0 :

        if selection == 1 :
            print("")
            print("--"*20)
            for resturant in methodes.resturants_names() :
                print(f"{resturant} \t", end="")
        elif selection == 2 :
            print("")
            print("--"*20)
            tprint("Sales Section ",font="standerd")
            print("To display total sales for every resturant enter 1:")
            print("To display first quarter sales for every resturant enter 2:")
            print("To display seconde quarter sales for every resturant enter 3:")
            print("To display third quarter sales for every resturant enter 4:")
            print("To display fourth quarter sales for every resturant enter 5:")
            print("To display all sales details enter 6:")
            print("To go back enter 0:")
            selection2 = int(input("Your selection :"))
            while selection2 != 0 :
                print("")
                print("--"*20)
                if selection2 == 1 :
                    methodes.totalـsales()
                elif selection2 ==2 :
                    quarter_1_sales = methodes.first_quarter_sales()
                    resturants_names = methodes.resturants_names()
                    for i in range(0,len(resturants_names)):
                        print(f"{resturants_names[i]}: {quarter_1_sales[i]}")
                elif selection2 ==3 :
                    quarter_2_sales = methodes.seconde_quarter_sales()
                    resturants_names = methodes.resturants_names()
                    for i in range(0,len(resturants_names)):
                        print(f"{resturants_names[i]}: {quarter_2_sales[i]}")
                elif selection2 ==4 :
                    quarter_3_sales = methodes.third_quarter_sales()
                    resturants_names = methodes.resturants_names()
                    for i in range(0,len(resturants_names)):
                        print(f"{resturants_names[i]}: {quarter_3_sales[i]}")
                elif selection2 ==5 :
                    quarter_4_sales = methodes.fourth_quarter_sales()
                    resturants_names = methodes.resturants_names()
                    for i in range(0,len(resturants_names)):
                        print(f"{resturants_names[i]}: {quarter_4_sales[i]}")
                elif selection2 ==6 :
                    methodes.sales_details()
                print("")
                print("--"*20)
                tprint("Sales Section ",font="standerd")
                print("To display total sales for every resturant enter 1:")
                print("To display first quarter sales for every resturant enter 2:")
                print("To display seconde quarter sales for every resturant enter 3:")
                print("To display third quarter sales for every resturant enter 4:")
                print("To display fourth quarter sales for every resturant enter 5:")
                print("To display all sales details enter 6:")
                print("To go back enter 0:")
                selection2 = int(input("Your selection :"))
                

        elif selection == 3 :
            methodes.all_details()
        elif selection == 4 :
            Resturant_data.add_resturant()
        elif selection == 5 :
            pass
        
        print("")
        print("--"*20)
        print("To display resturants names enter 1 :")
        print("For sales information enter 2 :")
        print("To display all resturants details enter 3 :")
        print("To add a new resturant enter 4 : ")
        print("To exit enter 0 : ")
        selection = int(input("Your selection :"))
    else :
        tprint("Thank You For Using Our Tool",font="standerd")
        
except TypeError :
    print("There was an error",TypeError)
except Exception as error:
    print("There was an error", error.__class__)








