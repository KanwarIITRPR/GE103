n = int(input("Enter an year: "))

res = f"The year {n} is a leap year."

if n%4 == 0:
    if n%100 == 0:
        if n%400 == 0:
            pass
        else:
            res = f"The year {n} isn't a leap year."
    else:
        pass
else:
    res = f"The year {n} isn't a leap year."

print(res)