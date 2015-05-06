from math import ceil

def DivisionStringified(num1,num2): 

  resultFloat = num1/float(num2)
  resultFloatInt = "{:,}".format(int(resultFloat // 1))
  if resultFloat <= 999:
    return int(ceil(resultFloat))
  else:
  	return resultFloatInt

# keep this function call here  
# to see how to enter arguments in Python scroll down
print DivisionStringified(raw_input())       
# not working
