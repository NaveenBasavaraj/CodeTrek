def mergeSort(arr, left, right):
    if right - left + 1 <= 1:
        # this means we have split the array to the point there's only 1 element
        return arr
    
    middle = (right+left)//2

    # sort the left
    mergeSort(arr, left, middle)

    # sort the right
    mergeSort(arr, middle+1, right)

    # merge both halves
    merge(arr, left, middle, right)

    return arr

def merge(arr, left, middle, right):
    l_arr = arr[left:middle+1]
    r_arr = arr[middle+1:right+1]

    i,j,k = 0,0,left # for l_arr, r_arr, arr

    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i] <= r_arr[j]:
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            j += 1
        k += 1
    
    while i < len(l_arr):
        arr[k] = l_arr[i]
        i += 1
        k += 1
    while j < len(r_arr):
        arr[k] = r_arr[j]
        j += 1
        k += 1


arr = [9,8,7,6,5,4,3,2,1]
mergeSort(arr, 0, len(arr)-1)
print(arr)