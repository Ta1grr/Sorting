# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j



        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]



    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(1, len(arr)):
        cur_value = None
        for  j in range(i, len(arr[::-i]), -1):
            j > cur_value


    return arr

#     mark first element as sorted

# for each unsorted element X

#   'extract' the element X

#   for j = lastSortedIndex down to 0

#     if current element j > X

#       move sorted element to the right by 1

#     break loop and insert X here


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr