import random

list_to_be_used = [1, 4, 0, 2, 8, 5, 9, 6] # Defining the list for which the median is to be found

def find_median(l = list_to_be_used, shift = 0):
    pivot_element = random.choice(l) # Choosing a random element to "arrange" other elements about
    pivoted_list = [pivot_element] # Making the list which is "arranged" about the pivoted element and also adding the pivoted element before hand
    list_of_elements_other_than_pivot = l[:l.index(pivot_element)] + l[l.index(pivot_element) + 1:] # Adding all the element in the list except the chosen pivot element

    for i in list_of_elements_other_than_pivot: # Adding other elements in the final "arranged" list by comparing their values with the pivot element
        if i < pivot_element:
            pivoted_list.insert(0, i) # If smaller, then adding in front
        else:
            pivoted_list.append(i) # If bigger (or equal), then adding at the back

    left = pivoted_list[:pivoted_list.index(pivot_element)] # Defining that part of pivoted list, which is towards the left side of pivoted element
    right = pivoted_list[pivoted_list.index(pivot_element) + 1:] # Defining that part of pivoted list, which is towards the right side of pivoted element
    mid_index = int(len(list_to_be_used)//2) # Defining the index of the "middle element"
    # In case of odd length, it is easily defined - but for even length a technique has been used while taking the input
    # It first calculates one the medians of the even-lengthed list and then later removes that element and re-finds the median which will now turn out to be the only other median as the list now will be odd-lengthed
    # This works because when it goes through the first time, it the median found is actually the greater one (or even equal) to the smaller median and thus when removed and re-calculated, smaller median will then appear

    # Here, length of the list is same as the index of pivoted element in the pivoted list, i.e., len(left) = pivoted_list.index(pivot_element)
    if len(left) + shift > mid_index: # If the next net index goes beyond the middle index of the original list, then the median will be in the left side - thus set the chosen list to be left
        chosen_list = left
    elif len(left) + shift < mid_index: # If the next net index is less than the middle index of the original list, then the median will be in the right side - as the median will be in the list which is towards middle index - thus set the chosen list to be right
        chosen_list = right
        shift += len(left) + 1 # Changing the shift value when the chosen list is right so as to keep track of the index we have travesed with respect to the original list
    else: # If the middle index is same as length of the list at left and the shift that is present, then it will be the required element - thus directly returning it
        return pivot_element
    
    return find_median(chosen_list, shift) # At recursing the function with the new list and the shifted value so as to again loop, and find better results

print(f"The original list is {list_to_be_used}.")

if len(list_to_be_used)%2 != 0: # If the list is odd-lengthed, find the median using normal strategy
    median = find_median()
    print(f"The median of the given list is {median}.")
else: # If the list is even-lengthed, find the greater median first, remove it - thus making it an odd list - and then finding the smaller median
    median1 = find_median()
    list_to_be_used.remove(median1)
    median2 = find_median()
    print(f"The medians of the given list are {median2} and {median1}.")