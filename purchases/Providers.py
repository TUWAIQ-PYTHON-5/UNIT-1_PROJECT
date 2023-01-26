
class Provider:
    def __init__(self , provider_name , email, phone):
        self.__provider_name = provider_name
        self.__email = email
        self.__phone = phone
        

    def set_name(self , provider_name):
        self.__provider_name = provider_name

    def get_name(self):
        return self.__provider_name  

    def set_email(self , email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_phone(self , phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone

    
