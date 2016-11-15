# Exercise No.   1
# File Name:     FibonacciSequence.py
# Programmer:    Kendra Steitz
# Date:          October 22, 2016
#
# Problem Statement:
#   Program computes and outputs the Fibonacci number of the
#   users choice.
#
# Overall Plan:
#   1. Create a method fibonacciNumber that takes in a int value
#       and returns the fibonacci number value
#       - potential errors to account for - number being less than 1
#   2. In method, if number is one return one, otherwise create while loop
#       to find the fibonacci value and return it
#   3. In main, ask user for position of fibonacci value to retrieve
#   4. Call method entering the value from user into argument
#   5. Output to user the fibonacci number value
#

def fibonacciNumber(number):

    numb1 = 0
    numb2 = 1
    i = 0
    if number == 1:
        return 1

    elif number < 1:
        print("You need to pick a positive value.")

    else:
        while i < number - 1:
            numb3 = numb1 + numb2
            numb1 = numb2
            numb2 = numb3
            i += 1

        return numb3

def main():

    fibNumber = eval(input("Enter Fibonacci Number place to retrieve: "))
    print()
    print("The Fibonacci Number value is:", fibonacciNumber(fibNumber))

main()

