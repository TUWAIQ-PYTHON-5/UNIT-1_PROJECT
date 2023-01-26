class ProductCar:
  def __init__(self,selectedCategory, cart, phone_number,location):
    self.cart = cart
    self.selectedCategory = selectedCategory
    self.phone_number = phone_number
    self.location = location
    self.categories = {
          "Eyes" : {"Eyeliner" : 23 , "Mascara" : 34 ,"Eyeshado": 55 },
          "Face" : {"Foundation" : 44 , "Blusher" : 17 , "Powder" : 56 },
          "lip"  : {"Rouge" : 45 , "Lip gloss" : 45 }
    }
    #Use some form of Error Handling 
    # Use functions that return an output
  def calculatePrice(self):
     try:
        products = self.categories[self.selectedCategory]
        total = 0
        for cat in self.cart:
            total += products[cat]
        return f'total price :{ str(total)}  SAR\n your phone number :\n {self.phone_number} \nyour location :\n {self.location}' 
      
     except:
           return "You have a mistake because you did not put anything in the basket"

 