def swap(array, i, j):
        array[i],array[j] = array[j], array[i]


def sort_012(input_list):
    one = 1
    start = 0
    currentIdx = 0
    end = len(input_list) -1

    while currentIdx <= end:
        if input_list[currentIdx] < 1:
            swap(input_list,currentIdx,start)
            currentIdx += 1
            start += 1
        elif input_list[currentIdx] > 1:
            swap(input_list,currentIdx,end)
            end -= 1
        else:
            currentIdx += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])