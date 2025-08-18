#Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.
# ============================================
# Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
# Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
# Output: Display the calculated distance between the two points.

#input
import math
x1 = float(input("Enter x1 coordinate:"))
y1 = float(input("Enter y1 coordinates:"))

x2 = float(input("Enter x2 coordinates:"))
y2 = float(input("Enter y2 coordinates:"))

#processing
Distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#output
print("The distance between the two points is:", Distance)