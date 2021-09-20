#Python Self Presentation Program
#Prompt usr to input name into variable name
name = input ("What is your name?")
#Prompt usr to input age into variable name
age = input ("What is your age?")
#Prompt usr to input country into variable country
country = input ("What country do you live in?")
#Prompt usr to input favourite color into variable color
color = input ("What is your favourite colour?")
#Prompt usr to input favourite animal into variable animal
animal = input ("What is your favourite animal?")
#Prints all usrs input into a self presentation, fuctions are used to manipulate usr input...
print ("Hello, nice to meet you " + (name.capitalize()) +"." + " You are " + (age) + " years old " \
       + "." + " You live in " + (country.upper()) + "." + " Your favourite colour is " \
       + (color.lower()) + "." + "Your favourite animal is the "  + (animal.lower() + '.'))
#Backslash tells python that code continues on the next line...