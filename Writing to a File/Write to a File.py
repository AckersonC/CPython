filename = "greeting.txt"
accessMode = "w"
myFile = open (filename, accessMode)
myFile.write ("Greetings, how are you?\n")
myFile.write ("Are you well?")
myFile.close()