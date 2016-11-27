# Exercise No.   2
# File Name:     Palindrome.py
# Programmer:    Kendra Steitz
# Date:          November 25, 2016
#
# Problem Statement:
#   Allow user to enter a sentence and output to whether that sentence is a
#   palindrome or not.
#
# Overall Plan:
#   1. Strip sentence of all whitespace
#   2. Transfer to all lowercase
#   3. Strip sentence of all punctuation
#   4. Create function to find if sentence is a palindrome
#       Using recursion
#   5. Base case would be when sentence is less than 2 characters long
#       Which would make the sentence a Palindrome
#   6. Go through sentence and compare the first character against the
#       last character.  If they are not the same, the sentence is not
#       a palindrome.
#   7. If the sentence length is greater than 2 and the first and last
#       character are equal, call upon the palindrome function again
#       using the sentence with the first and last characters cut off
#

from string import punctuation


def palindrome(sentence):

    if len(sentence) < 2:
        print("Sentence is a Palindrome.")
    elif sentence[0] != sentence[-1]:
        print("Sentence is not a Palindrome.")
    else:
        palindrome(sentence[1:-1])


def main():

    sentence = input("Enter sentence: ")
    s = sentence.replace(" ", "")
    s = s.lower()
    s = ''.join(c for c in s if c not in punctuation)

    palindrome(s)

main()
