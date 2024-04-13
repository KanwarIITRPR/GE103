n = int(input("Enter a number to check if its even: "))

def is_even(num):
    if num%2 == 0: # Checking if the number gives a remainder of 0 when divided by 2
        return True
    else:
        return False
    
print(is_even(n)) # Printing the result of the function