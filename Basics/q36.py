import random

n = int(input("Enter a number: "))

# Making n bins
bin_holder = []
for i in range(n):
    bin_holder.append([]) # Adding n bins in a "room"

print(bin_holder)

# Throwing n identical balls into n bins randomly
for i in range(n):
    index = random.randint(0, n-1) # Decides a random bin in which the ball is to be put
    bin_holder[index].append("ball") # Adds a ball (represented by 1) to the randomly selected bin
    # print(i+1)
    print(i+1, bin_holder)

# Finding the maximum number of balls present in a bin
max_balls = 0 # Initiates the counting process
for i in bin_holder:
    if len(i) > max_balls: # Checks if the number of balls in current bin is greater than the balls present in the previous maximum
        max_balls = len(i)

print(f"The maximum number of balls in a bin are {max_balls}.")


# To check for the number of bins containing a specific amount of  -
# l = [0 for i in range(max_balls + 1)]

# for i in bin_holder:
#     l[len(i)] += 1

# for i, element in enumerate(l):
#     print(i, element)
