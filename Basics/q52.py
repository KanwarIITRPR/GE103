list_to_be_sorted = [0, 7, 2, 3, 1, 9, 15, 12] # Defining the list that has to be sorted

def merge_sort(l):
    l1 = l[:int(len(l)//2)] # Defining first half of the entered list
    l2 = l[int(len(l)//2):] # Defining second half of the entered list

    if len(l) == 1: # If the list has finally reduced to a single element list, then return it - will be stored in a variable in the further program if the original list was bigger
        return l
    else:
        l_final = [] # Defining the sorted list
        new_l1 = merge_sort(l1) # Recurses through the function - will stop when a single element remains
        new_l2 = merge_sort(l2) # Recurses through the function - will stop when a single element remains

        for i in range(len(new_l1) + len(new_l2)): # Recurses through the total amount of elements present in the net kist at that time
            if len(new_l1) == 0: # If all the elements in new_l1 are gone thorugh - i.e., all the elements of new_l1 are used in sorting, then append the rest of new_l2 remaining elements (which will already be in order - as the new_l2 is formed by sorting two individual elements, then sorting the elements in two lists and so on)
                for i in new_l2:
                    l_final.append(i)
                break
            elif len(new_l2) == 0: # If all the elements in new_l2 are gone thorugh - i.e., all the elements of new_l2 are used in sorting, then append the rest of new_l1 remaining elements (which will already be in order - as the new_l1 is formed by sorting two individual elements, then sorting the elements in two lists and so on)
                for i in new_l1:
                    l_final.append(i)
                break

            # If no list is empty, compare the first element of each list, append the smallest of the two to the final list and remove the appended element from its list and re-run this until one of the list doesn't get emptied
            list_with_current_min_element = new_l1 if new_l1[0] < new_l2[0] else new_l2 # Compares the first elements of the two lists
            l_final.append(list_with_current_min_element[0]) # Appends the smallest element to the final list
            list_with_current_min_element.pop(0) # Removes the element that we have appended in the final list

        return l_final # Returns the final list - since this function is recursing, the merged and sorted list goes back into new_l1 or new_l2 - thus ready for more merging and sorting with bigger lists
    
if __name__ == "__main__":
    print(f"The original list is {list_to_be_sorted}.")
    print(f"The list sorted using merge sort is {merge_sort(list_to_be_sorted)}.")