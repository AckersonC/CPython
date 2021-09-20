#Printing Current Date
#Import class datetime
import datetime
#Configure the datetime class to todays date
currentdate = datetime.date.today()
#Print the variable currentdate
print (currentdate)
#Printing the current date with a different format
print (currentdate.strftime('%d %b, %Y'))
#strftime means make a string from time
# %d = day
# %b =  abbreviation for month
# %Y = 4 digit year
# %B = full month name
# %A = day of the week
# strftime.org for more