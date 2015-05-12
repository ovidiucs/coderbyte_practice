__author__ = 'ovidiucs'
"""
Using the Python language, have the function CountingMinutes(str) take the str
parameter being passed which will be two times (each properly formatted with
a colon and am or pm) separated by a hyphen and return the total number of
minutes between the two times. The time will be in a 12 hour clock format.
For example: if str is 9:00am-10:00am then the output should be 60.
If str is 1:00pm-11:00am the output should be 1320.
"""


def CountingMinutes(str):
    t = str.split("-")
    # if g[0] and e[2] == 'p':
    #     x = 720 + 60 * g[0] + g[1]
    #     if g[2] and e[4] == 'p':
    #         pass
    #     else:
    #         c =  g[2]*60+g[3]

    return t

# keep this function call here
# to see how to enter arguments in Python scroll down
print CountingMinutes("1:30pm-9:00am")
# Input = "12:30pm-12:00am"Output = 690
# Input = "1:23am-1:08am"Output = 1425