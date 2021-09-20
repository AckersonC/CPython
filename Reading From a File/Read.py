animalFile = open("Zoo.txt", "r")
#For reading one line at a time
#Change value in loop to print more lines
# for animals in range (4) :
#     firstanimal=animalFile.readline()
#     print (firstanimal)

#For reading all File Contents
AllFileContents = animalFile.read()
print (AllFileContents)
