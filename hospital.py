import hospital
from colour_text import*
ct = ColourText()
ct.initTerminal()
class the_hospital_system:
    languge=input(" welcome to hosptial system put start to contunio  :")
    if languge=="start":
     print(ct("<>blue welcome to the patient registry<>"))
     
    
    def __init__(self,name:str,family_name:str,ID_number:int,file_number:int,kind:str,phone_number:int):
        self.__name=name
        self.__famliy_name=family_name
        self.__ID_number=ID_number
        self.__file_number=file_number
        self.__kind=kind
        self.__phone_number=phone_number
        self.__vistor_city= {'ryidah':56,"abha":20,"jaddah":36}
    
    def get_description(self):
        return f"\nWELCOME TO HOSPITAL THE Patient data:\n  \nthe name\n  \n {self.__name}\n  \nthe fmaily name\n  \n{self.__famliy_name}\n \nthe ID number is\n \n{self.__ID_number}\n \nthe kind is\n \n{self.__kind}\n \nthe phone number is\n \n{self.__phone_number}\n "
    
    def get_name(self):
        return self.__name

    def get_family_name(self):
        return self.__famliy_name
    
    def get_ID_number(self):
        return self.__ID_number

    def get_phone_number(self):
        return self.__phone_number

    def get_kind(self):
        return self.__kind

    def get_file_number(self):
        return self.__file_number

    def get_vistor_city(self):
        return self.__vistor_city

    

    def set_file_number(self, file_number):
        self.__file_number = file_number
    
    def set_kind(self, kind):
        self.__kind = kind
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    
    
 



            




   
    
            




 

    

        
    

