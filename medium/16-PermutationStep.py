__author__ = 'ovidiucs'
import itertools
"""
Using the Python language, have the function PermutationStep(num) take the num
parameter being passed and return the next number greater than num using the
same digits. For example: if num is 123 return 132, if it's 12453 return 12534.
 If a number has no greater permutations, return -1 (ie. 999).
"""
# Input = 11121Output = 11211
# Input = 41352Output = 41523
def PermutationStep(num):

    nn = list(num)

    if len(nn) <=1:
        yield nn
    else:
        for n in PermutationStep(nn[1:]):
            for x in range(len(nn)):
                yield n[:x] + nn[0:1] + n[x:]



# code from
# http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python
# using yield Yield is a keyword that is used like return, except the function will return a generator.
#
# keep this function call here
# to see how to enter arguments in Python scroll down
print [x for x in PermutationStep("123")]
#print PermutationStep("41523")
#print PermutationStep("11211")