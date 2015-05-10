__author__ = 'ovidiucs'
"""
Using the Python language, have the function Consecutive(arr) take the array of
 integers stored in arr and return the minimum number of integers needed to
  make the contents of arr consecutive from the lowest number to the highest
  number. For example: If arr contains [4, 8, 6] then the output should be 2
  because two numbers need to be added to the array (5 and 7) to make it a
  consecutive array of numbers from 4 to 8. Negative numbers may be entered
  as parameters and no array will have less than 2 elements.
"""
def Consecutive(arr):

    return max(arr)-min(arr)-len(arr)+1



# keep this function call here
# to see how to enter arguments in Python scroll down
print Consecutive([5,10,15])
print Consecutive([4,8,6])
print Consecutive([-2,10,4])
# Input = 5,10,15Output = 8
# Input = -2,10,4Output = 10