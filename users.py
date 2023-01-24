from art import *



'''
here you can make user class if there is time
'''
def user(id):
    if id =="1":
        tprint("You are logged in.",font="fancy95")
        return 1
    elif id == 2:
        tprint("No points are recorded",font="fancy95")
        return 0

def showPoints(id):
    if id == 1:
        print(f"{user1} points")
    else:
        return

def addPoints(id,points):
    if id == 1:
        user1 = addingPoints(points,user1)
    else:
        return

addingPoints = lambda x , y : x+y
user1 = int
user("1")