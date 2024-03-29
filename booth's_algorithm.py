def shift(B, AC):
  print(f"\n...SHIFTING...")
  combined = AC + B
  lst = []

  lst.append(combined[0])

  for i in range(len(combined)):
    lst.append(combined[i])

  lst = "".join(lst)

  return (lst)

def sub(A, AC):

  A = list(A)

  for i in range(len(A)):

    if A[i] == '1':
      A[i] = '0'
    else:
      A[i] = '1'

  A = "".join(A)
  length = len(A)
  A = bin(int(A,2) + 1)[2::]
  A = A.zfill(length)

  sum = bin(int(A, 2) + int(AC, 2))[2::]
  if(len(sum) > len(A)):
    sum = sum[1::]

  return sum.zfill(len(A))

def add(A, AC):

  sum = bin(int(A, 2) + int(AC, 2))[2::]
  if(len(sum) > len(A)):
    sum = sum[1::]

  return sum.zfill(len(A))

def display(AC, Q, E):
  print(AC, Q, E)

def main():

  A_str = input("Enter multiplicand in binary ")
  B_str = input("Enter multiplier in binary ")

  A = int(A_str)
  B = int(B_str)

  largest = max(len(A_str), len(B_str))

  SC = int(largest)

  AC = '0' * largest

  A = str(A).zfill(largest)
  B = str(B).zfill(largest)

  ACQ = AC + str(B) + '0'

  E = ACQ[-1]
  AC = ACQ[0:len(ACQ)//2]
  Q = ACQ[len(ACQ)//2:-1]

  ACQ = AC + Q + E
  
  print("\nINITIAL VALUES:")

  while(SC > 0):
    
    display(AC, Q, E)

    if(Q[-1] + E == '01'):
      AC = add(A, AC)
      print(f"\n...ADDING...")
      display(AC, Q, E)
    elif(Q[-1] + E == '10'):
      AC = sub(A, AC)
      print(f"\n...SUBTRACTING...")
      display(AC, Q, E)
    else:
      pass

    SC -= 1

    ACQ = shift(Q, AC)
    E = ACQ[-1]
    AC = ACQ[0:len(ACQ)//2]
    Q = ACQ[len(ACQ)//2:-1]

  print("\nANSWER:\n", end = '')
  display(AC, Q, E)
  
if __name__=="__main__":
  main()
