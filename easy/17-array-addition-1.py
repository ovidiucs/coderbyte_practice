def ArrayAdditionI(arr):
    targetValue = max(arr)
    arr.remove(targetValue)
    mall = sum(arr)
    if targetValue <= mall:
        return 'true'
    else:
        return 'false'

# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArrayAdditionI(raw_input())
"""
Have the function ArrayAdditionI(arr) 
take the array of numbers stored in arr
 and return the string true if any combination 
 of numbers in the array can be added up to equal
the largest number in the array, otherwise return 
the string false. For example: if arr contains [4, 6, 23, 10, 1, 3]
the output should return true because 4 + 6 + 10 + 3 = 23. 
The array will not be empty, will not contain all
the same elements, and may contain negative numbers. 
"""
