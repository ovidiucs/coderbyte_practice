def StringScramble(str1,str2):

    ll = (set(str1) & set(str2))
    # for n in ll:
    #     if n in str1 or str2:
    #         print 'f',n

    if len(ll ^ set(str2)) and len(ll ^ set(str1)):
        return 'false'
    return 'true'
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print StringScramble(raw_input())     

# not working
