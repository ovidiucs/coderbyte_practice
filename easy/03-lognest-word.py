def LongestWord(sen): 
  si = sen.split()
  return max(si, key=len)

    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())           


"""
Have the function LongestWord(sen) take the sen parameter being passed and return the 
largest word in the string. If there are two or more words that are the same length, return the 
first word from the string with that length. Ignore punctuation and assume sen will not be empty. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""
# needs work
