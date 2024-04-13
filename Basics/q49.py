file = open("output.txt", "r") # Opening a file in with the required name - in Read-Only mode

contents = file.read().strip() # Reading the contents of the file and removing any extra spaces at the end that were left out, using .strip()
lines = contents.split("\n") # Splitting the contents with respect to "\n" - as this denotes the start of new line and we have to print the contents of the file line by line

for i in lines:
    print(i) # Printing the lines present in the file one by one

file.close() # Closing the file to signify the end of reading of file