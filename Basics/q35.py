length = int(input("Enter the term of the fibonacci sequence which you would want to know: "))

def fibonacci(a = 0, b = 1, n = length):
    n -= 1
    if n == 0:
        return a
    return fibonacci(b, a + b, n) # Takes in the variable n which decreases everytime the function recurses through itself
    # As n hits 0, it returns the value of the nth number of the fibonacci sequence that got accumulated all the way back

print(f"The {length}th term of the fibonacci sequence is {fibonacci()}.")