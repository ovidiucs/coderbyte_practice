def NumberAddition(str):
    d = []

    xc = list(str)

    try:
        while not xc[len(xc) - 1].isdigit() and len(xc) != 0:
            xc.pop(len(xc) - 1)
    except:
        return 0

    xs = "".join(xc)

    for ele in xs:
        if ele.isdigit():
            d.append(ele)
        else:
            d.append('+')

    f = "".join(d)
    return eval(f)

# keep this function call here  
# to see how to enter arguments in Python scroll down
print NumberAddition(raw_input())           

