from art import *



'''
here you can make user class if there is time
'''
class Users:
    user1 = 0
    userID = 0
    #user1
    def set_user1(user1):
        Users.user1 = user1
    def get_user1():
        return Users.user1
    #userID
    def set_userID(userID):
        Users.userID = userID
    def get_userID():
        return Users.userID

    def user(id):
        if id ==1:
            tprint("You are logged in.",font="fancy95")
            Users.set_userID(id)
            return 1
        elif id == 2:
            tprint("No points are recorded",font="fancy95")
            return 0

    def showPoints(id):
        if id == 1:
            return Users.get_user1()
        else:
            return

    def addPoints(id,points):
        addingPoints = lambda x , y : x+y
        if id == 1:
            oldScore = Users.get_user1()
            newScore = addingPoints(points,oldScore)
            Users.set_user1(newScore)
        else:
            return
