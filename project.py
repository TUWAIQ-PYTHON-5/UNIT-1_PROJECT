import main
def requrement(user_name):
         return f" Welcome {user_name} put all requirement  untill program work successfully  "


class Person:
    def __init__(self,name,Height,Mass):
             self.name=name
             self.Height=Height
             self.Mass=Mass
             
    print(main.program())

    def BMI_person(self):
          BMI=(self.Mass)/(self.Height**2)
          for t1, t2 in [(16, 'severely underweight'),
                       (18.5, 'underweight'),
                       (25, 'normal'), (30, 'overweight'),
                       (35, 'moderately obese'),
                       (float('inf'), 'severely obese')]:
                if BMI <= t1:
                  print('Your BMI is', BMI, 'and the person is :', t2)
                  plan=main.plan_function(BMI)
                  return plan
                  print(plan)
                  break
user_name=input("please enter your name:\n")
print(requrement(user_name))
user_hight=float(input("please enter your height in m :\n"))
user_Mass=float(input("please enter your mass in Kg : \n"))


user1=Person(user_name,user_hight,user_Mass)
print(user1.BMI_person())
z:str=input("welcome again do you want to calculate the amount of fat in your body: ")
if z=='yes':
  x:float=float(input("Enter you height in  cm :"))
  y:str=input("Enter your gender:")

  if y=='Male':
       perfect_weight = lambda x : (150-x)*1.1+48
       print(perfect_weight(x))
  else:
     y=='Female'
     perf_weight = lambda x : (150-x)*0.9+45
     print(perf_weight(x))
else:
    z=='no'
w:str=input("Did you benfit from this program ?")
if w=='yes'or 'no':
      try:
         k:str=input("Do you  have any suggestions to develop the program ?")
      except:
          print("please write it as string")
      if k=='no':
        print("Thank you for join to our Program ")
      else:
       if k=='yes':
        print("We will take your suggestion into consideration ,Thank you for join to our Program ")