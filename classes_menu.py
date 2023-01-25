class keto:
    type = "keto diet" 

    def __init__(self, name : str, Calories : str ,price : int ) -> None:
        self.name = name
        self.price = price
        self.Calories = Calories

#Methods : 

    def info(self):
        return self.name + ' : ' +  self.Calories + ' : $ ' + str(self.price)

# SubClasses  : 

class Cutting (keto) :
    type = "Cutting diet"

    def __init__(self, name : str,Calories : str ,  price : int ):
        super().__init__(name, Calories ,price)

    def info(self):
        return self.name + ' : ' + self.Calories + ' : $ ' + str(self.price)


class Bulking (keto) :
    type = "Bulking diet" 

    def __init__(self, name : str,Calories : str ,  price : int ):
       super().__init__(name, Calories ,price)

    def info(self):
        return self.name + ' : ' + self.Calories + ' : $ ' + str(self.price)



