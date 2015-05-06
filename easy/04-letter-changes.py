def LetterChanges(str):
    nstr = list(str)
    indx = ['a', 'e', 'i', 'o', 'u']
    ns = list()

    for y in nstr:
        if y.isalpha():
            y = chr(ord(y) + 1)
            if y in indx:
                s = y.upper()
                ns.append(s)
            else:
                ns.append(y)
        else:
            ns.append(y)

        xs = ''.join(ns)

    return xs


print LetterChanges(raw_input())
"""
Have the function LetterChanges(str) take the str parameter being
passed and modify it using the following algorithm. Replace every
letter in the string with the letter following it in the alphabet
(ie. c becomes d, z becomes a). Then capitalize every vowel in
this new string (a, e, i, o, u) and finally return this modified string. 

Use the Parameter Testing feature in the
box below to test your code with different arguments.

"""
