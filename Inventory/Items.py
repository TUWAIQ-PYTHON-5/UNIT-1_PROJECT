
class items:
    def __init__(self , name , sequence , quantity):
        self.__name = name
        self.__sequence = sequence
        self.__quantity = quantity
        

    def setName(self , name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSequence(self , sequence):
        self.__sequence = sequence

    def getSequence(self):
        return self.__sequence

    def setQuantity(self , quantity):
        self.__quantity = quantity

    def getQuantity(self):
        return self.__quantity

    
 
