def PalindromeTwo(str):
    strg = ''.join(x for x in str.lower() if x.isalnum())
    if strg[::-1] == strg:
        return 'true'
    else:
        return 'false'
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PalindromeTwo(raw_input())        


