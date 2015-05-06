from math import sqrt
def PowersofTwo(num):
  if sqrt(num) % 2 == 0:
    return 'true'
  return 'false'
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PowersofTwo(raw_input())           
# needs work
