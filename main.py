import class1 as data
from colorama import Fore
from art import *

#opject from User class

tprint(" Security  Vulnerabilities" ,font="small")

 

print("\n")
First_name=input(Fore.BLUE + "Enter your first name :")
Last_name=input(Fore.BLUE +"Enter your last name :")
print("\n")

user_1=data.User(First_name,Last_name,"random@gmail.com",598746623)
print(user_1.info())


print("\n")

vulnerabilities={1:"Broken Access Control",2:" Security Misconfiguration",3:"Identification and Authentication Failures"}
print("the vulnerabilities menu :")
print("\n") 
for key,value in vulnerabilities.items():
    print(key,value)
print("\n") 

try:
  user_input=int(input("Choose the vulnerability number from the menu:"))
except:
  print("You must write the number from the menu!!!")

print("\n")
print("1-Description")
print("2-Mitigation")
print("3-Exit")

print("\n") 

try:  
  number=int(input("Choose a number from the menu :"))
except:
  print("You must write the number from the menu!!!")


print("\n")

print("\n") 

while user_input==1:
        if number==1:
            file=open("Broken Access Control description.txt","r+",encoding="utf-8")
            content=file.readlines()
            for line in content:
                print(line)
            file.close()  
            break
        elif number==2:
               file=open("Broken Access Control Mitigation.txt","r+",encoding="utf-8")
               content=file.readlines()
               for line in content:
                   print(line)
               file.close()
               break
               print("EXIT")
        elif number==3:
            print("EXIT")
            break   
        elif number>3:
            print("Not one of the numbers on the menu")
            print("EXIT")
            break  
        
while user_input==2:
        if number==1:
            file=open("Security Misconfiguration description.txt","r+",encoding="utf-8")
            content=file.readlines()
            for line in content:
                print(line)
            file.close()
            break
        elif number==2:
            file=open("Security Misconfiguration Mitigation.txt","r+",encoding="utf-8")
            content=file.readlines()
            for line in content:
                print(line)
            file.close()
            break
        elif number==3:
            print("EXIT")
            break
        elif number>3:
            print("Not one of the numbers on the menu")
            print("EXIT")
            break        

while user_input==3:
        if number==1:
            file=open("Identification and Authentication Failures description.txt","r+",encoding="utf-8")
            content=file.readlines()
            for line in content:
                print(line)
            file.close()
            break
        elif number==2:
            file=open("Identification and Authentication Failures Mitigation.txt","r+",encoding="utf-8")
            content=file.readlines()
            for line in content:
                print(line)
            file.close()
            break
        elif number==3:
            print("EXIT")
            break
        elif number>3:
            print("Not one of the numbers on the menu")
            print("EXIT")
            break 

print("\n")
print("\n")

satisfied_percentage=input("On a scale of 1 to 100, how satisfied are you with our program ?" )
satisfaction= lambda rating : rating * 1

print(satisfaction(satisfied_percentage + "%")) 





def good_bye():
   return f"Thank you for using our program.... Bye"
   
print(good_bye()) 



