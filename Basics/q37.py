import random

n = int(input("Enter a number: "))

# Making n bins
bin_holder = []
for i in range(n):
    bin_holder.append(0) # Setting bin as 0s to simplify the code

print(bin_holder)

# Throwing n identical balls into n bins randomly
# Also simultaneously counting the number of balls that are thrown
balls_thrown = 0
while bin_holder.count(0) != 0: # Executing code till there are no bins with 0 balls
    index = random.randint(0, n-1) # Seecting a random "bin"
    bin_holder[index] += 1 # "Adding" a ball into the "bins" - basically keeping count of number of balls that were thrown into a bin by giving the bin a number

    balls_thrown += 1 # Counts the number of balls that are thrown
    # print(balls_thrown, ":", bin_holder)

print(f"The total number of balls that were thrown are {balls_thrown}.")