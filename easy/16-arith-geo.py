def ArithGeo(arr):
    diff = arr[1] - arr[0]
    div = float(arr[1]) / float(arr[0])
    for index in range(len(arr) - 1):
        if not (arr[index + 1] - arr[index] == diff):
            for index2 in range(len(arr) - 1):
                if not float((arr[index2 + 1]) / float(arr[index2]) == div):
                    return -1
            return 'Geometric'
    return 'Arithmetic'

# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArithGeo(raw_input())
"""
Have the function ArithGeo(arr) take the array of numbers stored in arr
and return the string "Arithmetic" if the sequence follows an arithmetic
pattern or return "Geometric" if it follows a geometric pattern. 
If the sequence doesn't follow either pattern return -1. 
An arithmetic sequence is one where the difference between 
each of the numbers is consistent, where as in a geometric sequence, 
each term after the first is multiplied by some constant or common ratio. 
Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. 
Negative numbers may be entered as parameters, 0 will not be entered,
 and no array will contain all the same elements. 
"""
