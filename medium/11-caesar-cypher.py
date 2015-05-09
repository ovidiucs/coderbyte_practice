__author__ = 'ovidiucs'

"""
Using the Python language, have the function CaesarCipher(str,num) take the str
parameter and perform a Caesar Cipher shift on it using the num parameter as the
shifting number. A Caesar Cipher works by shifting each letter in the string N
 places down in the alphabet (in this case N will be num). Punctuation, spaces,
  and capitalization should remain intact. For example if the string is "Caesar
   Cipher" and num is 2 the output should be "Ecguct Ekrjgt".
"""
# Input = "Hello" & num = 4Output = "Lipps"
# Input = "abc" & num = 0Output = "abc"


def CaesarCipher(str, num):

    ax = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    s = []
    for i in str:
        if i in ax:
            # s.append(ax.index(i))
            s.append(ax.index(i) % len(ax))
        else:
            s.append(i)

    return s

# keep this function call here
# to see how to enter arguments in Python scroll down
print CaesarCipher("zaAZ", -1)

