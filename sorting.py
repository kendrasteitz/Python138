# Exercise No.   1
# File Name:     sortingMethods.py
# Programmer:    Kendra Steitz
# Date:          December 3, 2016
#
# Problem Statement:
#   Write functions for different sorting methods.  The selection sort,
#   merge sort, and then also use pythons standard sorting method and
#   compare them against each other sorting an array of 5,000, 50,000,
#   and 500,000
#
# Overall Plan:
#   1. Create function mergeSort
#   2. Create function selectionSort
#   3. Create a method to randomly assign numbers into an array of
#       size of your choosing
#   4. Test each method out using timeit
#

from random import randrange
import timeit


def merge(lst1, lst2, lst3):
    i1, i2, i3 = 0, 0, 0
    n1, n2 = len(lst1), len(lst2)

    while i1 < n1 and i2 < n2:

        if lst1[i1] < lst2[i2]:
            lst3[i3] = lst1[i1]
            i1 = i1 + 1
        else:
            lst3[i3] = lst2[i2]
            i2 = i2 + 1
        i3 = i3 + 1

    while i1 < n1:
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1

    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1


def mergeSort(nums):
    n = len(nums)
    if n > 1:
        m = n // 2
        nums1, nums2 = nums[:m], nums[m:]
        mergeSort(nums1)
        mergeSort(nums2)
        merge(nums1, nums2, nums)


def selSort(nums):

    n = len(nums)

    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1, n):
            if nums[i] < nums[mp]:
                mp = i

        nums[bottom], nums[mp] = nums[mp], nums[bottom]


def makeList():
    numbs = []
    i = 0
    while i < 5000:
        number = randrange(1, 10000)
        numbs.append(number)
        i = i + 1

    return numbs


def main():

    numbers = makeList()
    start = timeit.default_timer()
    selSort(numbers)
    stop = timeit.default_timer()
    print("")
    print("Sorting by selection sort with 5000 items:", stop - start, "seconds")
    print("")
    print("=====================================================================================")
    print("")
    numbers = makeList()
    start = timeit.default_timer()
    mergeSort(numbers)
    stop = timeit.default_timer()
    print("Sorting by merge sort with 5000 items:", stop - start, "seconds")
    print("")
    print("=====================================================================================")
    print("")
    numbers = makeList()
    start = timeit.default_timer()
    numbers.sort()
    stop = timeit.default_timer()
    print("Sorting by pythons standard sort with 5000 items:", stop - start, "seconds")
    print("")
    print("=====================================================================================")
    print("")

main()
