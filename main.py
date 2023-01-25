#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from mobile_price import MobilePrice
import sys
print ("WELCOME IN OUR PREDICTION PROGRAM <3,WANT TO KNOW THE PRICE OF YOUR MOBILE? PLEASE ENTER YOUR MOBILE SPECIFICATIONS :) ")

def question(text,fun=int):
    try:
        feauters.append(fun(input(text)))
    except ValueError:
        print("Please try again")
        sys.exit(0)
if __name__ == "__main__":

    mp = MobilePrice("https://raw.githubusercontent.com/amankharwal/Website-data/master/mobile_prices.csv")
    mp.train_model()    
    while True:
        feauters = []
        question("1-What is your battery capacity?\n")
        question("2-Is there bluetooth in your mobile phone?\n")
        question("3-What is the frequency of your mobile phone processor?\n",fun=float)   
        question("4-Does your device have a dual_sim feature?\n")
        question("5-How many megapixels is your front camera?\n")
        question("6-Does your device support 4G technology?\n")
        question("7-What is the internal memory capacity of your mobile phone?\n")
        question("8-Enter the depth of your mobile in cm\n",fun=float)
        question("9-Enter the Weight of your mobile in gram\n")
        question("10-Enter the Number of cores of a processor\n")    
        question("11-How many megapixels is your primary camera?\n")    
        question("12-Enter Pixel Resolution Height\n")    
        question("13-Enter Pixel Resolution Width\n")    
        question("14-What is the RAM capacity of your mobile phone?\n")
        question("15-Enter the Screen Height of mobile in cm\n")
        question("16-Enter the Screen Width of mobile in cm\n")
        question("17-what is the longest time that a single battery charge will last when you are?\n")
        question("18-Does your device support 3G technology?\n")
        question("19-Does your device support touch screen?\n")
        question("20-Does your device support wifi?\n")
        print("\nResult:")
        res = mp.result(feauters)[0]      
        if(res == 0):
            print("Your mobile cost is a low")
        elif(res == 1):
            print("Your mobile cost is a normal")
        elif(res == 2):
            print("Your mobile cost is a high ") 
        else:
            print("Your mobile cost is a very high ")            
        print("----------------------------------------------------------------- \n")    
    


# In[ ]:




