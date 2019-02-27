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
    pivot = arr / 2
    if(low < pivot):
        quick_sort(low)
    if(high > pivot):
        quick_sort(high)
    return arr

#Quick Sort example we used during class:
def quick_sort(a):
    #Base case to exit out of the for loop
    if len(a) <= 1:
        return a

    #Initializing the pivot
    pivot = len(a)-1
    #Initializing the flag
    flag = 0

    #Iterating from 0 to the pivot
    for i in range( 0, pivot):
        #If a[i] is less than a[pivot] it'll swap place
        if a[i] < a[pivot]:
            a[i], a[flag] = a[flag], a[i]
        #Increment flag by 1, or moving it up by one
            flag += 1
    #If a[i] is greater than a[pivot] then it'll swap the flag and pivot value
    a[flag], a[pivot] = a[pivot], a[flag]

    # print("This is the pivot swap", a)
    # print("This is the flag:", a[flag])
    # print("This is the pivot:", a[pivot])
    # print("flag to pivot:", a[flag: pivot+1])
    # print("0 to pivot:", a[:len(a[1:flag+1])])

    #Recursively call quick_sort twice and split into two list, 0 to flag and flag to pivot.
    #Then repeat the previous steps until length of a is less than 1
    return quick_sort(a[:len(a[1:flag+1])]) + quick_sort(a[flag:pivot+1])

# Quick Sort Algorithm from the readme.md
# 1. Select a pivot. Often times this is the first or last element in a set. It can also be the middle.
# 2. Move all elements smaller than the pivot to the left. 
# 3. Move all elements greater than the pivot to the right.
# 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
