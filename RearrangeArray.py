
def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return mergeSortedArrays(mergeSort(leftHalf),mergeSort(rightHalf))

def mergeSortedArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArray

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # sort the input list using merge sort
    input_list = mergeSort(input_list)
    # find the middle index to split it
    middleIdx = len(input_list) // 2
    lowerHalf = input_list[:middleIdx]
    higherHalf = input_list[middleIdx:]
    output_list = []
    higherNumber = ''
    # zip through both arrays
    for i, j in zip(lowerHalf, higherHalf):
        print(i)
        print(j)

rearrange_digits([5, 4, 9, 8, 2, 1])
"""
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
# [1, 2, 3]  [4, 5]  --> [542]   
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
[2, 4, 5, 6, 8, 9]

"""

