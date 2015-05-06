def PrimeMover(num):
    n = 0
    for i in range(1,10000):
        if checkPrime(i):
            if n < num:
                n += 1
            else:
                return i
                break

def checkPrime(z):

    for j in range(2, z):
        if (z % j) == 0:
            return False
    return True

# keep this function call here  
# to see how to enter arguments in Python scroll down
print PrimeMover(raw_input())           

