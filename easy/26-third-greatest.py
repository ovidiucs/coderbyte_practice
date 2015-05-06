def ThirdGreatest(strArr):
    # code goes here
    d = []
    for i, v in enumerate(strArr):
        d.append((len(v)))

    return "".join(sorted(strArr, key=str.__len__, reverse=True)[2:3])

# keep this function call here  
# to see how to enter arguments in Python scroll down
print ThirdGreatest(raw_input())           

