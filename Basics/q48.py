n = int(input("Enter a natural number: ")) # Asking the natural number uptil which the numbers are to be put in the file

file = open("output.txt", "w") # Opening the file with the m=required file name - in Write-Only mode

for i in range(1, n + 1):
    file.write(str(i) + "\n") # Writing n natural numbers, one-by-one, to the opened file in each line
    # "Writing", though clears all the previous text and add new text as specified

file.close() # Closing the file to signify the end of the writing process