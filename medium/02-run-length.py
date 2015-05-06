def RunLength(str):
    di = list(str)
    ltst = []
    ct = 1
    while len(di) > 0:
        try:
            if di[0] == di[1]:
                ct += 1
            else:
                ltst.append(ct)
                ltst.append(di[0])
                ct = 1
        except:
            IndexError
        del di[0]

    ltst.append(ct)
    ltst.append(str[-1:])
    return "".join("{0}".format(n) for n in ltst)
    



# keep this function call here  
# to see how to enter arguments in Python scroll down
print RunLength(raw_input())           

