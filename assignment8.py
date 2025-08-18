#Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.
#=================================================
#Input: Ask the user to enter their marks for three subjects.
#Processing: Calculate the average of the marks. Determine the grade based on the average:
#90 and above: A
#80-89: B
#70-79: C
#60-69: D
#Below 60: F
#Output: Display the calculated grade.

#input
subject1 = float(input("Enter your mark for subject 1 (0-100):"))
subject2 = float(input("Enter your mark for subject 2 (0-100):"))
subject3 = float(input("Enter your mark for subject 3 (0-100):"))
#processing add all marks & divide by 3 to find average
average = (subject1 + subject2 + subject3) / 3
#make sure number is positive
if average < 0:
    if average >= 90:
        print(f"{average} Your Grade is an A")
    elif 89 <= average <= 80:
        print("B", average)
    elif 79 <= average <= 70:
        print(f"{average} Your Grade is a C ")
    elif 69 <= average <=70:
        print(f"{average} Your Grade is a D")
    elif average <= 60:
        print(f"{average} Your Grade is an F")

else:
    print("Please enter a positive number")