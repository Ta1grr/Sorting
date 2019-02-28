### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


### recursive sorting function
def merge_sort( arr ):
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) / 2 ] )
        right = merge_sort( arr[ len( arr ) / 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr, low, high ):
    #Setting the base case for the recursive function to stop once the length of arr is less than or equal to 1
    if len(arr) <= 1:
        return arr
    #Initializing flag to be low (0)
    flag = low
    #Initializing the variable pivot to be length of the list, I tried to setting it to high,
    #but it won't work because high is set to the length of the original list length.
    pivot = len(arr)-1
    #Iterating through the list from the beginning until it reach the pivot
    for i in range(0, pivot):
        #If arr[i] is less than arr[pivot] it'll swap arr[i] and arr[flag] position
        if arr[i] < arr[pivot]:
            arr[i], arr[flag] = arr[flag], arr[i]
            #Increment flag by 1 after swapping
            flag += 1
    #Swap the flag and pivot value
    arr[flag], arr[pivot] = arr[pivot], arr[flag]
    #Recursively calling the from 0 to flag and from flag to pivot then join back together until length of
    #arr is less than or equal to 1
    return quick_sort(arr[:len(arr[1:flag+1])], low, high) + quick_sort(arr[flag:pivot+1], low, high)



# Quick Sort Algorithm from the readme.md
# 1. Select a pivot. Often times this is the first or last element in a set. It can also be the middle.
# 2. Move all elements smaller than the pivot to the left. 
# 3. Move all elements greater than the pivot to the right.
# 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
