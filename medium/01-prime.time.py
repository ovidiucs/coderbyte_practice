def PrimeTime(num):
    i = 2
    if num < 2:
        return 'false'
    while i < num:
        if num % i == 0:
            return 'false'
        else:
            i += 1
    return 'true'

# keep this function call here  
# to see how to enter arguments in Python scroll down
print PrimeTime(raw_input())           
"""
Have the function PrimeTime(num) take the num parameter being passed and return the string true if the parameter is a prime number, otherwise return the string false. The range will be between 1 and 2^16. 
"""
