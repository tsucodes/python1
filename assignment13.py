#Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.
#===================================
#Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.


#input user enters string
input_value = input("Enter a word to check if it is a palindrome:")
#processing
# break input into individual characters. split string. use list to separate by character
# : are using for slicing -1 indicates backwards
# check to see if it is same backwards use operator ==
# if input is same forward and backward print palindrome
#challaenge use loop

#loop continues to execute as long as condition is true
while True:
    value = list(input_value)
    if value == value[::-1]:
        print("yes it is a palindrome")
        break
    else:
        print("Not a palindrome")
    break