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
    #Iterating through the list and selecting each elements to be sorted
    for i in range(1, len(arr)):
        #Iterating backward from i
        for j in range(i, -1 , -1):
            #Comparing if the value of arr[j] is greater than arr[cur_value], if it is then it'll save the larger value, and replace with cur_value.
            if (arr[j] > arr[i]):
                #swap arr[j] and arr[i]
                arr[j], arr[i] = arr[i], arr[j]
                #decrement i
                i = i - 1
        
    return arr

# This one is using a seperate variable
# def insertion_sort( arr ):
#     #Iterating through the list and selecting each elements to be sorted
#     for i in range(1, len(arr)):
#         #Assigning i to be the current value to compare
#         cur_value = i
#         #Iterating backward from i
#         for j in range(i - 1, -1 , -1):
#             #Comparing if the value of arr[j] is greater than arr[cur_value], if it is then it'll save the larger value, and replace with cur_value.
#             if (arr[j] > arr[cur_value]):
#                 arr[j], arr[cur_value] = arr[cur_value], arr[j]
#                 #Decrement cur_value
#                 cur_value = cur_value - 1
        
#     return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(1, len(arr)):
        
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr