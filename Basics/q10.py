from math import sqrt

n = int(input("Enter a number to check for prime: "))

res = "The number you entered is a prime."
for i in range(2, int(sqrt(n)) + 1):
		if n%i == 0:
				res = "The number you entered is not a prime."

print(res)
