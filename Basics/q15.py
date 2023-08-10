s = input("Enter a string to check for palindrome: ")

if s == s[::-1]:
		print("The string you entered is a palindrome.")
else:
		print("The string you entered is not a palindrome.")
