
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
    mergeSort(numbers)

    num = linearSearch(21, numbers)
    num2 = binarySearch(21, numbers)
    print(num)
    print(num2)
    print(numbers[num])
    print(numbers[num2])

main()