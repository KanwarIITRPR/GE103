n = int(input("Enter a number: "))
a = int(input("Enter a number for which is the divisor: "))
b = int(input("Enter another number for which is the divisor: "))

if n%a == 0 and n%b == 0:
    print(f"{n} is divisible both by {a} and {b}.")
else:
    print(f"{n} is not divisible both by {a} and {b}.")