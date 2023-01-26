from Login import * 
import json
from art import *
from stringcolor import * 


login_admin = Login ("abdulrahman",1, 1243, "Admin")
login_user1 = Login ("Sarah",2, 123, "User")
login_user2 = Login ("Ahmed",3, 4544, "User")
login_user3 = Login ("Nourah",4, 123, "User")


users_check = [login_user1, login_admin, login_user2, login_user3]

def Welcome_page ():
    print(cs("Welcome to - Daily Task -","DarkViolet2","lightgrey6"))
    return

 
def login_info(): #1 اول عملية 
    user_login_name = input("Please Add Your Name :")
    user_login_password = int(input("Please Add Your Password :"))
    x = 0
    for u in users_check:
     if  u.name.lower() == user_login_name and u.password == user_login_password :
         print(cs( f"welcome {u.name}","white","green"))
         x = 1 
         return u 
         
         break
    if x != 1:
         print(cs("SIR YOUR PASSWORD OR USERNAME IS WRONG , Plz enter Again","yellow", "Red")) 
         return None


def first_page_admin():
    for user in users_check:
        if user.privilege=="User":
         print(user.id ," - " ,user.name,"\n") 
    chose_employee = int( input("Please enter the employee number : \n"))
    for emp in users_check:
        if emp.id == chose_employee :

            secund_page_admin(emp.id)



def secund_page_admin(current_emp): #current employee is employee num 
    print(" - Select the operation to be performed -")
    print( "\n1--To add task \n2--View task status \n3-- Back to Employee list")
    admin_choise = int( input())
    if admin_choise == 1 :
        add_new_task(current_emp)
    elif admin_choise == 2 :
        view_task(current_emp)
    elif admin_choise == 3 :
         first_page_admin ()

def add_new_task (current_emp):
        type_in_item = input("Please write the task that you want to type :  ")
        file = open("user"+str(current_emp)+"Task.txt", "a", encoding="utf-8")
        task =Task(type_in_item,0)
        file.write(json.dumps(task.__dict__)+ "\n" ) 
        print(cs("Task added successfully !!!","Green"))
        file.close()
        first_page_admin()

def view_task(current_emp):
    try:
        file_read = open("user"+str(current_emp)+"Task.txt", "r+", encoding="utf-8")
        print("The Task Progress Are : ")
        Lines = file_read.readlines()
        counter= 0
        for line in Lines:
            counter +=1 # يرقم لي التاسك
            y = json.loads(line)
            print(str(counter)+" - " + y ['task_name'] + "     " + str(y['status'])+"%")
        file_read.close()
        
    except:
        print(cs("file not found !!! 404 Or line not found 404","yellow", "#ff0000"))


def update_progress(id,line,progress):
    try:
        file_read = open("user"+str(id)+"Task.txt", "r+", encoding="utf-8")
        Lines = file_read.readlines()
        y=json.loads(Lines[line-1])
        task =Task(y["task_name"],progress)
        Lines[line-1]=json.dumps(task.__dict__)+"\n"
        file_read.seek(0)
        file_read.truncate()
        for l in Lines:
            file_read.write(l) 
        file_read.close()
        view_task(id)
    except:
        print(cs("file not found !!! 404 Or line not found 404","yellow", "#ff0000"))

Welcome_page()

current_account=None
while current_account==None:
    current_account=login_info()  

if current_account.privilege =="Admin": #2 ثاني عمليه
    while input("press anything to continue and 0 to exit : ")!="0":
         first_page_admin()
    
    else:
        print(f"{cs('Thank You For Using Daily Task', 'yellow', 'grey').bold().underline()}")

elif current_account.privilege == "User":#2 ثاني عمليه
    while input("press anything to continue and 0 to exit : \n")!="0":
            print(bold("- your Daily Tasks - ").underline().cs("yellow", "gray"))
            view_task(current_account.id)# ثالث داله تشتغل 
            task_line =int(input("please select task number to update progress: ")) #  بعد مايعرض بيرجع هنا
            progress_percentage =int(input("please select the percentage of progress: "))
            print("")
            update_progress(current_account.id,task_line,progress_percentage) 
    else:
        print(f"{cs('Thank You For Using Daily Task', 'yellow', 'grey').bold().underline()}")



