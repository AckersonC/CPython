#Defines all variables 
monthlyPayment = 0
loanAmmount = 0
interestRate = 0
numberOfPayments = 0
#Prompt usr to input info
strloanAmmount = input ('Please enter your loan ammount >>>')
strinterestRate = input ('Please enter your interest rate >>>')
strnumberOfPayments = input ('Please enter the numbers of payments you want to make >>>')
#Set usrs input to a float
loanAmmount = float(strloanAmmount)
interestRate = float(strinterestRate)
numberOfPayments = float(strnumberOfPayments)
#Since payments are once per month, number of payments is number of years for the loan * 12
numberOfPayments = loanAmmount*12
#Standard calculation for all loan calculators
monthlyPayment = loanAmmount * interestRate * (1+ interestRate) * numberOfPayments \
    / ((1 + interestRate) * numberOfPayments -1)


#Output result to usr
print("Your monthly payment will be $%.2f" % monthlyPayment)
print ('Thank you for using LoanCalc')