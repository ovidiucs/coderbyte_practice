__author__ = 'ovidiucs'
"""
Using the Python language, have the function LetterCount(str) take the str
parameter being passed and return the first word with the greatest number of
repeated letters. For example: "Today, is the greatest day ever!" should return
greatest because it has 2 e's (and 2 t's) and it comes before ever which also
has 2 e's. '
If there are no words with repeating letters return -1. Words will be separated
by spaces.
"""


def LetterCount(str):
    s = str.split()
    di = {}
    so = []

    for element in s:
        for i in element:
            di[i] = di.get(i, 0) + 1
        so.append(di)
        di = {}

    for el in so:
        if any(i >= 2 for i in el.values()):
            return s[so.index(el)]
        # in el.values():
        #    return s[so.index(el)]
    return -1


# keep this function call here
# to see how to enter arguments in Python scroll down
print LetterCount("Today, is the greatest day ever!")
print LetterCount("Hello apple pie")
print LetterCount("No words")
# Input = "Hello apple pie"Output = Hello
# Input = "No words"Output = -1