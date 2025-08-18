'''
Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.
=============================
Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest.
'''
#starting the input section
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the intrest rate: "))
time = float(input("Enter the time period:"))

#this is the processing section
simple_intrest = (principal * rate * time) / 100

#this is the output section
print("The calculated simple intrest is:", simple_intrest)
