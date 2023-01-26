
from colorama import Fore, Back, Style


def usrs(flag:int):
    print("hi, in Users function")

    srFlagA:list=["Makka", "Muna"]
    srFlagD:list=["Hada", "Shafa", "Raha"]


    file = open("users.txt", "a+", encoding="utf-8")
    usrList=[line.strip() for line in open('users.txt')]
    print(usrList)
    
    print(Back.WHITE), print(Fore.BLUE)
    inUser:str=input("Enter the User Name:\n\n")
    if (flag == 2 and inUser in usrList): projects("") #new project
    elif (flag == 0 and inUser in usrList): print("This user Already Exist!")
    elif (flag == 0 and inUser not in usrList): #new user

        file.writelines([inUser, "\n"])
        file.seek(0)
        file.close()
        usrList = [line.strip() for line in open('users.txt')]
        print("The user have been added to the user list:")
        count=1
        for item in usrList:
            print(count, "- ", item)
            count+=1
    elif (flag == 1 and inUser not in usrList): print("No Such User")
    elif (flag == 1 and inUser in usrList):
       
        designerFile = open(inUser+"Designs.txt", "a+", encoding="utf-8")
        #designerFile    .writelines([newProjectName, "\n"])
        designerFile    .seek(0)
        designerFile    .close()

        authorFile = open(inUser+"Authoring.txt", "a+", encoding="utf-8")
        #authorFile      .writelines([newProjectName,"\n"])
        authorFile      .seek(0)
        authorFile      .close()
        usrDesignerList:list =  [line.strip() for line in open(inUser + "Designs.txt")]
        usrAutherList:list =  [line.strip() for line in open(inUser + "Authoring.txt")]
        
        logIn(usrAutherList,usrDesignerList,inUser)

def work (usrAuthoringList:list,usrDesignList:list,usrName:str):
    usrList = [line.strip() for line in open('users.txt')]
    workScope:str=input("If you want to Author type [A/a] or [D/d] for Design works \n")
    while (workScope not in ['A','a','D','d']):
        workScope=input("Enter a valid choise ")
    else:
        if (workScope in 'Aa' and len(usrAuthoringList) > 0):
            print(usrAuthoringList)
            authorWork:str=input("Choose project name to Approve/Reject\n")
            while (authorWork not in usrAuthoringList):
                print(usrAuthoringList)
                authorWork:str=input("Choose valid project name to Approve/Reject\n")
            authorDecision:str=""
            print("Type [A/a] to Approve the Design")
            print("Type [R/r] to Approve the Design")
            authorDecision=input()
            while (authorDecision not in 'A,a,R,r'):
                print("Type [A/a] to Approve the Design")
                print("Type [R/r] to Approve the Design")
                authorDecision=input()
            if(authorDecision in 'A,a'):
                file = open("DoneProjects.txt", "a+", encoding="utf-8")
                file.writelines([authorWork, "\n"])
                file.seek(0)
                file.close()

                #file01 = open(usrName+"Authoring.txt", "a+", encoding="utf-8")
                #file01.writelines([authorWork, "\n"])
                #file01.seek(0)
                #file01.close()
                file01 = open(usrName+'Authoring.txt','r')
                a = [authorWork]
                lst = []
                for line in file01:
                    for word in a:
                        if word in line:
                            line = line.replace(word,'')
                    lst.append(line)
                file01.close()
                file01 = open(usrName+'Authoring.txt','w')
                for line in lst:
                    file01.write(line)
                file01.close()
                print("Project is Done!")
                
            elif(authorDecision in 'Rr'):
                print("The Available Users are: ", usrList)
                newProjectDesigner = input("Enter the Project Architact Name\n")
                while (newProjectDesigner not in usrList):
                    print("UNKNOWN USER, To register a new Employee Rerun the application")
                    print(usrList)
                    newProjectDesigner = input("Enter valid Architact Name\n")
                designerFile = open(newProjectDesigner+"Designs.txt", "r+", encoding="utf-8")
                designerFile.writelines([authorWork, "\n"])
                designerFile.seek(0)
                designerFile.close()



        elif (workScope in 'Dd' and len(usrDesignList) > 0):
            print(usrDesignList)
            designerWork:str=input("Choose project name to submit ")
            while (designerWork not in usrDesignList):
                print(usrList)
                designerWork:str=input("Choose valid project name to submit")

            newProjectAuthor = input("Enter the Project Author Name")
            while (newProjectAuthor not in usrList):
                print("UNKNOWN USER, To register a new Employee Rerun the application")
                print(usrList)
                newProjectAuthor = input("Enter valid Author Name")
            authorFile = open(newProjectAuthor+"Authoring.txt", "r+", encoding="utf-8")
            authorFile.writelines([designerWork,"\n"])
            authorFile.seek(0)
            authorFile.close()

            file03 = open(usrName+'Authoring.txt','r')
            a = [designerWork]
            lst = []
            for line in file03:
                for word in a:
                    if word in line:
                        line = line.replace(word,'')
                lst.append(line)
            file03.close()
            file03 = open(usrName+'Designs.txt','w')
            for line in lst:
                file03.write(line)
            file03.close()

            print("Your Design is submited")

def fChoise (usrChoise:int) -> str:
    print("hi, in fChoise function")
    if (usrChoise == 1): return ("Login")
    elif(usrChoise== 2): return ("newProject")
    elif(usrChoise== 3): return ("addUser")
    else: print("Enter a valide Choise or [Ctrl + C] to exit")

