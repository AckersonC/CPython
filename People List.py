plist = []
people = ()
while people != "0" :
    people = input ("Who is in your list? Enter 0 to stop...")
    plist.append (people)

print (plist)

people2 = ()
while people2 != "0" :
    people2 = input ("Who do you want to remove? Enter 0 to stop...")
    plist.remove (people2)

print (plist)
