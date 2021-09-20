#My Python Input Program
#Takes input from usr and insert it in to variable firstName
firstName = input('''What is your first name?''')
#Takes input from usr and insert it in to variable lastName
lastName  = input ('''What is your last name?''')
#print Hello with input form usr
print ('Hello ' + firstName + (' ') + lastName)
#print hello with input form usr with attributes to change variable to lowercase .lower() / uppercase .upper() and swapcase .swacase()
print ('Hello ' + firstName.lower() + (' ') + lastName.swapcase())