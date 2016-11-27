# Exercise No.   1
# File Name:     sortingMethods.py
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
#   3.
#


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


def main():

    numbers = []
    numbers.append(10)
    mergeSort(numbers)

main()
