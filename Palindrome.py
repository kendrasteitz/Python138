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
#   4. Split sentence in half
#   5. Reverse the second part of the sentence
#   6. Compare the two halves
#       if they are equal to each other, it's a palindrome
#       if they are not equal, the sentence is not a palindrome
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

    if firstPart == new:
        print(sentence, "is a Palindrome")
    else:
        print(sentence, "is not a Palindrome")


def main():

    sentence = input("Enter sentence: ")
    palindrome(sentence)

main()