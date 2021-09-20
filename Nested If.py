GST = .05
HST = .13
PST = .06

country = input ("What country are you from?").upper() 
if country == "CANADA" :
    province = input ("Which province are you from?").upper()

ordertotal = float(input("What is your order total?"))



if country == "CANADA":
    if province == "ALBERTA" :
        ordertotal = ordertotal + ordertotal * GST
    elif province == "ONTARIO" or "NEWS BRUNSWICK" or "NOVA SCOTIA" :
        ordertotal = ordertotal + ordertotal * HST
    else :
        ordertotal = ordertotal + ordertotal * PST + ordertotal * GST

print("Your total including taxes comes to $%.2f " % ordertotal)
    


