
class patient():
    def __init__(self,name:str,gender:str,age:int , weight : float , hight_in_meter : float , appointment : str):
        self.name = name
        self.gender = gender
        self.appointment = ""
        self.age = age
        self.weight = weight
        self.hight_in_meter = hight_in_meter
        


    def claclate_activity(self , time : int) -> float :
        '''calculate burn calories according to patient daile exrecise '''
        calories = (time * 3.4)
        calories = float(calories)
        return calories


    def calculate_BMI(self) -> float:
        BMI : float = self.weight / (self.hight_in_meter*2)
        return  BMI


    def calculate_body_case(self)-> str:
        '''giv an expression understandable for patient not for Doctor'''
        BMI_RESULT_FOR = self.calculate_BMI()
        if BMI_RESULT_FOR < 17:
            msg = f"BMI : {BMI_RESULT_FOR} is over Underweight (Mild thinness)"
            return msg
        elif BMI_RESULT_FOR > 18 and BMI_RESULT_FOR < 24.9:
            msgOne = f"BMI : {BMI_RESULT_FOR} Normal range"
            return msgOne
        else : 
            msgTow = f" : {BMI_RESULT_FOR} , {self.name} is Overweight"
            return msgTow     
            
                
    def add_to_list(self) ->list :
        new_list : list = []
        new_list.append(patient(self.name , self.appointment , self.gender , self.age , self.weight , self.hight_in_meter))
        patient_list = new_list
        return patient_list

    def in_need_for_Physical_examination(self) -> bool:
        '''this function help System to define an appintment or not '''
        is_in_need : float = self.calculate_BMI()
        if is_in_need >= 30:
            return True
        else:
            return False  

    def make_an_appointment(self):
        '''check '''
        if self.in_need_for_Physical_examination() == True:
            appointmentnew = self.appointment 
            appointmentnew = input(f"please eter an appointment for patient : {self.name} , (year/month/day) ex-2023/6/6  : ") 
        else:
            appointmentnew = "ther is no appointment for patient"             
        return appointmentnew
    
    def write_patient_info(self):
        file_name =open('patient.txt'  , "a" , encoding="utf-8") 
        file_name.writelines(f"name : {self.name} , Gender :  {self.gender} , Age: {self.age} , BMI : {self.calculate_BMI()}  , helth case according to BMI : {self.calculate_body_case()} , patient next appointment : {self.make_an_appointment()}  .  \n  ")
        file_name.writelines(input("enter any recommendation for patient \n"))
        file_name.writelines(f"\n \n \n ")
        file_name.close()


 
         

          
                  
