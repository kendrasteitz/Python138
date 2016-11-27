# Exercise No.   Extra Credit
# File Name:     BaseConversion.py
# Programmer:    Kendra Steitz
# Date:          November 25, 2016
#
# Problem Statement:
#   Allow user to enter a number and a base for it.
#   Using recursion output the digits of that number using the base given
#
# Overall Plan:
#   1. ask user for number and base
#   2. call upon function baseConversion(num, base)
#   3. base case is when num//base equals 0
#       if it does get remainder of num (num % base) and append to list
#   4. else find number = num//base and the remainder (num % base)
#       call upon baseConversion function again inputting the calculated number
#       append the calculated remainder to the list
#   5. Once base case has been hit, output the digits of the original number one by one,
#       in order, from the list.
#


def baseConversion(num, base):

    digits = []
    if num//base == 0:
        remainder = num % base
        digits.append(remainder)
    else:
        number = num//base
        remainder = num % base
        baseConversion(number, base)
        digits.append(remainder)

    for i in digits:
        print(i, end=' ')


def main():

    print()
    number = eval(input("Enter number: "))
    base = eval(input("Enter base: "))

    print()
    baseConversion(number, base)
    print()

main()
