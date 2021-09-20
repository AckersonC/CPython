import datetime


dateline = ""
finalDate = 0
Weeks = 0
Days = 0



currentdate = datetime.date.today()

dateline = input ('Please enter dateline e.x(mm/dd/yyyy) >>>')

daysToDateLine = datetime.datetime.strptime(dateline, '%m/%d/%Y').date()



finalDate = daysToDateLine - currentdate

Weeks = finalDate.days / 7

Days = finalDate.days%7

print("You have %d weeks" %Weeks + " and %d days " %Days + "until your deadline.")
