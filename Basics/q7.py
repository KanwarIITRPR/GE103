a = int(input("Enter the starting number: "))
d = int(input("Enter the common difference: "))
b = int(input("Enter the ending/stopping number: "))

if (a <= b and d > 0):
		while a <= b:
				print(a, end = " ")
				a = a + d
elif (a >= b and d < 0):
		while a >= b:
				print(a, end = " ")
				a = a + d
else:
		print("Invalid input!")
