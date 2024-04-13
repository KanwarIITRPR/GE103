full_array = [-8, 8, 6, -6, -2, 3, -5, 2, 5] # Array which will used to solve the problem of finding maximum sumed sub-array
print(f"The array used is {full_array}.")

def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    
    current_sum, best_sum = 0, 0 # Initializing the values representing the sums counting in the current (continuous), and the best sum possible
    start_index, end_index = 0, 0 # Initializing the variables used to represent the starting and the ending index of the continuous sub-array in the original array
    temporary_start = 0 # Initializing the variable that represents a temporary start index - if this index provides higher sum, then used, else thrown

    for index in range(len(numbers)):
        if current_sum + numbers[index] > 0: # If the sum till the current index is net positive ("till the current index" is being measured from the point when current index is 0)
            current_sum += numbers[index] # Then, make the current_sum equal to sum being measured from its previous 0 till the given index
        else:
            current_sum = 0 # Else, set the current sum to 0 and restart the continuous counting process
            temporary_start = index + 1 # Set the temporary starting index to be the current value - will later make it permanent if the sum increase to be better than current sum

        if current_sum > best_sum:
            best_sum = current_sum # Setting the best sum to be equal to the current sum, if the current sum is more
            start_index = temporary_start # Setting the starting index to be the earlier defined temporary starting index - i.e., it finally resulted in a better net sum
            end_index = index # Setting the end index to the current index

    return best_sum, numbers[start_index:end_index + 1] # Returning the best possible sum and the continuous sub-array with the best possible sum

max_sum, sub_array = max_subarray(full_array)

if max_sum == 0 and 0 not in sub_array: # If the maximum sum is 0, then set the sub-array to be an empty list - if the sub-array is not [0]
    sub_array = []

print(f"The maximum attainable sum in a continuous sub-array is {max_sum}.")
print(f"The sub-array with the maximum attainable sum is {sub_array}.")