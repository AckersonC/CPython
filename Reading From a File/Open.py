fileName = "Zoo.txt"
accessMode = "w"
myfile = open(fileName, accessMode)
myfile.write ("Tasmanian Devil, Endangered\n")
myfile.write ("Tasmanian Emu, Extinct\n")
myfile.write ("Tasmanian Tiger, Extinct\n")
myfile.write ("Possum, Common")
myfile.close()