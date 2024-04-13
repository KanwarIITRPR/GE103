list_to_be_sorted = [0, 7, 2, 3, 1, 9, 2] # Defining the list that has to be sorted

def bubble_sort(l):
    l_local = l[:] # Defining a list that is duplicate of the original list - so as to leave the original list unaltered
    
    while True: # Runs the code till a "break" is called
        sort = True # Assuming the list is sorted at first - if it is not, the code further will set it automatically to False
        for i in range(len(l_local) - 1):
            if l_local[i] > l_local[i + 1]: # Checking if the next element is less than the current element - if yes, then interchange both of them
                l_local[i], l_local[i + 1] = l_local[i + 1], l_local[i]
                sort = False # Setting sort to be False as we have at least once changed the position of elements in the list - thus our assumption of list being sorted was wrong and thus there is possibility that more switching can be required

        if sort == True: # Checks if the variable we defined for the sorting of the list is true or not - if it is, then stopping the code and returning the sorted list - if not, then there is a possibility of having more switching required, thus keeping the while loop running
            break

    return l_local

if __name__ == "__main__":
    print(f"The original list is {list_to_be_sorted}.")
    print(f"THe list sorted using bublle sort is {bubble_sort(list_to_be_sorted)}.")