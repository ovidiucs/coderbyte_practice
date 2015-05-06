def AdditivePersistence(num):
    counter = 0
    ss = num

    while ss >= 10:
        if ss >= 10:
            counter += 1
            ss = mpp(ss)
    if ss < 10 and num < 10:
        return 0
    if ss < 10:
        return counter

    return counter


def mpp(nm):
    nm = map(int, str(nm))
    return sum(nm)

# keep this function call here  
# to see how to enter arguments in Python scroll down
print AdditivePersistence(raw_input())           

