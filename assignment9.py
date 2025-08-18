'''
Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.
=====================================================
Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant.
'''

#input

single_ch = input("Enter a single character:")
#processing. variable to hold  vowels & consonant
vowels = "aeiou"
if len(single_ch) == 1:
    if single_ch in vowels:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Error: only enter 1 character")