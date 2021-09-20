import datetime
currentTime = datetime.datetime.now()
print (datetime.datetime.strftime(currentTime, '%H : %M'))
#H = hours 24 hours clock
#I = 12 hours clock
#p = am or pm
#m = Minutes
#S = seconds
print (currentTime.hour)
print (currentTime.minute)
print (currentTime.second)

