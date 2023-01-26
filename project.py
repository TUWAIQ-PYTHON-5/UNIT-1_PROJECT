import datetime
date = datetime.datetime.now()



class read:
    def read_diary():
        file_read = input("To read write (r), or choose any letter to move: ")

        if file_read == "r":
            try:
                file=open(input("Type the file name:"),"r",encoding="utf-8")
                for read_lines in file:
                    print(read_lines)
                file.close()
            except FileNotFoundError:
                print("File not found:\n ","__"*50 )
                    
def write_file():
    while True:
    
        file=open(input("Enter the file name to search for or create it: \n"),"a+",encoding="utf-8")
        word = input("enter you diary : \n")
        file.writelines(f"\n{word}")
        file.writelines(f"\n{date}")
        file.close()
        break
                
        





