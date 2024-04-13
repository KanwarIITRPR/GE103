import sys
sys.setrecursionlimit(10**9)

letters = ["R", "U", "L", "D"] # Defining the letters required for the pattern
recurse_limit = 1000000

def spiral_maker(recurse_times = 0, spiral = "", recurse_through_list = 0):
    '''This recursion defines the making of the required pattern'''

    if recurse_times >= recurse_limit: # Checking if the amount of times we have recursed is greater than equal to the recursion limit we have set - so as to stop printing the pattern
        return spiral

    index = (recurse_through_list)%4 # Setting the index of the letter to be used from the list "letters"
    repeat_times = int(recurse_through_list//2) + 1 # Defining the number of times we have to repeat the letter we have chosen

    # If the number of times we have recursed till now and the number of letters we are going to add exceed our limit, then we are going to add the letters till the recurse limit is achieved
    if recurse_times + repeat_times >= recurse_limit: 
        spiral = spiral + (letters[index]) * (recurse_limit - recurse_times)
    else:
        spiral = spiral + (letters[index]) * repeat_times

    recurse_times = recurse_times + repeat_times # Adding the number of letters we have put in the resulting string "spiral"
    recurse_through_list = recurse_through_list + 1 # Adding the number of recursions we are through

    return spiral_maker(recurse_times, spiral, recurse_through_list)

print(spiral_maker())