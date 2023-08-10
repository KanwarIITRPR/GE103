s = input("Enter a string: ").lower()
vowels = ["a", "e", "i", "o", "u"]

vowelCount = 0
consonantCount = 0

for i in s:
		if i in vowels:
				vowelCount += 1
		elif i != " ":
				consonantCount += 1

print("The vowels present in string are", vowelCount)
print("The consonants present in string are", consonantCount)
print("The spaces present in string are", len(s) - consonantCount - vowelCount)
