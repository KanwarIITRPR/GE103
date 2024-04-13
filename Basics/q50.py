import math
import matplotlib.pyplot as plt

stamp = [[1, 1], [2, 1], [2, 2], [1, 2]] # Enters the basic stamp - i.e., the base case required for computing higher cases - aka "The Base Pattern"

numberRecurse = int(input("Enter a number: ")) # Taking in the number required for generating a consequent pattern

def RotateRight(obj): # "Rotates" the list (obj) towards it's right
    obj_copy = [i[:] for i in obj] # Copying the list - so to preserve the initial list
    size = int(math.sqrt(len(obj_copy))) # Defining the "size" of the pattern - i.e., the length of the square that will be so formed

    for i in obj_copy:
        i[0], i[1] = i[1], (size - 1) - (i[0] - 1) + 1 # Changing the points so as to give an effect of rotated-ness
        # Using the fact that 90 degree clockwise rotation has - 
        # x_new = y_old
        # y_new = - x_old
        ### Though, these are first mainpulated to get to the origin, then rotated 90 degrees, then returned back to (1, 1)

    obj_copy.reverse() # Reversing the "list" will create a sense of opposite flow of direction of the pattern - the correct way

    return obj_copy

def RotateLeft(obj): # "Rotates" the list (obj) towards it's left
    obj_copy = [i[:] for i in obj] # Copying the list - so to preserve the initial list
    size = int(math.sqrt(len(obj_copy))) # Defining the "size" of the pattern - i.e., the length of the square that will be so formed

    for i in obj_copy:
        i[0], i[1] = (size - 1) - (i[1] - 1) + 1, i[0] # Changing the points so as to ive an effect of rotated-ness
        # Using the fact that 90 degree anticlockwise rotation has - 
        # x_new = - y_old
        # y_new = x_old
        ### Though, these are first mainpulated to get to the origin, then rotated 90 degrees, then returned back to (1, 1)

    obj_copy.reverse() # Reversing the "list" will create a sense of opposite flow of direction of the pattern - the correct way

    return obj_copy

def SFC(n = numberRecurse - 1, obj = stamp): # Making the final pattern/list
    l = [] # List containing the final pattern
    n -= 1 # Number of times left to recurse thorugh
    size = int(math.sqrt(len(obj))) # Defining the "size" of the pattern - i.e., the length of the square that will be so formed

    if numberRecurse == 1: # If the initial value is 1, return the base case
        return stamp
    
    listL = RotateLeft([i[:] for i in obj]) # Rotates the list towards its left
    listR = RotateRight([i[:] for i in obj]) # Rotates the list towards its left

    # The pattern goes by having the left-rotated object, then a normal object shifted down by the object "size", then another noraml object shifted down and right by the object "size" and finally a right-rotated object shifted towards the right by object "size"
    for i in listL: # Adding the left-rotated object to the final list
        l.append(i)

    objC = [i[:] for i in obj]
    for i in objC: # Adding a normal object and shifting it down by "size"
        i[0] += (size - 1) + 1
        l.append(i)

    objC = [i[:] for i in obj]
    for i in objC: # Adding a normal object and shifting it down by "size" and shifting right by "size"
        i[0] += (size - 1) + 1
        i[1] += (size - 1) + 1
        l.append(i)

    for i in listR: # Adding a normal object and shifting it right by "size"
        i[1] += (size - 1) + 1
        l.append(i)

    if n == 0: # If all iterations are complete, then return the list
        return l
    else: # Else re-iterate
        return SFC(n ,l)

print(RotateRight(stamp))

pattern = SFC()
print(f"The final pattern is {pattern}.")

pattern_atq = RotateRight(pattern)

x_coor = [] # To plot graphs, noting all the x coordinates in order
y_coor = [] # To plot graphs, noting all the y coordinates in order
for i in pattern_atq:
    x_coor.append(i[0])
    y_coor.append(i[1])

plt.plot(x_coor, y_coor, marker = "o", ms = 1, mec = "r", mfc = "r") # Plotting the points with lines joining them as required in the question - with additional decorations
plt.show() # Showing the plot