import csv
import random
import matplotlib.pyplot as plt

file = open("GE103/SOCR-HeightWeight.csv", "r+") # Opening the csv file as a Read-Only File
contents = csv.reader(file) # Storing the contents of the file in a variable - though doesn't represent the excat data - just points to a csv object

# Storing all the exact values of the heights and weights in "data" list
data = []
iterations = 0 # Using this to avoid having the Titles of the columns stored in "Data"
for i in contents:
    if iterations == 1:
        data.append([float(i[1]), float(i[2])])
    else:
        iterations = 1

file.close() # Closing the file to proceed with the stored data

# error_check is a function which returns the relative error of a value inputed that is actually used to find the closest correlation value of heights and weights
def error_check(alpha):
    net_error = 0
    for i in data:
        net_error += abs(i[1] - alpha*i[0]) # Adds (weight - (value * height)) so as to note the error

    return net_error/len(data)

error_limit = 0.0001 # Used to stop the finding_alpha function recursion if the error gets below this threshold
def finding_alpha(mid = 5, r = 5): # mid and r are used to define the range in which we are going to produce random points and check them for least error
    test_points = [random.uniform(mid - r, mid + r) for i in range(1000)] # Produces 1000 points in between the provided range so as to check for their error

    min_error = error_check(test_points[0]) # Assuming a value with minimum error and checking if any other value has a lower error than this
    alpha = test_points[0]
    for i in test_points:
        current_error = error_check(i)
        if current_error < min_error: # If any other value has a lower error than the current minimum error, then we store its error as minimum error and that value as alpha
            min_error = current_error
            alpha = i

    print(alpha, min_error)

    # Checking if the lowest error found till now is less than or equal to the error threshold
    if min_error <= error_limit: # If yes, then the alpha (value for which the error is below the error threshold) is returned
        return alpha
    else: # else, we keep repeating this process until the minimum error is below the error threshold
        return finding_alpha(alpha, error_limit) # Though we provide more accurate range to work with with each recursion we are through
    
alpha = finding_alpha() # Setting alpha equal to the value which will give least error when tested for correlation
correlation = 1/alpha # Correlation value

plt.scatter([i[0] for i in data], [i[1] for i in data], s = 0.1) # Plotting all the data points - weight vs height

# Finding the center point pof the distribution (approximately) - works fine as the sample size of data is very large
average_x = 0
average_y = 0
for i in data:
    average_x += i[0]/len(data)
    average_y += i[1]/len(data)

# Finding the point which has maximum distance from the origin - so as to find the end point of the line we are going to plot
dist_max = data[0][0]**2 + data[0][1]**2 # Assuming some point's distance to be maximum
max_point_x = 0 # Setting the x coordinate of the maximum distance point
for i in data:
    current_dist = i[0]**2 + i[1]**2
    if current_dist > dist_max: # If the distance of the current point is more than the previously set maximum, then set the maximum distance to this current distance and setting the maximum x to this point
        dist_max = current_dist
        max_point_x = i[0]

max_point_y = average_y + alpha*(max_point_x - average_x) # Finding the corresponding maximum y corrdinate that lies on the line containing the center and having a slope alpha

# Finding the point which has minimum distance from the origin - so as to find the starting point of the line we are going to plot
dist_min = data[0][0]**2 + data[0][1]**2 # Assuming some point's distance to be minimum
min_point_x = 0 # Setting the x coordinate of the minimum distance point
for i in data:
    current_dist = i[0]**2 + i[1]**2
    if current_dist < dist_min: # If the distance of the current point is less than the previously set minimum, then set the minimum distance to this current distance and setting the minimum x to this point
        dist_min = current_dist
        min_point_x = i[0]

min_point_y = average_y + alpha*(min_point_x - average_x) # Finding the corresponding minimum y corrdinate that lies on the line containing the center and having a slope alpha

plt.plot([min_point_x, max_point_x], [min_point_y, max_point_y], color = "red", linewidth = "1.5") # Plotting the required line
plt.show()