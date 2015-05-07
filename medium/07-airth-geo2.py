__author__ = 'mig'
"""
Using the Python language, have the function ArithGeoII(arr) take the array of
numbers stored in arr and return the string "Arithmetic" if the sequence follows
 an arithmetic pattern or return "Geometric" if it follows a geometric pattern.
 If the sequence doesn't follow either pattern return -1. An arithmetic sequence
 is one where the difference between each of the numbers is consistent, where as
 in a geometric sequence, each term after the first is multiplied by some
 constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric
  example: [2, 6, 18, 54]. Negative numbers may be entered as parameters,
  0 will not be entered, and no array will contain all the same elements.
"""
# Input = 5,10,15Output = "Arithmetic"
# Input = 2,4,16,24Output = -1

def ArithGeoII(arr):

    s = [abs(i) for i in arr]
    if range(s[0],max(s)+1,s[1] - s[0]) == s:
        return "Arithmetic"
    elif is_geometric(s):
        return "Geometric"
    return '-1'

def is_geometric(a):
    # set first test for first element
    r = a[1]/float(a[0])

    return all(a[i]/float(a[i-1]) == r for i in xrange(2,len(a)))

# keep this function call here
# to see how to enter arguments in Python scroll down
print ArithGeoII([3,6,9,12,15])
print ArithGeoII([2,6,18,54])
print ArithGeoII([1,5,9])
print ArithGeoII([-3,-4,-5,-6,-7])

# Basically, it calculates the ratio between the first
# two, and uses all to determine
# if all members of the generator are true.
# Each member of the generator is a boolean value representing
# whether the ratio between two numbers is equal to the ratio
# between the first two numbers.
