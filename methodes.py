def resturants_names():
    ''' return reaturants names'''
    file = open("resturants.txt", "r", encoding="utf-8")
    lines = file.readlines()
    result = []
    for x in lines[1:]:
        result.append(x.split(',')[0])
    file.close()
    return result

# print(resturants_names())

def sales_lists() :
    ''' return nested list of sales'''
    file = open("resturants.txt", "r", encoding="utf-8")
    lines = file.readlines()
    result = []
    for x in lines[1:]: #nestead list ,all columns in one list and each column represnt list 
        result.append(x.split(',')[3:])
    file.close()
    return result

def all_months_sales() : # return every month sales in list
    total_sales = []
    sales = sales_lists()
    for month_list in sales : # buecuase sales[0:1] is the monthes names
        sum = 0
        for monthly_resturant_sales in month_list :
            sum += int(monthly_resturant_sales)
        total_sales.append(sum)  
    return total_sales



def totalـsales() : # total sales for every resturant
    resturants_sales = {}
    
    resturants_name = resturants_names()
    sales = sales_lists()
    total_sales = all_months_sales()
    
    for i in range(0,len(resturants_name)):
        resturants_sales[resturants_name[i]]=total_sales[i]
        # print(resturants_sales)

    for name, sales in enumerate(resturants_sales) :
        print(f"Resturant name: {sales}, slaes: {resturants_sales[sales]} SR ")

# totalـsales()



def first_quarter_sales() : # first quarter sales
    first_quarter_sales = []
    sales = sales_lists()
    for month_list in sales : 
        sum = 0
        for monthly_resturant_sales in month_list[0:3] :
            sum += int(monthly_resturant_sales)
        first_quarter_sales.append(sum)
    return first_quarter_sales

def seconde_quarter_sales() : # seconde quarter sales
    seconde_quarter_sales = []
    sales = sales_lists()
    for month_list in sales : # first quarter sales
        sum = 0
        for monthly_resturant_sales in month_list[3:6] :
            sum += int(monthly_resturant_sales)
        seconde_quarter_sales.append(sum)
    return seconde_quarter_sales

def third_quarter_sales() : # third quarter sales
    third_quarter_sales = []
    sales = sales_lists()
    for month_list in sales : # first quarter sales
        sum = 0
        for monthly_resturant_sales in month_list[6:9] :
            sum += int(monthly_resturant_sales)
        third_quarter_sales.append(sum)
    return third_quarter_sales

def fourth_quarter_sales() : # fourth quarter sales
    fourth_quarter_sales = []
    sales = sales_lists()
    for month_list in sales : # first quarter sales
        sum = 0
        for monthly_resturant_sales in month_list[9:12] :
            sum += int(monthly_resturant_sales)
        fourth_quarter_sales.append(sum)
    return fourth_quarter_sales

add_numbers = lambda x , y : x+y #lambda function

def first_half_sales():
    first_half = []
    for i in range(0,len(first_quarter_sales())):
        sal = add_numbers(first_quarter_sales()[i],seconde_quarter_sales()[i])
        first_half.append(sal)
    return first_half

def seconde_half_sales():
    seconde_half = []
    for i in range(0,len(third_quarter_sales())):
        sal = add_numbers(third_quarter_sales()[i],fourth_quarter_sales()[i])
        seconde_half.append(sal)
    return seconde_half

# print(first_half_sales())
# print(seconde_half_sales())


def staff_number() : # return list of employees number
    staff = []
    file=open("resturants.txt", "r", encoding="utf-8")
    lines=file.readlines()
    for num in lines[1:]: 
        staff.append(num.split(',')[1])
    file.close()
    return staff

def branches_number() : # return list of branches number
    branches = []
    file=open("resturants.txt", "r", encoding="utf-8")
    lines=file.readlines()
    for num in lines[1:]: 
        branches.append(num.split(',')[2])
    file.close()
    return branches

def months_names_list() :
    file=open("resturants.txt", "r", encoding="utf-8")
    lines=file.readlines()
    names = []
    for name in lines[0:1]: # monthes names
        names.append(name.split(',')[3:])
    file.close()
    return names
        
def all_details() : # print all resturant details
    resturants_name = resturants_names()
    sales = sales_lists()
    staff = staff_number()
    branches = branches_number()
    total_sales = all_months_sales()
    first_half = first_half_sales()
    seconde_half = seconde_half_sales()
    first_quarter = first_quarter_sales()
    seconde_quarter = seconde_quarter_sales()
    third_quarter = third_quarter_sales()
    fourth_quarter = fourth_quarter_sales()
    months_names = months_names_list()
   
   
    for i in range(0, len(resturants_name)) :
        print("--"*20)
        print(f"Resturant name: {resturants_name[i]}")
        print(f"Number of branches: {branches[i]}")
        print(f"Staff: {staff[i]}")
        print(f"Total sales : {total_sales[i]}")
        print(f"Monthly sales :")
        for j in range(0,len(months_names[0])) :
            print(f"{months_names[0][j]} : {sales[i][j]}SR")
        print(f"First half sales : {first_half[i]}")
        print(f"seconde half sales : {seconde_half[i]}")
        print(f"First quarter sales : {first_quarter[i]}")
        print(f"Seconde quarter sales : {seconde_quarter[i]}")
        print(f"Third quarter sales : {third_quarter[i]}")
        print(f"Fourth quarter sales : {fourth_quarter[i]}")
       
# all_details()

def sales_details() : # print all resturant sales details
    file=open("resturants.txt", "r", encoding="utf-8")
    lines=file.readlines()

    
    
    resturants_name = resturants_names()
    sales = sales_lists()
    total_sales = all_months_sales()
    first_half = first_half_sales()
    seconde_half = seconde_half_sales()
    first_quarter = first_quarter_sales()
    seconde_quarter = seconde_quarter_sales()
    third_quarter = third_quarter_sales()
    fourth_quarter = fourth_quarter_sales()
    months_names = months_names_list()

    for i in range(0, len(resturants_name)) :
        print("--"*20)
        print(f"Resturant name: {resturants_name[i]}")
        print(f"Total sales : {total_sales[i]}")
        print(f"Monthly sales :")
        for j in range(0,len(months_names[0])) :
            print(f"{months_names[0][j]} : {sales[i][j]}SR")
        print(f"First half sales : {first_half[i]}")
        print(f"seconde half sales : {seconde_half[i]}")
        print(f"First quarter sales : {first_quarter[i]}")
        print(f"Seconde quarter sales : {seconde_quarter[i]}")
        print(f"Third quarter sales : {third_quarter[i]}")
        print(f"Fourth quarter sales : {fourth_quarter[i]}")
       

    
    file.close()

# sales_details()

