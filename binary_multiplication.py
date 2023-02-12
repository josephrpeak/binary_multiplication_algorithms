import booths_algorithm
import columncompression

while(True):
  choice = input("\n[1]: Booth's Algorithm (signed)\n[2]: Column Compression (unsigned)\n[3]: Quit\n")
  try:
    if(choice == '1'):
      booths_algorithm.main()
    elif(choice == '2'):
      columncompression.main()
    elif(choice == '3'):
      break
    else:
      raise ValueError
  except ValueError:
    print("Please make a valid entry.")

print("Thanks for using my program.")
