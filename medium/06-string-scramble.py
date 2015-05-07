def StringScramble(str1,str2):

    lst = list(str1)

    for i in str2:
        if i in lst:
            lst.remove(i)
            print lst
        else:
            return 'false'
    return 'true'

"""
Using the Python language,
have the function StringScramble(str1,str2)
take both parameters being passed and return
the string true if a portion of str1 characters
can be rearranged to match str2,
otherwise return the string false.
For example: if str1 is "rkqodlw" and str2 is "world"
the output should return true.
Punctuation and symbols will not be entered with the parameters.
"""
# keep this function call here  
# to see how to enter arguments in Python scroll down
print StringScramble("abcgggdfe","abcdef")
print StringScramble("h3llko","hello")
print StringScramble("coodrebtqqkye","coderbyte")
print StringScramble("heloooolwrdlla","helloworld")
print StringScramble("coamamaaqq","comma")
print StringScramble("letrrkakaeaaaqq","letter")
print StringScramble("aqwe","qa")
print StringScramble("yelowrqwedk","yellowred")
print StringScramble("cdore","coder")
print StringScramble("win33er","winner")
# Input = "cdore" & str2= "coder"Output = "true"
# Input = "h3llko" & str2 = "hello"Output = "false"