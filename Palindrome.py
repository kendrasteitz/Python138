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
#   1.
#
#

from string import punctuation

def palindrome(sentence):
    s = sentence.replace(" ", "")
    s = s.lower()
    s = ''.join(c for c in s if c not in punctuation)
    half = len(s) // 2
    firstPart = s[:half]
    secondPart = s[half:]

    new = ""
    i = 1
    while i <= half:
        new = new + (secondPart[len(secondPart) - i])
        i = i + 1

    if(firstPart == new):
        print(sentence, "is a Palindrome")
    else:
        print(sentence, "is not a Palindrome")


def main():

   sentence = input("Enter sentence: ")
   palindrome(sentence)

main()