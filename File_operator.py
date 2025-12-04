print("Welcome to our new project File_Operator :)")

import datetime

now = datetime.datetime.now()


class File_Operator:
    
    def __init__(self):
        self.filename = "demo.txt"

    def add_entry(self):
        entry = input("Enter your journal here : ")
        with open("demo.txt","a") as file:
            file.write( entry + "\n")

        print("Entry added successfullly :)")

    def reader(self):
        print("\n Here are all the entries :)")
        file = open(self.filename,"r")
        lines = file.readlines()    
        for i in lines:
            print(i)
        file.close()
        print(f"{now}")

    def srch(self):
        kwrd = input("\nEnter a keyword which you want to found : \n")
        with open("demo.txt","r") as file:
            lines = file.readlines()
            
            for line in lines:
                if kwrd in line:
                    print("---------------")
                    print(f"[{now}]")
                    print(line)
        

    def c_E(self):
        Confirmation = input("\nAre youe about deleting All entries(Yes/No) : \n")
        if Confirmation == "Yes" or "yes":
            with open("demo.txt","w") as file:
                file.write("")
            print("\nYour all entries are deleted successfully :) \n")
        elif Confirmation == "No" or "no":
            print("Entries are safe :)")
        else:
            print("Invalid choice.")

file_op = File_Operator()

while True:
     
    print("Enter 1 to Add Entry.")
    print("Enter 2 to View all Entries.")
    print("Enter 3 to Search entry.")
    print("Enter 4 to Clear all entry.")
    print("Enter 0 to exit the programme.")

    Choice = int(input("Enter your Choice here : "))

    if Choice == 1:
          
        file_op.add_entry()

    elif Choice == 2:
        
       file_op.reader()

    elif Choice == 3:
      
        file_op.srch()

    elif Choice == 4:
        
        file_op.c_E()

    elif Choice == 0:
        print("Thanks for visiting our Project :)")
        print(f"[{now}]\n")

        break
    else:
        print("Your entered Choice is invalid :(")

