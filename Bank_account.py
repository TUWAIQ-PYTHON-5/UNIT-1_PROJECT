from datetime import datetime
Now=datetime.now()
class User_Information :
    def __init__(self,name :str, phone_number : int ,id :int):
        self.__name=name
        self.__phone_number=phone_number
        self.__id =id
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_phon_number(self, phone_number):
        self.__phone_number = phone_number
    def get_phone_number(self):
        return self.__phone_number
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    def new_account(self):
         if len(self.__phone_number)==10 and len(self.__id)==10 :
            return self.get_phone_number(),self.get_id()
         else:
            return f"the number must be 10 digits {self.__name} try again"

class Atm(User_Information):
    def __init__(self,balance_amount: int):
        self.balance_amount=balance_amount


    def deposit(self, amount:int):
        self.balance_amount += amount
        print(f"account balance has been updated: {self.balance_amount} in ",Now.strftime("%m/%d/%Y, %H:%M:%S"))
    def withdraw(self, amount_withdraw):
        if amount_withdraw > self.balance_amount:
            print("insufficient funds")
        else:
            self.balance_amount-=amount_withdraw
            print(f"account balance has been updated:-{amount_withdraw} in ",Now.strftime("%m/%d/%Y, %H:%M:%S"))

    def balance(self):
        print(f"these your current account: {self.balance_amount} ")










