import math
import matplotlib.pyplot as plt

numberRecurse = int(input("Enter the number of iterations: ")) # Taking in the number required for generating a consequent pattern
stamp = [[1, 1], [1, 2], [1, 3], [2, 3], [2, 2], [2, 1], [3, 1], [3, 2], [3, 3]] # Enters the basic stamp - i.e., the base case required for computing higher cases - aka "The Base Pattern"

def Mirror(obj): # Flips/Mirrors the "object" with respect to the y-axis
    obj_copy = [i[:] for i in obj] # Creating a copy of the "object" so as to preserve and make changes in another list
    size = int(math.sqrt(len(obj_copy))) # Defining the "size" of the pattern - i.e., the length of the square that will be so formed

    for i in obj_copy:
        i[0], i[1] = (size - 1) - (i[0] - 1) + 1, i[1] # Changing the points so as to give an effect of mirror-ness
        # Using the fact that mirror abou the y-axis has - 
        # x_new = - x_old
        # y_new = y_old
        ### Though, these are first mainpulated to get to the origin, then mirrored, then returned back to (1, 1)

    return obj_copy # Returning the mirrored object

def MakeList(n = numberRecurse - 1, l = stamp): # Making the final pattern/list
    pattern_list = [] # List that contains the resulting pattern
    n -= 1 # Number of times left to recurse through this function
    size = int(math.sqrt(len(l))) # Defining the "size" of the pattern - i.e., the length of the square that will be so formed

    if numberRecurse == 1: # If the initial value is 1, then return the base case
        return stamp

    for i in range(9): # Going through the total number of times we have to add "stamp" in some way - denotes the "points" where "stamps" are to be placed
        if i%2 == 0: # If the iteration value is even, let the object be appended as it is - just an observation - that if we go as in the direction of stamp, then each "even" iteration will have normal stamp
            list_to_be_appended = [i[:] for i in l]
        else: # If the iteration value is odd, let the object be appended by being mirrored - just an observation - that if we go as in the direction of stamp, then each "odd" iteration will have mirrored stamp
            list_to_be_appended = Mirror(l)

        # If the current iterations are present in the middle column, then reverse the direction of flow - as they are supposed to be rotated as the line/direction are changing direction
        if i >= 3 and i < 6:
            list_to_be_appended.reverse()

        for j in list_to_be_appended: # Adding the stamp by shifting it as per requirement
            # The stamp itsekf tells how much to be shifted - if we measure the relative position of each point with respect to (1, 1) {inital point}, then the distance they are away in each direction needs to be multiplied with the current size of the stamp so as to properly shift them
            j[0] += size * (stamp[i][0] - 1) 
            j[1] += size * (stamp[i][1] - 1)
            pattern_list.append(j)

    if n == 0: # If all iterations are complete, then return the list
        return pattern_list
    else: # Else re-iterate
        return MakeList(n, pattern_list)
    
pattern = MakeList()
print(f"The final pattern is {pattern}.")

x_coor = [] # To plot graphs, noting all the x coordinates in order
y_coor = [] # To plot graphs, noting all the y coordinates in order
for i in pattern:
    x_coor.append(i[0])
    y_coor.append(i[1])

plt.plot(x_coor, y_coor, marker = "o", ms = 1, mfc = "r", mec = "r") # Plotting the points with lines joining them as required in the question - with additional decorations
plt.show() # Showing the plot