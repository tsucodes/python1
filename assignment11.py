
"""
   Instructions
Challenge: Use a loop structure to generate the Collatz sequence until it reaches 1. Handle cases where the user enters a non-numeric input.
=================================
Description: Write a program that generates the Collatz sequence for a given positive integer entered by the user. The Collatz sequence is generated iteratively by repeatedly applying the following rules:
If the current number is even, divide it by 2.
If the current number is odd, multiply it by 3 and add 1.

"""

# This is the input section
#Prompt the suer to enter a positive number

user_input = input("Enter a positive number:")

#check if the input is numeric and convert it to an

while True:
    if user_input.isdigit():
        number = int(user_input)
        if number > 0:
            break

        else:
            user_input = input("The number must be a positive integer.Enter again:")
    else:
            user_input = input("Invalid input. Please enter a positive number:")

#generate and print the collatz sequence

print("collatz sequence")
while number != 1:
    print(number, end=" -> ")
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1