from Inventory.inventory import Service
from purchases.purchseServ import PurchaseOrder
from art import *

tprint("Welcome to the inventory management",font="cybermedum")
def main():
    user_input = 0
    try:
        user_input = int(input("- Enter 1 to open Inventory or 2 to open Purchases : "))
        if user_input == 1:
            Service()      
        elif user_input == 2:
            PurchaseOrder()
        else:
            print("Please Enter 1 or 2  : ")
    except ValueError:
        print("Input must be integer ! ")
main()
