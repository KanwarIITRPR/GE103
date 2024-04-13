import time
import q51, q52, q53
import test2

def check_timing():
    test2.random_words_in_testfile()

    testfile = "Ge103/testcase1.txt" # Specifting the file for which we are reading the contents
    f = open(testfile, "r") # Opening the given file in Read-Only Mode
    contents = f.readlines() # reading and storing the lines in the file in a list
    f.close() # Closing the file
    # print(f"The contents of the file are {contents}.")

    # start_bubble_sort = time.time() # Starting to measure the time taken by bubble sort to sort the contents
    # q51.bubble_sort(contents)
    # # print(f"The list when sorted using bubble sort is {q51.bubble_sort(contents)}.")
    # end_bubble_sort = time.time() # Stopping the measuring of time that was going on for bubble sort

    start_merge_sort = time.time() # Starting to measure the time taken by merge sort to sort the contents
    q52.merge_sort(contents)
    # print(f"The list when sorted using merge sort is {q52.merge_sort(contents)}.")
    end_merge_sort = time.time() # Stopping the measuring of time that was going on for merge sort

    start_quick_sort = time.time() # Starting to measure the time taken by quick sort to sort the contents
    q53.quick_sort(contents)
    # print(f"The list when sorted using quick sort is {q53.quick_sort(contents)}.\n")
    end_quick_sort = time.time() # Stopping the measuring of time that was going on for quick sort

    # Net time taken = Stopping time - Starting time
    # bubble_sort_time = end_bubble_sort - start_bubble_sort
    bubble_sort_time = 1000
    merge_sort_time = end_merge_sort - start_merge_sort
    quick_sort_time = end_quick_sort - start_quick_sort

    # print(f"The total time taken by bubble sort is {bubble_sort_time} seconds.")
    

    methods_and_time = {"Bubble Sort": bubble_sort_time, "Merge Sort": merge_sort_time, "Quick Sort": quick_sort_time} # Storing the sorting methods and their respective times in a dictionary
    least_time_taken = min(list(methods_and_time.values())) # Evaluting the least time by finding the minimum of all the times ("values" of the dictionary above)
    method_with_least_time = list(methods_and_time.keys())[list(methods_and_time.values()).index(least_time_taken)] # Defining the method that took the least time - by first finding the index of least time in the "values" of the dictionary and then using that index to map it for the "keys" of the dictionary

    return method_with_least_time
    # print(f"The least time is taken by {method_with_least_time} - in {least_time_taken} seconds.")

merge_count = 0
for i in range(1000):
    res = check_timing()
    if res == "Merge Sort":
        merge_count += 1
    print(res)

print(f"The times merge sort is faster than quick sort is {merge_count}.")