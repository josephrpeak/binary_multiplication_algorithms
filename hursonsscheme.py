# -*- coding: utf-8 -*-
"""HursonsScheme

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/145q49Jv49RDSt6oIqXNbUkOz-KYNbUPb
"""

'''from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')'''

def generateSummands(a, b):
  zeroes = '0' * len(a)
  summands = []
  for i in range(1, len(b)+1):
    if(b[-i] == '0'):
      summands.append(zeroes)
    else:
      summands.append(a)

  return summands

def createStacks(summands, direction):
  stacks = []
  current_stack = ""

  if(direction == "left"):
    for i in range(len(summands[0])):
      for j in range(len(summands)):
        current_stack += summands[j][-i-1]
      stacks.append(current_stack)
      current_stack = ""

  elif(direction == "right"):
    for i in range(len(summands[0])):
      for j in range(len(summands)):
        current_stack += summands[-j-1][i]

      stacks.append(current_stack)
      current_stack = ""

  return stacks

def convertLongform(lst):
  for i in range(len(lst)):
    lst[i] = '.' * (len(lst) - i - 1) + lst[i] + '.' * i

  return lst

def deleteZeroes(lst):
  for i in range(len(lst)):
    lst[i] = list(lst[i])
    for j in range(len(lst[0])):
      if(lst[i][j] == '0'):
        lst[i][j] = '.'

    lst[i] = "".join(lst[i])

  return lst

def moveToFront(stack):
  for i in range(len(stack)):
    count = 0
    stack[i] = list(stack[i])
    for j in range(len(stack[0])):
      if(stack[i][j] == '1'):
        count += 1
        stack[i][j] = '.'
      if(count == 0):
        stack[i][0] = '0'
    for k in range(count):
      stack[i][k] = '1'
    
    stack[i] = "".join(stack[i])

  return stack
    
def generateCarryList(lst):
  count = 0
  carry = 0
  carry_list = []

  for i in range(len(lst[0])):
    count = 0
    for j in range(len(lst)):
      if(lst[j][-i-1] == '1'):
        count += 1

    carry_list.append(count)

  for i in range(len(carry_list)-1):
    carry_list[i+1] += carry_list[i] // 2

  return carry_list

def generateResult(lst, carry_list):
  answer = ""
  count = 0

  for i in range(len(lst)):
    lst[i] = list(lst[i])
    for j in range(carry_list[i]):
      lst[i][j] = '1'
      if(carry_list[i] == 0):
        lst[i][0] = '0'
    lst[i] = "".join(lst[i])

  if(carry_list[-1] > 1):
    lst.append('1' + '.'*(len(lst[0])-1))
    
  lst = createStacks(lst, "right")
  
  print("\nWith Carries:")
  display(lst)

  for i in range(len(lst[0])):
    for j in range(len(lst)):
      if(lst[j][-i-1] == '1'):
        count += 1
    if(count % 2 == 0):
      answer += '0'
    else:
      answer += '1'
    count = 0
  return answer
        
def display(lst):
  print('='*30)
  for elm in lst:
    print(elm)

def main():

  a = input("Enter first binary number: ")
  b = input("Enter second binary number: ")

  summands = generateSummands(a, b)
  summands = convertLongform(summands)

  print("\nMatrix of Summands:")
  display(summands)

  nozeroes = deleteZeroes(summands)

  stacks = createStacks(summands, "left")

  one_stacks = moveToFront(stacks)

  original_shape = createStacks(one_stacks, "right")

  print("\nPartial Products Without Zero Elements:")
  display(original_shape)

  carry_list = generateCarryList(original_shape)

  with_carries = createStacks(original_shape, "left")

  result = generateResult(with_carries, carry_list)

  print('\nResult: ' + result[::-1])


if __name__=="__main__":
  main()