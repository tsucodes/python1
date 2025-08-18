'''
Challenge: Implement error handling to ensure that the user enters a positive integer for the age.
==================================
Input: Prompt the user to enter their age.
Processing: Classify the age into different categories:
Under 18: Minor
18-65: Adult
Above 65: Senior citizen
Output: Display the category based on the entered age
'''

#input
age_input = input("Enter your age:")

#processing. check if user enter a number
if age_input.isdigit():
    age = int(age_input)

#make sure age is positive
    if age > 0:
        #add classifications
        if age < 18:
            print("Minor")
        elif 18 <= age <= 65:
            print("Adult")
        else:
            print("Senior Citizen")
    else:

        print("Error: age must be a positive number.")
else:
    print("Error: Invalid Inout! Please enter a positive number.")