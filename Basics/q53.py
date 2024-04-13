list_to_be_sorted = [0, 7, 2, 3, 1, 9, 8, 5, 3] # Defining the list that has to be sorted

def quick_sort(l): # Sorts the list by using_quick sort algorithm
    pivot_element = l[0] # Taking the element about which the list to be sorted is pivoted - We pivot the list to arrange all the other elements about it - on the left if smaller and on the right if greater
    l.pop(0) # Removing the pivoted element from the given list - as now we require all the other elements so as to arrange other elements about it

    final_list = [pivot_element] # Initializing the list that is to be given away for recursion and will finally contain the sorted list
    # Currently we will be arranging all the other elements about the pivot
    for i in l:
        if i >= pivot_element: # If the currrent element is greater than or equal to the pivot, then append to the end of the final list
            final_list.append(i)
        else: # If the current element is less than the pivot, then insert that element to the start of the list
            final_list.insert(0, i)

    left = final_list[:final_list.index(pivot_element)] # Defining the part present at left of the pivot after arranging the list
    right = final_list[final_list.index(pivot_element) + 1:] # Defining the part present at the right of the pivot after arranging the list
    
    if len(final_list) == 1: # If the final list is containing only one element, this means that the list will automatically be sorted - and thus we can return list which will join back to other lists in an sorted manner
        return final_list
    else:
        if len(left) == 0: # If the list has only right part, then quick sorting the left part doesn't make sense - thus return the pivot element and then right part in order - this will recurse as quick_sort calls the further sorting of the function
            return [pivot_element] + quick_sort(right)
        elif len(right) == 0: # If the list has only left part, then quick sorting the right part doesn't make sense - thus return the left part and then pivot element in order - this will recurse as quick_sort calls the further sorting of the function
            return quick_sort(left) + [pivot_element]
        else: # If both sides are to be sorted, return the list in a way that it will be sorted - that is the sorted left list + pivot_element + sorted right list - and in sorted left and right lists themselves, this will again happen but with a new pivot element - thus effectively arranging the pivot elements in order
            return quick_sort(left) + [pivot_element] + quick_sort(right)

if __name__ == "__main__":
    print(f"The original list is {list_to_be_sorted}.")
    print(f"The list sorted using quick sort is {quick_sort(list_to_be_sorted)}.")