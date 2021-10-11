def binary_search(array, low, high, number):
    mid_index = (low + high) // 2
    if array[mid_index] == number:
        return mid_index
    elif array[mid_index] < number:
        return binary_search(array[mid_index: high], mid_index, high, number)
    elif array[mid_index] > number:
        return binary_search(array[low: mid_index], low, mid_index, number)
    return None


def search_sorted_array(array, number):
    low_index = 0
    high_index = len(array) - 1
    mid_index = (low_index + high_index) // 2

    if array[mid_index] == number:
        return mid_index
    # number: 10 .... array : [5, 6, 7, 9, 10, 0 , 1, 2]    
    elif array[mid_index] < number:
        # is it in the first half, to the left? 
        # [6, 7, 8, 1, 2, 3, 4] 
        # middle is 1.  number: 8

        # look to the second half
        if array[high_index] == number:
            return high_index
        # [6, 7, 8, 1, 2, 3, 4]
        # [1, 2, 5, 6, 7, 8, 9, 10]
        # middle is 1.  number: 2
        if array[high_index] > number:
            return binary_search(array[mid_index: high_index], mid_index, high_index, number)
            # binary search of whole array  [6, 7, 8, 1, 2, 3, 4]
            # mid to high index, [1, 2, 3, 4] of the whole array
        # [5, 6, 7, 9, 10, 0 , 1, 2] 
        # number: 10
        elif array[high_index] < number:
            # we don't know if it's in the second half or not
            # [5, 6, 7, 9, 10, 0 , 1, 2]
            # [5, 6, 7]
            # pass in whole array with low and high indexes
            return search_sorted_array(array[low_index: mid_index], number)
    elif array[mid_index] > number:
        # check the first half
        if array[low_index] == number:
            return low_index
        elif array[low_index] < number:
            # assume number is in first half of array
            return binary_search(array[low_index: mid_index], low_index, mid_index, number)
        elif array[low_index] > number:
            # assume number is in the second half
            return search_sorted_array(array[mid_index + 1: high_index + 1], number)



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == search_sorted_array(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# test_function([[6, 7, 8, 1, 2, 3, 4], 10])