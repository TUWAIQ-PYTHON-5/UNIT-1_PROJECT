from purchases.Providers import Provider
from art import *
from stringcolor import * 


class PurchaseOrder:

    def __init__(self):
        self.provider_list = []
        self.Display()
#----------------------------------------function to display the options available in the purchase program

    def Display(self):
        tprint("Purchase")
        while True:
            print(15*"-")
            print("input 1  to Display PR :")
            print("input 2  to Create provider :")  
            print("input 3  to Display provider :")  
            print("input 4  to Exit :")  
            print(20*"_")
            try:
                Choose = int(input("Please Choose Number : "))
                print(15*"-")
                if Choose < 0 or Choose >  4 :
                    print(cs("Please check the entry ! ", "#ff0009"))
                if Choose == " ":
                    print(cs("Please check the entry ! ", "#ff0009"))
                else:
                    if Choose == 1:
                        self.Display_Purchaser_requests()
                    elif Choose == 2:
                        self.Create_provider()             
                    elif Choose == 3:
                        self.Display_providers()            
                    elif Choose == 4:
                        break           
            except ValueError:
                print()
                print(cs("input Error , must be integer between 1 to 5 !", "#ff0009"))
                print()
#-------------------------------------- function to display purchase requests sent from the store
    def Display_Purchaser_requests(self):
        #show_list = input("do you want to Display Purchase Requests ?  : ")
        #if show_list == 'y':
        files = open('NewPR.txt' , 'r', encoding='utf-8') 
        print(files.read())
        files.close()
        self.Receive_orders()
#----------------------------------- Function to display available providers
    def Display_providers(self):
        print("Inventory Items =>")
        if not self.provider_list:
            print(cs("Their is not providers", "#ff0009"))
            self.add()
        else:
            print()
            for _items in self.provider_list:
                print(cs(f"Name : {_items.get_name()} | Emile : {_items.get_email()} | Phone : {_items.get_phone()}", "DeepPink3"))
                print()
                self.Display()
#-------------------------------------function to creating providers and saving them in a file
    def Create_provider(self):
        x = 1 
        while True:
            try:
                input_user = input(cs("Do you want to Create Provider ? y or n : ", "#ffff87"))
            except Exception as e:
                print(cs("Error The input value type is invalid", "#ff0009" , e.__doc__))
            try:
                if input_user == "y":
                    print(" ")
                    provider_name = input(f"Name of provider {x} : ")
                    email = input("Email of provider : ")
                    description = input("Phone : ")
                    self.provider_list.append(Provider(provider_name ,email, description))
                    print(cs("Added successfully ","#00d787"))
                    print()
                    x = x + 1
                elif input_user == "n":
                    self.Display()
            except ValueError as e:
                    print(cs("Error The input value type is invalid", "#ff0009") , e.__doc__)
                    print(cs("Failed to add ", "#ff0009"))
                    print("-----------")
            break
        return  self.provider_list
 #--------------------------------------------function to confirm and send purchase orders       

    def Receive_orders(self):
        email = ""
        phone = ""
        try:
            while True:
                user_input =input("Do you want confirm and send Purchase Order ? y or n : ")
                if user_input == 'y':
                    provider_name = input("Enter provider Name : ")
                    new_po = input("Type new PO  : ")
                    for info in self.provider_list:
                        if info.get_name() ==  provider_name:
                            email = info.get_email()
                            phone = info.get_phone()
                            file = open('NewPO.txt', 'a+' , encoding='utf-8')
                            file.write(f"Provider : {provider_name} - Emil : {email} - Phone : {phone} -> {new_po} \n")
                            file.close()
                            print(cs("Send successfully ","#00d787"))
                elif user_input == 'n':
                    break
            self.Display()               
        except ValueError :
             print(cs("Error The input value type is invalid (Sent PO)"), "#ff0009")

    

