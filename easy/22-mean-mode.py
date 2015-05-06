def MeanMode(arr):
    mn = sum(arr) / len(arr)
    if arr.count(mn) > 1:
        return 1
    return 0

# keep this function call here  
# to see how to enter arguments in Python scroll down
print MeanMode(raw_input())           

