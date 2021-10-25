def binarySearch(array, low_index, high_index, number):
    # user put in wrong indices OR number is not found
    if high_index < low_index:
        return -1
    mid_index = (high_index + low_index) // 2

    if array[mid_index] == number:
        return mid_index
    elif array[mid_index] < number:
        # means number is in second half of array
        return binarySearch(array, mid_index + 1, high_index, number)
    elif array[mid_index] > number:
        return binarySearch(array, low_index, mid_index - 1, number)


# [5, 6, 7, 9, 10, 0 , 1, 2]

# [6, 7, 8, 1, 2, 3, 4] 
def findPivot(array, low_index, high_index):
    # pivot is found, possibly one element in array
    if low_index == high_index:
        return low_index
    # pivot is not found, array is already sorted
    # what if array is empty?
    if high_index < low_index or len(array) == 0:
        return -1
    
    # start searching for pivot at the middle
    mid_index = (low_index + high_index) // 2

    # pivot is the only element where the next element is smaller
    # look to the right to check if the mid_index is the pivot
    if mid_index < high_index and array[mid_index] > array[mid_index + 1]:
        return mid_index
    # look at the previous element to see if it is the pivot
    if mid_index > low_index and array[mid_index - 1] > array[mid_index]:
        return mid_index - 1
    # if the element at the low_index is greater, than the pivot must be in the first half.
    # [6, 7, 8, 0, 1, 2, 3, 4, 5]  
    if array[low_index] > array[mid_index]:
        # find the pivot in the first half, recursion
        # mid_index or mid_index - 1 ? 
        return findPivot(array, low_index, mid_index)
    # if the element a tthe low_index is smaller, than the first half is sequential/ordered, so the pivot must be in the second half
    elif array[low_index] < array[mid_index]:
        return findPivot(array, mid_index + 1, high_index)


def searchRotatedArray(array, number):
    # find the pivot of the array
    pivot = findPivot(array, 0, len(array) - 1)
    # once we find a pivot, found out which side of the pivot we want to do binary search on - first or second half?
    # pivot happens to be number
    if array[pivot] == number:
        return pivot
    # [5, 6, 7, 9, 10, 0 , 1, 2]
    # look for 7
    if array[0] <= number:
        # look in first half
        return binarySearch(array, 0, pivot - 1, number)
    elif array[0] > number:
        # look in the second half 
        # all the numbers in the first half are bigger than all the numbers in the second half. 
        return binarySearch(array, pivot + 1, len(array) - 1, number)
# print(findPivot([], 0, 4))

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == searchRotatedArray(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[1,2,3,4,0], 2]) # edge case: pivot is at the end, expect 1
test_function([[1,2,3,4,0], 5]) # edge case: expect -1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])