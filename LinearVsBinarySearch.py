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
#       for binary search, list has to be sorted - use pythons sorting
#   3. Create a function that makes a list of the size needed
#   4. Run program for each size list using linear search and binary search
#   5. Take note of differences, if any
#

from random import randrange


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
        number = randrange(1, 100000)
        numbs.append(number)
        i = i + 1

    return numbs


def main():

    numbers = makeList()

    num = linearSearch(21, numbers)
    num2 = binarySearch(21, numbers)
    print(num)
    print(num2)
    print(numbers[num])
    print(numbers[num2])

main()
