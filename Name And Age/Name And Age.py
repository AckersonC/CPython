fileName = "nameAndage.csv"
WRITE = "w"
myFile = open (fileName, mode = WRITE)
myFile.write ("Doyle McCarty, 27\n")
myFile.write ("Jodi Mills, 25\n")
myFile.write("Nicholas Rose, 32\n")
myFile.write ("Kian Goddard, 36\n")
myFile.write ("Zuha Hanania, 26")
myFile.close()