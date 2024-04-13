str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

def concatenate(s1, s2):
    concatenated_string = s1 + " " + s2 # Puting the entered strings together by adding a space between them and then joining them together
    return concatenated_string

print(f"The concatenation of the string you entered has resulted in '{concatenate(str1, str2)}'.")