ask = ()
wordlist = []
while ask != "0" :
    ask = input ("Words: ")
    wordlist.append (ask)
    print ("Enter 0 to stop!!!")
wordlist.sort()
wordlist.remove ("0")
print (wordlist)
