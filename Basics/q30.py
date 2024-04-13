import random

k = int(input("Enter the number of digits present in these numbers: "))
max_steps = 0
nums_with_highest_gcd = [] # Storing the numbers with highest GCD

def gcd(a, b, steps = 0): # Defining a recursive definition of GCD
    steps = steps + 1
    if a%b == 0:
        return b, steps
    else:
        return gcd(b, a%b, steps)
    
for i in range(10**(k - 1), 10**(k)):
    for j in range(10**(k - 1), 10**(k)):
        if i >= j: # Setting which number out of i and j is bigger
            a, b = i, j
        else:
            a, b = j, i

        hcf, steps = gcd(a, b)
        if steps > max_steps: # Setting max_steps being the largest number possible by comparing all values AND setting the numbers accordingly
            max_steps = steps
            nums_with_highest_gcd = [a, b]

print(f"The GCD of {k} digit numbers takes maximum steps when the numbers are {nums_with_highest_gcd[1]} and {nums_with_highest_gcd[0]}.")