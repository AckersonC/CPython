import tkinter as tk

data = []
r_id = []
repeat = []
usr = []
check = []
ibook = []
iid = []
n_check = []
idcheck = ''
datalist = []
a = True
booktimes  =  0

for steps in range (1):
    enter = input ("Start the program? (y/n): ")
    if enter == 'y' :
        while a == True:
            mylibrary=open ("lib.csv", 'w+')
            ID = input ("Please enter your ID: ")
            iid.append (ID)
            print ("What do you want to do...?\n(1)Borrow a book\n(2)Return a book\n(3)Inquiry\n(4)Library Administrator\n(5)Exit")
            option = input ("Please select an option: ")
            if option == '1' :
                
                                    
                if ID != check :
                    check.append (ID)
                    nameofbook = input ("Please enter the name of the book: ")
                    ibook.append (nameofbook)
                    datadata = ID + nameofbook
                    datalist.append (ID)
                    datalist.append (nameofbook)
                    datalist.append ('|')
                    data.append (datadata)
                    mylibrary.write (ID)
                    mylibrary.write (booktimes)
                    alllibrary = mylibrary.read()
                    usr.append (datadata)
                    repeat.append (ID)
                    r_id.append (ID)
                    iid.append (ID)
                    
                    if nameofbook == '':
                        print ("ERROR!Please enter a valid book name!!!")
                        break
                    n_check.append (nameofbook)
                    print ("Your request has been processed.")
                    books = books + 1
                else:
                    print ("You haven't returned your previous book. Please select the return a book option to proceed...")
            elif option == '2' :
                r_nameofbook = input ("Please enter the name of the book: ")
                if r_nameofbook == '':
                        print ("ERROR!Please enter a valid book name!!!")
                        break
                if r_nameofbook in n_check  :
                    if ID in check :
                        r_ask1 = ID
                        r_ask2 = r_nameofbook
                        r_data = r_ask1 + r_ask2
                        if r_data in data:
                            n_check = []
                            check = []
                            iid.remove (ID)
                            ibook.remove (r_nameofbook)
                            r_id.remove (ID)
                            repeat.remove (ID)
                            print ("Successfully returned book. Please come again.")
                            books = books - 1
                        else:
                            print ("Bookname or ID invalid. Please try again...")
                    else :
                        print ("Please borrow a book first. Please select the Inquiry option to check...")
                else:
                    print ("Bookname or ID invalid. Please try again...")
            elif option == '3':
                try:
                    if data == usr :
                        print ("ID: " + ID)
                        print ("Status: Not returned")
                    else:
                        print ("Status: Returned")
                except:
                    print ("Sorry, something went wrong...No values in list. Please start using the program to use Inquiry option.")
            elif option == '4':
                print ("This option is for library administrators only, please contact your library administrator to access.")
                usrname = input ("Username: ")
                password = input ("Password: ")
                if usrname == 'user' and password == '123' :
                    print ("(1)Check usr ID and book borrowed\n(2)Change number f book usr can borrow")
                    adminask = input ("Please select an option: ")
                    if adminask == '1':
                        print (datalist)
                else:
                    print ("Access denied, please contact your library administrator.")
                                    
                
            elif option == '5':
                a = False
                print ("Thank you for using LMS, please come again!!!")
            
            else :
                print ("ERROR! Option not found. Please select an existing option!!!")
                    
    elif enter == 'n' :
        print ("Thank you for comming, please come again.")
        break
    else :
        print ("Plese select an existing option...!")





