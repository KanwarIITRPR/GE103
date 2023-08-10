from math import sqrt

n = int(input("Enter a number: "))

for i in range(2, n + 1):
		res = 1
		for j in range(2,int(sqrt(i)) + 1):
				if i%j == 0:
						res = 0

		if res == 1:
				print(i)
