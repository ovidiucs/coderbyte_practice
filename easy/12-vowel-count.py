def VowelCount(str):
    o = 0
    for i in "aeiou":
        o += str.count(i)

    return o

# keep this function call here  
# to see how to enter arguments in Python scroll down
print VowelCount(raw_input())
"""
Have the function VowelCount(str) take the str string parameter being passed and return the number of vowels the string contains (ie. "All cows eat grass" would return 5). Do not count y as a vowel for this challenge. 
"""
