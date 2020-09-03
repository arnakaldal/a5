# Design an algorithm that finds the maximum positive integer input by a user.  
# The user repeatedly inputs numbers until a negative value is entered.
# Make sure that you write up the algorithm before starting to code.
# Then implement the algorithm in Python. 
# Put your algorithmic description as a comment in the program file.

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

max_int = 0

while num_int >= 0:
    if num_int >= max_int:
        max_int=num_int
        num_int = int(input("Input a number: "))  
    else: 
        num_int = int(input("Input a number: "))  

print("The maximum is", max_int)    # Do not change this line