n = int(input("Enter a number: "))
i = int(input("Enter the starting number for the multiplication table: "))
j = int(input("Enter the ending number for the multiplication table: "))

for x in range(i, j + 1):
		print(n, "x", x, "=", n*x)
