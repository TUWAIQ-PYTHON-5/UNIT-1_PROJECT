import Products


#information [ Glow Your Face ]
name = input("what is your name?")
print("welcome ... to Glow Your Face ... " ,name)
name_want =print("we are a makeup store that offers everything related to the face")
answer = input("if you want to start shopping please type ?  (yes) if not  type (no) ")

phone_number = input("please write your phone number ")
print("Please complete your information")

location = input("Please specify your location")


Email = input("Enter your Email")
print("We are honored to have you in our store <3 ")


# Use lists or dictionaries
list1 = ["Eyes", "Face", "lip"]
if answer == "yes" :
   print(list1)
else :
   print('Thanks for visiting our store')
   exit()

answer_category = input("please type the category that you want to preview the products >>> ")

Eyes = {"Eyeliner" : 23 , "Mascara" : 34 ,"Eyeshado": 55 }

Face = {"Foundation" : 44 , "Blusher" : 17 , "Powder" : 56 }

lip = {"Rouge" : 45 , "Lip gloss" : 45 }

categories = {
      "Eyes" : Eyes,
      "Face" : Face,
      "lip"  : lip
}
#Use loops .....
for cat in categories:
    if cat == answer_category :
       print(categories[answer_category])


selectProduct = input('please type the product to add to cart : >>>> ')

cartProducts = []
cartProducts.append(selectProduct)
print(cartProducts)

answerToContinue = input('If you want to continue shopping type (yes) or exit and print receipt (no) ')
if answerToContinue == 'yes' :
   print(categories[answer_category])
   selectProduct2 = input('please type the product to add to cart : >>>> ')
   cartProducts.append(selectProduct2)
   print(cartProducts)
else :
       print(cartProducts)
       obj1 = Products.ProductCar(answer_category, cartProducts, phone_number,location)
       print(obj1.calculatePrice())
       exit()


answerToContinue2 = input('If you want to continue shopping type (yes) or exit and print receipt (no) ')
if answerToContinue2 == 'yes' :
   print(categories[answer_category])
   selectProduct3 = input('please type the product to add to cart : >>>> ')
   cartProducts.append(selectProduct3)
else :
     print(cartProducts)
     obj1 = Products.ProductCar(answer_category , cartProducts, phone_number,location)
     print(obj1.calculatePrice())
     exit()


obj1 = Products.ProductCar(answer_category , cartProducts, phone_number,location)
print(obj1.calculatePrice())

exit()

