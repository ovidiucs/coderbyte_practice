"""
Have the function SimpleAdding(num)
add up all the numbers from 1 to num.
For the test cases, the parameter num will be any number from 1 to 1000. 
"""
def SimpleAdding(num):
    sumall = sum(range(1, num + 1))

    return sumall

# keep this function call here
# to see how to enter arguments in Python scroll down
print SimpleAdding(raw_input())           

