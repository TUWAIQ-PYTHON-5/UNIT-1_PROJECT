
    
    
#Our services
list_services={1:"\nWhat is diabetes?\n",
    2:"Types of diabetes\n",
    3:"Blood Glucose(Sugar) levels & What they mean?\n",
    4:"Know your current(today) sugar level\n",
    5:"Symptoms of the diabetes\n",
    6:"Diet\n",
    7:"Weekly schedule to monitor your blood glucose level\n",
    8:"Ambulance number\n",
    9:"EXIT"}


while True:
        
        print("\nour services is:\n",list_services)
        services=int(input("\nWhat services number you want? \n"))

        
        #first service
        if services == 1:
            print("Diabetes is a chronic (long-lasting) health condition\nthat affects how your body turns food into energy.")
        #second service
        elif services== 2:
            print("Type 1 Diabetes:\nis thought to be caused by an autoimmune reaction (the body attacks itself by mistake).\nThis reaction stops your body from making insulin.\nApproximately 5-10% of the people who have diabetes have type 1")
            print("\nType 2 Diabetes:\nWith type 2 diabetes, your body doesn’t use insulin well and can’t keep blood sugar at normal levels.\nAbout 90-95% of people with diabetes have type 2\n")
        #third service
        elif services== 3:
            print("70 to 100 - do not have diabetes ,100 to 125 - This means that the person may be prediabetic\n(prediabetes means that the person has a higher than normal blood glucose level, but is not yet considered diabetic).\n126 or higher indicates that the person has diabetes")
        #fourth service
        elif services== 4:
            rate_glucose=int(input("What is the number shown on your device?? \n"))
            if rate_glucose >=126 :
                print("Your blood glucose level is high")
            if rate_glucose <=125:
                print("Your blood glucose level is low")
            if rate_glucose >=70 | rate_glucose<=100:
                print("Your blood glucose level is normal")
        #fifth service
        elif services== 5:
            print("high blood sugar include:\nFeeling very thirsty\nFrequent urination\nFatigue\nFeeling very hungry\nUnexplained weight loss\nBlurred vision\nSlow healing of cuts or sores.")
            print("\nlow blood sugar include:\nShaking or trembling\nSweating and chills\nDizziness or lightheadedness\nFaster heart rate\nIntense hunger.")
        #sixth service
        elif services== 6:
            print("The following foods should be included in the diabetic diet:\n 1. Fatty fish\n 2. Leafy vegetables\n 3. eggs\n 4. Greek yogurt\n 5. Nuts\n 6. broccoli \n"
            "\nFoods that diabetics should avoid: \nSweetened drinks with sugar\nFoods rich in fat\nWhite bread, rice, and pasta\nSweetened breakfast cereal\nEnergy Drinks.")
            #seventh service
        elif services== 7:
            Day1=int(input("First day\n"))
            Day2=int(input("Second day\n"))
            Day3=int(input("Third day\n"))
            Day4=int(input("Fourth day\n"))
            Day5=int(input("Fifth day\n"))
            Day6=int(input("Sixth day\n"))
            Day7=int(input("Seventh day\n"))
        
            sum=int(Day1+Day2+Day3+Day4+Day5+Day6+Day7)
            if sum== 2268:
                    print("You should consider what you eat, try to change or reduce it")
            if sum== 624:
                    print("Try to eat well")
            if sum== 1034:
                    print("Well done, keep your level up")
            #eighth service
        elif services== 8:
            print("997")
            #ninth services
        elif services== 9:
            x = lambda a, b : a * b
            print("1*1=",x(1,1))
            print ("Remember that the disease does not affect a person's life completely.\n")
            print("Thank you for visiting, we hope you are always safe")
            break