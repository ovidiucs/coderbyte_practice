def DashInsert(str):
    ints = list(str)
    d = list(str)
    ls = []
    for el in enumerate(str):
        idx = el[0]
        eo = el[1]
        jt = (idx + 1) % len(str)
        yt = int(ints[jt])
        if int(eo) % 2:
            if yt % 2:
                ls.append(idx + 1)

    while len(ls) != 0:
        d[ls[0]:ls[0]] = ['-']
        ls.remove(ls[0])
        try:
            ls[0] += 1
            if d[(ls[0] - 1)] == '-':
                ls[0] += 1
        except:
            IndexError

    return "".join(d)

# keep this function call here  
# to see how to enter arguments in Python scroll down
print DashInsert(raw_input())
# needs redoing
