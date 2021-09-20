country = input ("What country are you from?").lower()
pet = input ("What pet do you have?").lower()

countryiscorrect = False
if country == "canada" :
    countryiscorrect = True
    
petiscorrect = False
if pet == "moose" or pet == "beaver" :
    petiscorrect = True

if countryiscorrect and petiscorrect :
    print ("Do you play hockey too?")
    