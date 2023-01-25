
from student import student

student1 = student(name="mohmmad", age=32, gender="male", GPA=3.75, DNA=20.0)

print(""" 

             Welcome To Student Management System	


Enter 1 : To check student GPA
Enter 2 : see absent persent % 
Enter 3 : Check the student if he or she has an absence
Enter 4 : to see student information 
Enter 0 : to exit 

        """)

flag = True
while flag:
    user_input = int(input("please select a number from "))
    if user_input == 1:
        print(f" gpa out of 5 : {student1.GPA}  : {student1.student_GPA()}  ")
    elif user_input == 2:
        print(f"the persent of absent for {student1.name} {student1.attendance_rate()} %  ")
    elif user_input == 3:
        print(f" WITH {student1.is_student_status_DNA()}")
    elif user_input == 4:
        student_info = f"name  : {student1.name} , age : {student1.age} , gender : {student1.gender} ,  GPA  : {student1.GPA} ,  attendance rate : {student1.is_student_status_DNA()}"
        print(student_info)
    elif user_input == 0:
        flag = False
        print("see soon!!")




