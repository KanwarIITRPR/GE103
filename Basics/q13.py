str1 = input("Enter a string: ")
str2 = input("Enter another string of the same length: ")

for i in range(len(str1)):
		print(str1[i] + str2[i], end = "")
