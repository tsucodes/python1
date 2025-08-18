'''
Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.
=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle.
'''

#input
length = int(input("Enter length: "))
width = int(input("Enter width: "))

#processing
area = length * width

#output
print("The calculated area of a rectangle is: ", area)


