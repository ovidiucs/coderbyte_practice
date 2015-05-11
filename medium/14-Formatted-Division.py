__author__ = 'ovidiucs'
"""
Using the Python language, have the function FormattedDivision(num1,num2) take
both parameters being passed, divide num1 by num2, and return the result as a
string with properly formatted commas and 4 significant digits after the decimal
place. For example: if num1 is 123456789 and num2 is 10000 the output should
be "12,345.6789". The output must contain a number in the one's place even
if it is a zero.
"""
def FormattedDivision(num1,num2):

  return "{0:,.4f}".format(num1 / float(num2))


# keep this function call here
# to see how to enter arguments in Python scroll down
print FormattedDivision(2,3)
print FormattedDivision(10,10)
print FormattedDivision(123456789, 10000)

# Input = 2 & num2 = 3Output = "0.6667"
# Input = 10 & num2 = 10Output = "1.0000"
