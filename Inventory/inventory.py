
from Inventory.Items import items
from art import *
from stringcolor import * 


class Service:

     
    def __init__(self):
        self.list_items = []
        self.Display()

    def Display(self):
        tprint("Inventory")
        while True:
            print(15*"-")
            print("input 1  to List items :")
            print("input 2  to Add items :")
            print("input 3  to Delete items :")
            print("input 4  to Edit items :")
            print("input 5  to check :")
            print(20*"-")
            try:
                Choose = int(input("Please Choose Number : "))
                print(15*"-")
                if Choose < 0 or Choose >  5 :
                    print(cs("Please check the entry ! ", "#ff0009"))
                if Choose == " ":
                    print("Please check the entry ! ")
                else:
                    if Choose == 1:
                        self.Display_Items()
                    elif Choose == 2:
                        self.add()
                    elif Choose == 3:
                        self.delete()
                    elif Choose ==4:
                        self.Edit()
                    elif Choose ==5:
                        self.Minimum_Check()
            except ValueError:
                print()
                print(cs("input Error , must be integer between 1 to 5 !", "#ff0009") )
                print()
#-------------------------------------Function to display list of items

    def Display_Items(self):
        print("Inventory Items =>")
        if not self.list_items:
            print()
            print(cs("Their is not items in Store ", "#ff0009"))
            print()
            self.add()
        else:
            print()
            for _items in self.list_items:
             print(cs(f"Name : {_items.getName()} | Sequence : {_items.getSequence()} | Quantity : {_items.getQuantity()}", "DeepPink3"))
             print()
            self.add()
#-------------------------------------Function to add items to the list

    def add(self):
        x = 1 
        while True:
            try:
                input_user = input(cs("Do you want to add items ? y or n   : ", "#ffff87"))
                print()
            except Exception as e:
                print(cs("Error The input value type is invalid", "#ff0009" , e.__doc__))
            try:
                if input_user == "y":
                    print(" ")
                    name = input(f"Name of item {x} : ")
                    sequence = int(input("Sequence of item : "))
                    quantity = int(input("Quantity : "))
                    self.list_items.append(items(name ,sequence, quantity))
                    print(cs("Added successfully ","#00d787"))
                    print()
                    x = x + 1
            except ValueError as e:
                    print(cs("Error The input value type is invalid", "#ff0009") , e.__doc__)
                    print(cs("Failed to add ", "#ff0009"))
                    print("-----------")
            if input_user == "n":
                    self.Display()
                    
            return  self.list_items
#-------------------------------------Function to delete one item from the list

    def delete(self):
        try:
            item_Sequence = int(input("Enter The Sequence of item to delete : "))
            item_index = ""
            for i, item in enumerate(self.list_items):
                if item.getSequence() == item_Sequence:
                    item_index = i
            del self.list_items[item_index]
            print()
            print(cs("The item has been deleted successfully ","#00d787"))
        except ValueError :
             print("Error The input value type is invalid (Delete)")
            #self.list_items.remove(items.setName(item))
            #list_1 = list(filter(lambda _list : _list not in item ,self.list_items))
            #return  list_1     
 #--------------------------------------function to modify name of one item from the list

    def Edit(self):
        try:
            item_New_name = ""
            item_name = input("Enter The name of item to edit : ")
            # if item_name == " ":
            #         print("Please check the entry ! ")
            # else:
            newItemName = input("enter new name : ") 
            for _item in self.list_items:
                if _item.getName() == item_name :
                    item_New_name = newItemName
                    _item.setName(item_New_name)
                    print(cs("Modified successfully ","#00d787"))
                    break
            else:
                    print(cs("this item is not found ", "#ff0009"))
        except ValueError :
             print("Error The input value type is invalid (Edit)")  
#-------------------------------------------Function to check minimum stock for items that have less than 5 items

    def Minimum_Check(self):
            for item in self.list_items:    
                if item.getQuantity() < 5:
                    print(cs(f"Name : {item.getName()} Quantity : {item.getQuantity()} ," " Exceeding the minimum stock ", "#ff0009"))
                    self.purchase_requests()
#-------------------------------------------Function to send (purchase request) from inventory to purchases        
#        
    def purchase_requests(self)-> list:
        print("-------------------------")
        while True:
            try:
                user_input =input("Do you need send Purchase Requests ? y or n ")
                print("___________________")
                if user_input == 'y':
                    new_pr = input("type in new PR  : ")
                    file = open('NewPR.txt', 'a+' , encoding='utf-8')
                    file.write(f"Purchase Requests : {new_pr} \n")
                    file.close()
                    print(cs("Added successfully ","#00d787"))
                elif user_input == 'n':
                    self.Display_Items()
                    break
            except ValueError :
                print("Error The input value type is invalid (PR)")
    
        self.Minimum_Check()





















