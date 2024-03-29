import math

def generateSummands(a, b):
  zeroes = '0' * len(a)
  summands = []
  for i in range(1, len(b)+1):
    if(b[-i] == '0'):
      summands.append(zeroes)
    else:
      summands.append(a)

  return summands

def padOnes(ones, length):
  binary_ones = []

  for elm in ones:
    binary_ones.append(format(elm, f'0{length}b'))
  
  return binary_ones

def countOnes(summands):
  ones = []
  count = 0

  for i in range(len(summands[0])):
    for j in range(len(summands)):
      if(summands[j][-i-1] == '1'):
        count += 1
    ones.append(count)
    count = 0

  return ones

def convertLongform(lst):
  for i in range(len(lst)):
    lst[i] = '.' * (len(lst) - i - 1) + lst[i] + '.' * i

  return lst

def fullAdder(a, b, c):

  res = str(a)+str(b)+str(c)

  if(res == '000'):
    sum = 0
    carry = 0
  elif(res == '001' or res == '010' or res == '100'):
    sum = 1
    carry = 0
  elif(res == '011' or res == '101' or res == '110'):
    sum = 0
    carry = 1
  elif(res == '111'):
    sum = 1
    carry = 1

  return (int(sum), int(carry))

def generateResult(padded_ones):
  result = []
  result_string = ""
  carry = 0

  result.append(int(padded_ones[0][1]))

  for i in range(len(padded_ones)-1):
    ans = fullAdder(padded_ones[i][0], padded_ones[i+1][1], carry)
    result.append(ans[0])
    carry = ans[1]

  result.append(int(padded_ones[-1][0]))

  result = list(reversed(result))

  for elm in result:
    result_string += str(elm)

  return result_string

def main():
  a = input("Enter first binary number: ")
  b = input("Enter second binary number: ")
  
  print('\nMATRIX OF SUMMANDS\n')

  length = int(math.log(len(a), 2)) + 1

  summands = generateSummands(a, b)
  summands_longform = convertLongform(summands)
    
  for elm in summands_longform:
    print(elm)

  ones = countOnes(summands_longform)
  padded_ones = padOnes(ones, length)
  padded_ones_longform = convertLongform(padded_ones[::])
  count = 1

  while(length > 2):

    print(f'\nCOMPRESSION STAGE {count}\n')
    
    for elm in padded_ones_longform:
      print(elm)

    length = int(math.log(len(padded_ones[0]), 2)) + 1

    ones = countOnes(padded_ones_longform)
    padded_ones = padOnes(ones, length)
    padded_ones_longform = convertLongform(padded_ones[::])

    count += 1

  print(f'\nCOMPRESSION STAGE {count}\n')

  for elm in padded_ones_longform:
      print(elm)

  result = generateResult(padded_ones)

  print(f"\nRESULT: {result}\n")

if __name__=="__main__":
  main()