def logIn (usrFlagA:list, usrFlagD:list,newUser:str):
    print("hi, in Login function")
    print("Hello ",newUser,"!")
    if (usrFlagA == []): 
        print(Back.GREEN), print(Fore.BLACK)
        print("\033[1m No Project To Author")# + Style.RESET_ALL)
    else: 
        print(Back.YELLOW), print(Fore.BLACK)
        print('Pending Project To Author are:')
        counter:int=0
        for project in usrFlagA:
            counter+=1
            print(counter,"- ",project)
        #print(Style.RESET_ALL)

    if (usrFlagD == []): 
        print(Back.GREEN), print(Fore.BLACK)
        print("No Project To Analyze and Design")# + Style.RESET_ALL)

    else: 
        print(Back.RED), print(Fore.WHITE)
        print('Pending Project To Analyze and Design are:')
        counter:int=0
        for project in usrFlagD:
            counter+=1
            print(counter,"- ",project)
            #print(Style.RESET_ALL)
    
    print(Style.RESET_ALL)
    work(usrFlagA,usrFlagD,newUser)

def projects(usrFlag: str):
    print("hi, in Projects function")
    projectFile = open("projects.txt", "a+", encoding="utf-8")
    usrList = [line.strip() for line in open('users.txt')]
    projectList: list = [line.strip() for line in open('projects.txt')]

    #designerDict: dict = {line.split()[0]: line.split()[1] for line in open("designers.txt")}
    #designPairs = (line.split(None) for line in "designers.txt")
    #designerDict:dict  = {int(designPairs[0]):designPairs[1] for designPairs in designPairs if len(designPairs) == 2 and designPairs[0].isdigit()}
    #print(designerDict)

    #authorDict: dict = {line.split()[0]: line.split()[1] for line in open("authors.txt")}
    #authorPairs = (line.split(None) for line in authorFile)
    #authorDict:dict = {int(authorPairs[0]):authorPairs[1] for authorPairs in authorPairs if len(authorPairs) == 2 and authorPairs[0].isdigit()}
    #print(authorDict)

    if (usrFlag == ""):
        newProjectName: str = ""
        newProjectDesigner: str = ""
        newProjectAuthor: str = ""

        newProjectName = input("Enter The New Project Name:")
        while (newProjectName in projectList):
            print("This Project already rejesterd!")
            newProjectName = input("Enter A New Project Name:\n")

        print("The Available Users are: ", usrList)
        newProjectDesigner = input("Enter the Project Architact Name\n")
        while (newProjectDesigner not in usrList):
            print("UNKNOWN USER, To register a new Employee Rerun the application")
            newProjectDesigner = input("Enter valid Architact Name\n")

        #newProjectAuthor = input("Enter the Project Author Name")
        #while (newProjectAuthor not in usrList):
           # print("UNKNOWN USER, To register a new Employee Rerun the application")
           # newProjectAuthor = input("Enter valid Author Name")

        
        projectFile     .writelines([newProjectName, "\n"])
        projectFile     .seek(0)
        projectFile     .close()

        designerFile = open(newProjectDesigner+"Designs.txt", "a+", encoding="utf-8")
        designerFile.writelines([newProjectName, "\n"])
        designerFile.seek(0)
        designerFile.close()

        #authorFile = open(newProjectAuthor+"Authoring.txt", "a+", encoding="utf-8")
        #authorFile.writelines([newProjectName,"\n"])
        #authorFile.seek(0)
        #authorFile.close()

        
        usrDesignerList:list =  [line.strip() for line in open(newProjectDesigner + "Designs.txt")]
        usrAutherList:list =  [line.strip() for line in open(newProjectAuthor + "Authoring.txt")]
        print(usrDesignerList)
        print(usrAutherList)
        

        #designerDict[usrFlag] = usrDesignerList, print(designerDict)
        #authorDict  [usrFlag] = usrAutherList, print(authorDict)

    elif (usrFlag not in usrList):
        print("Rerun the application to get the user registed")
    else:
        print("Hi", usrFlag)
        usrDesignerList:list =  [line.strip() for line in open(usrFlag + "Designs.txt")]
        usrAutherList:list =  [line.strip() for line in open(usrFlag + "Authering.txt")]
        
        logIn(usrAutherList,usrDesignerList,usrFlag)




####################################3333
try:
    print(Back.MAGENTA), print(Fore.WHITE)
    print("\033[1mPress [1] :\t if you Want to Login")# + Style.RESET_ALL)
    print(Back.CYAN), print(Fore.BLACK)
    print("\033[1mPress [2] :\t if you Want to Open New Project")# + Style.RESET_ALL)
    print(Back.WHITE), print(Fore.BLUE)
    print("\033[1mPress [3] :\t if you Want to Add New User\n" + Style.RESET_ALL)
    print(Back.GREEN), print(Fore.BLACK)

    srChoise:int=int(input())
    print(Style.RESET_ALL)


    if (fChoise(srChoise)=="Login"):
        usrs(1)
    elif (fChoise(srChoise)=="addUser"):
        usrs(0)
    elif (fChoise(srChoise)=="newProject"):
        usrs(2)
    else: print("Please Enter a valid Choise [1], [2] or [3]")


except ValueError:
    print("Pleas Enter a Number, not a Word")





#print(Style.DIM)



