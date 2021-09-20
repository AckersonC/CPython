import tkinter as tk
repeat = []
check = ''
ibook = []
iid = []
n_check = ''
idcheck = ''
a = True
for steps in range (1):
    enter = input ("Start the program? (y/n): ")
    if enter == 'y' :
        while a == True:
            ID = input ("Please enter your ID: ")
            iid.append (ID)
            print ("What do you want to do...?\n(1)Borrow a book\n(2)Return a book\n(3)Inquiry\n(4)Exit")
            option = input ("Please select an option: ")
            if option == '1' :
                if ID in repeat :
                    print ("You haven't returned your previous book. Please select the return a book option to proceed...")
                else:
                    if ID != check :
                        check = (ID)
                        nameofbook = input ("Please enter the name of the book: ")
                        code = ID
                        repeat.append (code)
                        ibook.append (nameofbook)
                        if nameofbook == '':
                            print ("ERROR!Please enter a valid book name!!!")
                            break
                        n_check = (nameofbook)
                        print ("Your request has been processed.")
                    else:
                        print ("You haven't returned your previous book. Please select the return a book option to proceed...")
            elif option == '2' :
                r_nameofbook = input ("Please enter the name of the book: ")
                if r_nameofbook == '':
                        print ("ERROR!Please enter a valid book name!!!")
                        break
                if n_check == r_nameofbook :
                    if ID == idcheck :
                        n_check = ''
                        check = ''
                        iid.remove (ID)
                        ibook.remove (r_nameofbook)
                        print ("Successfully returned book. Please come again.")
                else :
                    print ("Please borrow a book first. Please select the Inquiry option to check...")
            elif option == '3':
                try:
                    if iid and ibook == ID and nameofbook:
                        print (ID)
                        print (nameofbook)
                        if ID == check:
                            print ("Status: Not returned")
                        else:
                            print ("Status: Returned")
                    else :
                        print ("Welcome new user, please start borrowing books to check inquiries.")
                except:
                    print ("Sorry, something went wrong...No values in list. Please start using the program to use Inquiry option.")
            elif option == '4':
                a = False
                print ("Thank you for using LMS, please come again!!!")
            else :
                print ("ERROR! Option not found. Please select an existing option!!!")
                    
    elif enter == 'n' :
        print ("Thank you for comming, please come again.")
        break
    else :
        print ("Plese select an existing option...!")
                    
                    
     
                    
                    
    
                
                




