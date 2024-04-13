x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

def add(a, b):
    sum = a + b # Adding the two numbers
    return sum # Returning the result

print(f"The sum of {x} and {y} is {add(x, y)}.")