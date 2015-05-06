def SwapCase(str):
    d = []
    for letter in enumerate(str):
        if letter[1].isupper():
            d.append(letter[1].lower())
        else:
            d.append(letter[1].upper())

    return "".join(d)
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SwapCase(raw_input())           

