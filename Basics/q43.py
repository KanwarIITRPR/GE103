import csv

file = open("GE103/CSVForDate.csv", "r+") # Opening the csv file as a Read-Only File
contents = csv.reader(file) # Storing the contents of the file in a variable - though doesn't represent the excat data - just points to a csv object

dates = [] # Adding the dates of the stock entries into the list
closing = [] # Adding the prices of the stocks in the list with corresponding day
iterations = 0 # Using "iterations" variable to skip stroing the heading of the csv table
for i in contents:
    if iterations == 1:
        dates.append(i[0])
        closing.append(float(i[4]))
    else:
        iterations = 1

file.close() # Closing the file so as to work with stored data

def minima_and_maxima(l): # Writing a program to find when the stocks are "locally" maximum and "locally" minimum - so as to buy at minimums and sell at maximums
    extremums = [] # A list to store the extremums and other normal points
    # Adding 1 for a maximum, -1 for a minimum and 0 for none of those

    # Checking if the first value is a maximum, minimum or none - by checking only one value - i.e., the next value by comparing it with the first value
    if l[0] > l[1]:
        extremums.append(1)
    elif l[0] < l[1]:
        extremums.append(-1)
    else:
        extremums.append(0)

    # Checking if other numbers are maximum, minimum or none - by comparing the value before and after it 
    for i in range(1, len(l) - 1):
        if l[i - 1] < l[i] and l[i] > l[i + 1]:
            extremums.append(1)
        elif l[i - 1] > l[i] and l[i] < l[i + 1]:
            extremums.append(-1)
        else:
            extremums.append(0)

    # Checking if the first value is a maximum, minimum or none - by checking only one value - i.e., the next before by comparing it with the last value
    if l[-1] > l[-2]:
        extremums.append(1)
    elif l[-1] < l[-2]:
        extremums.append(-1)
    else:
        extremums.append(0)

    return extremums # Returning the final list containing the information of mins and maxs

extremums = minima_and_maxima(closing)

# Removing possibilities of having a rise (maximum) initially and dip (minimum) finally
# This will effect as we don't want to buy at rise initially, nor do we want to sell at dip at last
if extremums.index(1) < extremums.index(-1): # If "1" occurs before "-1" initially - i.e. if rise occurs before dip initially
    extremums = extremums[extremums.index(1) + 1:] # Removing the extra rise
if extremums[::-1].index(1) > extremums[::-1].index(-1): # If "-1" occurs before "1" at last - i.e. if dip occurs after rise at last
    extremums = extremums[:len(extremums) - extremums[::-1].index(-1) - 1] # Removing the extra dip

extremums_copy = extremums[:] # Creating a copy of extremums so as to preserve the list and ensure that original list doesn't get lost

money = 100000 # Starting money
indices_iterated = 0 # To keep a track of indices for checking in the copiedextremums - as the list "extremums" gets shortened in length as we progress thus losing the exact price values

while extremums.count(1) != 0:
    nearest_local_max = closing[indices_iterated + extremums.index(1) + 1] # Defines the nearest local maximum
    nearest_local_min = closing[indices_iterated + extremums.index(-1) + 1] # Defines the nearest local minimum
    money = money*(nearest_local_max/nearest_local_min) # Final price after buying at dip and selling at rise
    
    print(f"Buy the stocks on {dates[indices_iterated + extremums.index(-1) + 1]} and then sell on {dates[indices_iterated + extremums.index(1) + 1]}.")

    indices_iterated_currently = extremums.index(1) + 1 # Indices we currently went through
    extremums = extremums[indices_iterated_currently:] # Defining a shorter, new extremums so as to get the new set of -1 and 1
    
    indices_iterated += indices_iterated_currently # Adding the current indices in the total indices traversed till now

print(f"At last, total money in hand after end of 30 years is: {money}.")