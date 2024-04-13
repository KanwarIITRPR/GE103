s = input("Enter a list of numbers separated by ',': ")
l = []

for i in s.split(","):
    l.append(int(i)) # Converting the string entries of numbers into integers and storing them in a list

def find_max(l):
    largest_num = 0

    for i in l:
        if i > largest_num: # Going through all the elements in the list and changing largest_num's value if a higher value is found in the list
            largest_num = i

    return largest_num

print(f"The largest number in the list that you entered is {find_max(l)}.")