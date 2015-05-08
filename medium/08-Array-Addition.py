__author__ = 'ovidiucs'
"""
Using the Python language, have the function ArrayAddition(arr) take the array
of numbers stored in arr and return the string true if any combination of numbers
in the array can be added up to equal the largest number in the array, otherwise
return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the
output should return true because 4 + 6 + 10 + 3 = 23. The array will not be
empty, will not contain all the same elements, and may contain negative numbers.
"""
# Input = 5,7,16,1,2Output = "false"
# Input = 3,5,-1,8,12Output = "true"
def ArrayAddition(arr):
    m = max(arr)
    arr.remove(max(arr))
    l = sum(arr)
    if l % m in arr or l == m:
        return "true"
    else:
        return "false"


# keep this function call here
# to see how to enter arguments in Python scroll down
print ArrayAddition([3,5,-1,8,12])
print ArrayAddition([4, 6, 23, 10, 1, 3])
print ArrayAddition([5,7,16,1,20])
# ha :) missed theese
print ArrayAddition([10,20,30,40,100])
print ArrayAddition([31,2,90,50,7])