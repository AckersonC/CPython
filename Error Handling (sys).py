import sys
firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter first number: "))

try :
    result = firstNumber / secondNumber
    print (result)
except:
    error = sys.exc_info()[0]
    print ("Error, something went wrong...")
    print (error)