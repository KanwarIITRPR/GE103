n = int(input("Enter the length of the Fibonacci Sequence: "))

a = 0
b = 1

for i in range(n):
		print(a)
		a, b = b, a + b
