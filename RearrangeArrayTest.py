
def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return mergeSort(leftHalf),mergeSort(rightHalf)

print(mergeSort([1, 2, 8, 4, 11, 6]))

    
