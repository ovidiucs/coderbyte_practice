__author__ = 'ovidiucs'
"""
Using the Python language, have the function SimpleMode(arr) take the array of
numbers stored in arr and return the number that appears most frequently
(the mode). For example: if arr contains [10, 4, 5, 2, 4] the output should be 4.
If there is more than one mode return the one that appeared in the array first
(ie. [5, 10, 10, 6, 5] should return 5 because it appeared first).
 If there is no mode return -1. The array will not be empty.
"""


def SimpleMode(arr):

    di = {}
    for i in arr:
        di[i] = di.get(i, 0) + 1
    j = (di.values())

    print [di.get(i) for i in arr]
        #arr.remove(i)

    #print di.get(2),di.has_key(2), di.keys(), di.values(), di

# print arr.index(v)



# keep this function call here
# to see how to enter arguments in Python scroll down
print SimpleMode([5, 5, 2, 2, 2, 1])
# Input = 5,5,2,2,1Output = 5
# Input = 3,4,1,6,10Output = -1