# Exercise No.   1
# File Name:     LinearVsBinary.py
# Programmer:    Kendra Steitz
# Date:          November 25, 2016
#
# Problem Statement:
#   Write functions for linear search and binary search.  Test each one out
#   using 5,000, 50,000, and 500,000 to experience first hand which the quicker
#   of the two are.
#
# Overall Plan:
#   1. Create function linearSearch(x, nums)
#   2. Create function binarySearch(x, nums)
#       for binary search, list has to be sorted - use the built-in python method
#   3. Create a function that makes a list of the size needed
#   4. Run program for each size list using linear search and binary search
#   5. Use timeit to time each function and output the seconds it took and
#       the amount of steps to find the number searched for
#

from random import randrange
import timeit


def linearSearch(x, nums):
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


def binarySearch(x, nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high)//2
        item = nums[mid]
        if x == item:
            return mid
        elif x < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def makeList():
    numbs = []
    i = 0
    while i < 500000:
        number = randrange(1, 1000000)
        numbs.append(number)
        i = i + 1

    # numbs.sort()
    return numbs


def main():

    numbers = makeList()

    start = timeit.default_timer()

    # Perform the search
    foundIt = linearSearch(17, numbers)
    # foundIt = binarySearch(17, numbers)

    # Stop the clock
    stop = timeit.default_timer()

    steps = linearSearch(17, numbers)
    # steps = binarySearch(17, numbers)

    # Print the time and number of steps it took
    if foundIt != -1:
        print("Search with 5000 items:", stop - start, "seconds (", steps, "steps )")
    else:
        print("Not in list")

main()
