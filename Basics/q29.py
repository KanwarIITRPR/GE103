import math

decimal = int(input("Enter a decimal number: "))
binary = ""
power = math.floor(math.log(decimal, 2))

while power != -1:
    if decimal >= 2**power:
        decimal -= 2**power
        binary = binary + "1"
    else:
        binary = binary + "0"
    power -= 1
    
print(int(binary))