#Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.
# =======================================================
# Input: Prompt the user to enter a time duration in hours.
# Processing: Convert the time duration to minutes and seconds.
# Output: Display the converted time duration in minutes and seconds.

#input
hour = float(input("Enter time duration in hours:"))

#processing
minutes = hour * 60
seconds = minutes * 60

#output
print("is the same as",minutes,"minutes", "and", seconds, "seconds")
