from hospital import*
from colour_text import*

ct = ColourText()
ct.initTerminal()




user1=the_hospital_system("saad","Alshahriy",12945654,1122,"male",599231124)
user2=the_hospital_system("mohammad","Alqahatni",10234556,1321,"male",504323115)
user3=the_hospital_system("Noura","Alshahrani",10384555,4221,"fmale",564432223)
user4=the_hospital_system("jana","Alqahatni",234452456,1234,"fmale",596232344)
users_log={"12945654" : user1,"10234556" : user2,"10384555":user3,"234452456":user4}

def vistor_number(user_id):
    return users_log.get(user_id, None)



user_input=input( "plase put the ID number : ")
the_user=vistor_number(user_input)
if the_user is not None: 
    print(the_user.get_description())

try:
    the_user=vistor_number(user_input)
    if the_user !=True:
     print(the_user.get_description())
except Exception as IdError:
    for x in users_log:
        if x!=users_log:
         print(ct("  <>red the number of id not found palese try agien<> "))
        else:
         print("seccesful")




print("the number of patient visites hospital",the_user.get_vistor_city())


   
search = input("inter city name to check visitor :")
if the_user.get_vistor_city().get(search, 0) > 0:
 print(user1.get_name(),user2.get_name(),user3.get_name(),user4.get_name())
else:
        print('this is the first time!')



file = open("patient_record.txt", "w", encoding="utf-8")
content = file.write(user1.get_description())
content = file.write(user2.get_description())
content = file.write(user3.get_description())
content = file.write(user4.get_description())
print(content)
file.close()




