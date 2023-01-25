from patient import patient
import os
import platform
from art import *

Art=text2art("""Welcome To Doctor Helper""") 
print(Art)
print("Add your patient to access to all services , and follow instruction")
print("***"*40)


start_user = input("do you wont to add new user or No ? y / n : ")

if(start_user.lower() == 'y'):
	patient1=patient(name=input("please enter patient name : "), appointment="" , gender=input("please enter gender : ") , age=input("please enter age : ") , weight=int(input ("please enter weight : ")) , hight_in_meter=float(input("please enter tall meter  : ")))
	result = patient1.add_to_list()	
	BMIOne = patient1.calculate_BMI()
	
else:
	print("ther is no patient please enter new one *_*  ")
	patient1=patient(name=input("please enter patient name : "), appointment="" , gender=input("please enter gender : ") , age=input("please enter age : ") , weight=int(input ("please enter weight : ")) , hight_in_meter=float(input("please enter tall meter : ")))
	result = patient1.add_to_list()	
	BMIOne = patient1.calculate_BMI()	
def managePatient():
	
	
		


		print(""" 
		          *Main Section*
		Enter 1 : To claclate_burn_calories !
		Enter 2 : To calculate_BMI !
		Enter 3 : To calculate_body_case_according_to_BMI ! 
		enter 4 : to show patient info !
		enter 5 : to check the next appointment status , and Give a Recommandation for a patient ! 
		enter 6 : to show all patient has been record  !
		enter 7 : to Search For a patient if he exist !
		

				""")
		
					
		try: #Using Exceptions For Validation
			userInput = int(input("Please Select An Above Option: to leave enter 0  :  ")) #Will Take Input From User
		except ValueError:
			exit("\nHy! That's Not A Number , please be sure to enter a number from 1 to 6") #Error Message
		else:
			print("\n") #Print New Line


				
		
			if(userInput == 1): 
				print("claclate_activity \n") 
				result_calc = patient1.claclate_activity( time = int(input(f'How many minutes for {patient1.name} daily exercising? ')) )
				print(f"patient {patient1.name} burn about {result_calc} calories a day ")

			elif(userInput == 2): 
				print("claclate_BMI : \n") 
				 
				print(f"{patient1.name} BMI is : {BMIOne}")

			elif(userInput == 3): 
				print("To calculate_body_case_according_to_BMI  : \n") 
				bmiResult = patient1.calculate_body_case() 
				print(f"patient body case according to BMI is{bmiResult}")



			elif(userInput == 4): 
				print("patient info \n") 
				for i in result:
					# print("name"patient1.name , patient1.age , patient1.gender , patient1.weight , patient1.hight_in_meter)
					patient_info = f"name  : {patient1.name} , age : {patient1.age} , gender : {patient1.gender} ,  weight : {patient1.weight} ,  hight in meter : {patient1.hight_in_meter}"
					print(patient_info)

			#add to the file 
			elif(userInput == 5):
				patient1.write_patient_info()

			#if patient need appointment system will enforce doctor to give appointment to the paitent before giving a recommendation and save patient details
			elif(userInput == 6):	 
				print("patients info \n") 
				file = open("patient.txt" , "r" , encoding="utf-8")
				content = file.read()
				print("patient" , content)
				file.close

			#for Search
			elif(userInput == 7):
				word = input("please enter the name for patient :  ")
				file = open(r'C:\Project\patient.txt', 'r')
				lines = file.readlines()
				for line in lines:
					if line.find(word) != -1:
						print(f"{word} , is exist in the System")
						break
				else:
					print(f"{word} ,is not exist ")	


			elif(userInput == 0):
				Art=text2art("""See You Soon """) 
				print(Art)
				quit("")		
			

		
	
							

managePatient()

def runAgain(): 
	runAgn = input("\nwant To Run  Y/n: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): 
			print(os.system('cls')) 
		else:
			print(os.system('clear'))

			
		managePatient()
		
		runAgain()
	
	elif(runAgn.lower() != 'n' and runAgn.lower() != 'y' ):
		
		print(f"{runAgn} is not correct try agin")
		
		managePatient()
		
		runAgain()

	else:
		Art=text2art("""See You Soon """) 
		print(Art)
		quit("")	
					 

runAgain()


				