

class User():
    def __init__(self,First_name:str,Last_name:str,Email:str,Number: int):
        self.First_name=First_name
        self.Last_name=Last_name
        self.Email=Email
        self.Number=Number
    
    def info(self):

        return f"Welcome to our program {self.First_name} {self.Last_name}"



