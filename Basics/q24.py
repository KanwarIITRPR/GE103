temp_statement = input("Enter the temperature(ex: 98F or 40C): ").lower()
temp = float(temp_statement[:-1])

if temp_statement[-1] == "f":
    print(f"{temp_statement.upper()} is the same as {(temp-32)*5/9}C")
elif temp_statement[-1] == "c":
    print(f"{temp_statement.upper()} is the same as {((temp)*9/5+32)}F")