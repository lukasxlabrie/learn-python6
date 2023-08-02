# defines a var
types_of_people = 10
# f string AKA Format, allows Var to print in string with {} string here is a var
x = f"There are {types_of_people} types of people."
# defines 2 var
binary = "binary"
do_not = "don't"
# y is a var using two previous vars also an F string
y = f"those who know {binary} and those who {do_not}." 
# These tell the program to output data AKA print to terminal
print(x)
print(y)
# These are both f strings that print previously assigned var in a new statment
print(f"I said: {x}")
print(f"I also said: '{y}")
#This is a new Var
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}" #not sure why but adding the {} adds false to the output
# This print the @ var above and inserts False, I think {} takes the .format from the print command
print(joke_evaluation.format(hilarious))
# Defines 2 vars
w = "This is the left side of..."
e ="a string with a right side."
# Prints on one line beacuse they are asssigned the same line
print(w + e)