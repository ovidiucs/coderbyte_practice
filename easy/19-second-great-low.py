def SecondGreatLow(arr): 
  alt = sorted(list(set(arr)))
  if len(alt) == 1:
    alt.append(alt[0])
  return ' '.join([str(alt[x]) for x in 1,-2])
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SecondGreatLow(raw_input())           

