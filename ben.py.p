from io import Writer
#Write a program that prints the following sentence 4 times:

print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")

#Writer code that calculates the result of:

# (99^3)*8 ,( 99 to the power of 3, times 8)

print((99**3)*8)

#Predict the output of the following code snippets:
# Comment what is your guess, then run the code and compare
#15<8
#False
print(15<8)

#5<3
#False
print(5<3)
#3=="3"
#True
print(3=="3")
#3==3
#True
print(3==3)
#3==4
#False
#"3"==3
#False
print("3"==3)
#"Hello'=="Hello"
#True
#Create a variable called computer_brand which value is the brand name of your computer.
computer_brand = "Dell"
#Using the computer_brand variable, print a sentence that states the following:
#"I have a <computer_brand> computer."
print(f"I have a {computer_brand} computer.")
#Create a variable called name, and set it’s value to your name.
name = "Alice"
print(f"Hello, my name is {name}.")

#Create a variable called age, and set it’s value to your age.
age = 30
print(f"I am {age} years old.")

#Create a variable called shoe_size, and set it’s value to your shoe size.
shoe_size = 9
print(f"My shoe size is {shoe_size}.")
#Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
info = f"I have a {computer_brand} computer, my name is {name}, I am {age} years old, and my shoe size is {shoe_size}."
print(info)