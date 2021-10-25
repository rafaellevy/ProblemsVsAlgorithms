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
    # sort the input list using merge sort
    if input_list == []:
        return []
    input_list = mergeSort(input_list)
    resultArray = []
    largerNumber = ""
    smallerNumber = ""
    current = None
    for i in range(len(input_list)-1,-1,-2):
    # auxArray.append(array[i])
        largerNumber += str(input_list[i])
    for i in range(len(input_list)-2,-1,-2):
        smallerNumber += str(input_list[i])
    smallerNumber = int(smallerNumber)
    largerNumber = int(largerNumber)
    resultArray.extend([largerNumber,smallerNumber])
    return resultArray

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
# [1, 2, 3]  [4, 5]  --> [542]   
test_case1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case2 = [[1, 2, 3, 4, 5, 6], [642, 531]] # edge case: array already sorted.
test_case3 =  [[], []] # edge case: expect error message 

test_function(test_case1)
test_function(test_case2)
test_function(test_case3)


