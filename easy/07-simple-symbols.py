def SimpleSymbols(str):
    li = list(str)
    idx = 0

    while idx+1 < len(li):
        if li[idx] == '+':
            idx += 1
            if li[idx].isalpha():
                idx +=1
                if li[idx] == '+':
                    return "true"
                else:
                    return "false"
        elif li[idx].isalpha():
            return "false"
        idx+=1

print SimpleSymbols(raw_input())           
"""
Have the function SimpleSymbols(str) take the str parameter
being passed and determine if it is an acceptable sequence by either returning
the string true or false. The str parameter will be composed of + and = symbols with several
letters between them (ie. ++d+===+c++==a) and for the string to be true each
letter must be surrounded by a + symbol. So the string to the left would be false. 
The string will not be empty and will have at least one letter. 

"""
