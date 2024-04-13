num = int(input("Enter the number for which you want its factorial: "))

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1) # Recursively goes through the function until the value of n becomes 1
    # When it hits n == 1, it returns 1 to the factorial(2) which further returns 2*1 in factorial(3) and this continues till n...

print(f"The factorial of {num} is {factorial(num)}.")