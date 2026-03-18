#decleare a variable and asssing a value to it
first=print("Hello,world!")
#"This is a comment"
print("I AM A COMPUTER")
# Statement that check if 1>2and if 4>2
if 1 > 2:
    print("1 is greater than 2")
else:
    print("1 is not greater than 2")

if 4 > 2:
    print("4 is greater than 2")
else:
    print("4 is not greater than 2")
    "math is fun"
    nope=()
    #use the languages"and" operator to combine the language's"true" and "false" values
if True and False:
    print("This will not be printed")
if True and True:
    print("This will be printed")
    # calculate the length of a string "what;s my length?"
length=len("what's my length?")
print(length)
#convert the string"i am a shouting" to uppercase
shouting="i am a shouting"
print(shouting.upper())
#convert the string"1000"to the number 1000
number=int("1000")
print(number)
#commbine the number 4 with the string "real" to produce"4real"
combined=str(4)+"real"
print(combined)
#record the outputof the expression 3*"cool"
output=3*"cool"
print(output)
#record the output of the expression 1/0
try:
    result=1/0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    #determine the user for their name and store it in a variable called "name"
name=input("What is your name? ")
print("Hello, " + name + "!")
#ask the user for their number.if the number is negative,show a message that says"That number is less than 0!"if the number is positive,show a message that says"That number is greater than 0!"if the number is 0!"otherwise,show a message that says"you picked 0!"
number=int(input("Please enter a number: "))
if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")
    #find the index of "l"in"apple"
index="apple".find("l")
#check whether"y"is in "xylophone"
is_y_in_xylophone="xylophone".find("y") != -1
print(f"Index of 'l' in 'apple': {index}")
print(f"Is 'y' in 'xylophone'? {is_y_in_xylophone}")
#check whether the string called my_string is all in lowercase when you're ready,move on to list Basics
my_string="this is a lowercase string"
is_lowercase=my_string.islower()
print(f"Is my_string all lowercase? {is_lowercase}")
