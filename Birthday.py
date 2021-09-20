import datetime
currentdate = datetime.date.today()
userInput = input ('Please enter your birthday (mm/dd/yyyy)...... ')
birthday = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()
print (birthday)

days = birthday - currentdate
print (days.days)