from Bank_account import User_Information , Atm

try:
    name=input("wrie your name: ")
    for call in range(3):
        phone_number=input("please enter your phone number: ")
        id=input("please enter your national identity: ")
        user=User_Information(name,phone_number,id)
        if type(user.new_account()) != tuple:
            print(user.new_account())
        else:
            print(f"{user.get_name()} your account created",user.new_account())
            break



    atm=Atm(0)
    for x in range(5):
        amount_to=int(input("Enter the amount to deposit :"))
        if amount_to > 50000:
            print("Go to the bank to deposit the amount")
        elif amount_to < 50 :
                print("try to deposit larger amount ")
        else:
            atm.deposit(amount_to)
            out = input("do you want it to deposit more? press Enter to continue if no write 'exit': ")
            if out == "exit":
                break



    while True :
        masseg = input("do you want to withdraw from your balance press 'w' or view balance press 'v' 'exit' to out: ")
        if masseg.lower()== "w":
            number = int(input("enter the amount to withdraw  : "))
            atm.withdraw(number)
        elif masseg.lower()== "v":
            atm.balance()
        else:
            break




except KeyboardInterrupt:
    print("you have a KeyboardInterrupt")




print("\n thank you for using our program")

