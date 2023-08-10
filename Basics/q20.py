lines = int(input("Enter the number of lines: "))
curve = int(input("Enter the amount of curvature: "))

mid = int(lines//2)

for i in range(1, lines + 1):
		y = int((((lines - mid - i)**2)*abs(curve))/4)
		y_max = int((((lines - mid - 1)**2)*abs(curve))/4)

		if curve > 0:
				print(" " * y + "*")
		else:
				print(" " * (y_max - y) + "*")
