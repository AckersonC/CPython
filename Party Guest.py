guest = ()
guestlist = []

while guest != '0' :
    guest = input ('Who will come to your party? Enter 0 to stop... ')
    guestlist.append (guest)
guestlist.remove ('0')
guestlist.sort()
for guestlist in (guestlist) :
    print (guestlist)