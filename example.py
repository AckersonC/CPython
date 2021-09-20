import tkinter as tk
import datetime
data = []
repeat = []
usr = []
check = []
n_check = []
datalist = []
booksrepeat = []
a = True
IDforbidlist = []
bookforbidlist = []
adminask = ''
soption = ["1", "2","3"]
for steps in range (1):
    print (datetime.date.today())
    enter = input ("Start the program? (y/n): ")
    if enter == 'y' :
        while a == True:
            option = ''
            print ("(1)User\n(2)Administrator\n(3)Exit")
            st = input ("Please select an option: ")
            if st == '3':
                a = False
                break
            if st not in soption :
                print ("Please select an existing option.")
            else:
                ID = input ("Please enter your ID: ")
                if ID == '':
                    print ("Invalid ID, please try again.\nExiting...")
                if ID in IDforbidlist :
                    print ("Sorry, this ID is blocked by the library administrator.")
                else:
                    while option != '5':
                        if st == '1':
                            print ("What do you want to do...?\n(1)Borrow a book\n(2)Return a book\n(3)Inquiry\n(5)Exit")
                        elif st == '2':
                            print ("What do you want to do...?\n(1)Borrow a book\n(2)Return a book\n(3)Inquiry\n(4)Library Administrator\n(5)Exit")
                        option = input ("Please select an option: ")
                        if option == '1' :
                            if ID in repeat:
                                print ("You haven't returned your previous book. Please select the return a book option to proceed...")
                            elif ID != check :
                                check.append (ID)
                                nameofbook = input ("Please enter the name of the book: ")
                                if nameofbook in bookforbidlist:
                                    print ("Sorry, this book is blocked by the library administrator.")
                                if nameofbook in booksrepeat:
                                    print ("Sorry, someone just took the last coppy. Try finding another book.")
                                else:
                                    datadata = ID + nameofbook
                                    datalist.append (ID)
                                    datalist.append (nameofbook)
                                    datalist.append ('|')
                                    data.append (datadata)
                                    usr.append (datadata)
                                    repeat.append (ID)
                                    if nameofbook == '':
                                        print ("ERROR!Please enter a valid book name!!!")
                                    n_check.append (nameofbook)
                                    booksrepeat.append (nameofbook)
                                    print ("Your request has been processed.")
                            else:
                                print ("You haven't returned your previous book. Please select the return a book option to proceed...")
                        elif option == '2' :
                            r_nameofbook = input ("Please enter the name of the book: ")
                            if r_nameofbook == '':
                                    print ("ERROR!Please enter a valid book name!!!")
                            if r_nameofbook in n_check  :
                                if ID in check :
                                    r_ask1 = ID
                                    r_ask2 = r_nameofbook
                                    r_data = r_ask1 + r_ask2
                                    if r_data in data:
                                        n_check = []
                                        check = []
                                        repeat.remove (ID)
                                        data.remove (r_data)
                                        print ("Successfully returned book. Please come again.")
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
                            if st == '2':
                                print ("This option is for library administrators only, please contact your library administrator to access.")
                                usrname = input ("Username: ")
                                password = input ("Password: ")
                                if usrname == 'user' and password == '123' :
                                    while adminask != '9':
                                        print ("(1)Check usr ID and book borrowed\n(2)Force return\n(3)Block account\n(4)Block book\n(5)Unblock account\n(6)Unblock book\n(7)Change username\n(8)Change password\n(9)Exit")
                                        adminask = input ("Please select an option: ")
                                        if adminask == '1':
                                            print (datalist)
                                        elif adminask == '2':
                                            repeat.remove (ID)
                                            print ("Force return successfull.")
                                        elif adminask == '3':
                                            IDforbid = input ("ID to forbid: ")
                                            IDforbidlist.append (IDforbid)
                                        elif adminask == '4':
                                            bookforbid = input ("Book to forbid: ")
                                            bookforbidlist.append (bookforbid)
                                        elif adminask == '5':
                                            try:
                                                IDunforbid = input ("Account to allow: ")
                                                IDforbidlist.remove (IDunforbid)
                                            except:
                                                print ("Account has not been blocked. Cannot unblock.")
                                        elif adminask == '6':
                                            try:
                                                bookunforbid = input ("Book to allow: ")
                                                bookforbidlist.remove (bookunforbid)
                                            except:
                                                print ("Book has not been blocked. Cannot unblock.")
                                        elif adminask == '7':
                                            usernamecheck = input ("Please enter pprevious username to make changes: ")
                                            if usernamecheck == usrname:
                                                new = input ("New username: ")
                                                usrname == new
                                            else:
                                                print ("Access denied")
                                        elif adminask == '8':
                                            passwordcheck = input ("Please enter previous password to make changes: ")
                                            if passwordcheck == password:
                                                pnew = input ("New password: ")
                                                password == pnew
                                            else:
                                                print ("Access denied")
                                        elif adminask == '9':
                                            print ("Saving changes....................\nExiting....................")
                                    else:
                                        print ("Plese select an existing option...!")
                                else:
                                    print ("Access denied, please contact your library administrator.")
                            else:
                                print ("This option is for Library Administrators only.")
                        elif option == '5':
                            print ("Thank you for using LMS, please come again!!!")
                        else :
                            print ("ERROR! Option not found. Please select an existing option!!!")
    elif enter == 'n' :
        print ("Thank you for comming, please come again.")
        break
    else :
        print ("Plese select an existing option...!\nExiting...")
print ("Library System Management (LMS)\nCredits:\n\tAnderson.C")