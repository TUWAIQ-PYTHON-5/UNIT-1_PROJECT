class Record :
    def __init__(self, name,staff, branches, month1, month2, month3, month4, month5, month6, month7, month8, month9, month10, month11, month12) :
        self.__resturant_name = name
        self.__staff = staff
        self.__branches = branches
        self.__jan_sales = month1
        self.__feb_sales = month2
        self.__march_sales = month3
        self.__april_sales = month4
        self.__may_sales = month5
        self.__jun_sales = month6
        self.__july_sales = month7
        self.__aug_sales = month8
        self.__sep_sales = month9
        self.__oct_sales = month10
        self.__nov_sales = month11
        self.__dec_sales = month12

    def set_resturant_name(self, name) :
        self.__resturant_name = name

    def set_staff(self, staff) :
        self.__staff = staff

    def set_branches(self, branches) :
        self.__branches = branches

    def set_jan_sales (self, sales) :
        self.__jan_sales = sales

    def set_feb_sales (self, sales) :
        self.__feb_sales = sales

    def set_march_sales (self, sales) :
        self.__march_sales = sales
    
    def set_april_sales (self, sales) :
        self.__april_sales = sales
    
    def set_may_sales (self, sales) :
        self.__may_sales = sales
    
    def set_jun_sales (self, sales) :
        self.__jun_sales = sales
    
    def set_july_sales (self, sales) :
        self.__july_sales = sales
    
    def set_aug_sales (self, sales) :
        self.__aug_sales = sales

    def set_oct_sales (self, sales) :
        self.__oct_sales = sales
    
    def set_nov_sales (self, sales) :
        self.__nov_sales = sales
    
    def set_dec_sales (self, sales) :
        self.__dec_sales = sales

    def get_resturant_name(self) :
        return self.__resturant_name

    def get_staff(self) :
        return self.__staff 

    def get_branches(self) :
        return self.__branches

    def get_jan_sales(self) :
        return self.__jan_sales
    
    def get_feb_sales(self) :
        return self.__feb_sales

    def get_march_sales(self) :
        return self.__march_sales
    
    def get_april_sales(self) :
        return self.__april_sales

    def get_may_sales(self) :
        return self.__may_sales
    
    def get_jun_sales(self) :
        return self.__jun_sales

    def get_july_sales(self) :
        return self.__july_sales
    
    def get_aug_sales(self) :
        return self.__aug_sales

    def get_sep_sales(self) :
        return self.__sep_sales
    
    def get_oct_sales(self) :
        return self.__oct_sales

    def get_nov_sales(self) :
        return self.__nov_sales

    def get_dec_sales(self) :
        return self.__dec_sales



def add_resturant():
    resturant_name = input("Enter the resturant name: ")
    if type(resturant_name) != str :
        raise TypeError("Only String are allowed")
    staff = int(input("Enter the staff number: "))
    if type(staff) != int :
        raise TypeError("Only integers are allowed")
    branches = int(input("Enter the branches number: "))
    if type(branches) != int :
        raise TypeError("Only integers are allowed")
    month1 = int(input("Enter January sales : ") )
    if type(month1) != int :
        raise TypeError("Only integers are allowed")
    month2 = int(input("Enter February sales : "))
    if type(month2) != int :
        raise TypeError("Only integers are allowed")
    month3 = int(input("Enter March sales : "))
    if type(month3) != int :
        raise TypeError("Only integers are allowed")
    month4 = int(input("Enter April sales : "))
    if type(month4) != int :
        raise TypeError("Only integers are allowed")
    month5 = int(input("Enter May sales : "))
    if type(month5) != int :
        raise TypeError("Only integers are allowed")
    month6 = int(input("Enter June sales : "))
    if type(month6) != int :
        raise TypeError("Only integers are allowed")
    month7 = int(input("Enter July sales : "))
    if type(month7) != int :
       raise TypeError("Only integers are allowed")
    month8 = int(input("Enter August sales : "))
    if type(month8) != int :
        raise TypeError("Only integers are allowed")
    month9 = int(input("Enter September sales : "))
    if type(month9) != int :
        raise TypeError("Only integers are allowed")
    month10 = int(input("Enter October sales : "))
    if type(month10) != int :
        raise TypeError("Only integers are allowed")
    month11 = int(input("Enter November sales : "))
    if type(month11) != int :
        raise TypeError("Only integers are allowed")
    month12 = int(input("Enter December sales : "))
    if type(month12) != int :
        raise TypeError("Only integers are allowed")
    new_resturant = Record(resturant_name,staff, branches, month1, month2, month3, month4, month5, month6, month7, month8, month9, month10, month11, month12)
    file = open("resturants.txt", "a", encoding="utf-8")
    file.write(f"{new_resturant.get_resturant_name()},{new_resturant.get_staff()},{new_resturant.get_branches()},{new_resturant.get_jan_sales()},{new_resturant.get_feb_sales()},{new_resturant.get_march_sales()},{new_resturant.get_april_sales()},{new_resturant.get_may_sales()},{new_resturant.get_jun_sales()},{new_resturant.get_july_sales()}, {new_resturant.get_aug_sales()},{new_resturant.get_sep_sales()},{new_resturant.get_oct_sales()},{new_resturant.get_nov_sales()},{new_resturant.get_dec_sales()} \n")
    file.close()

# add_resturant()



