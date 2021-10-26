import random
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == []:
        return None, None
    min = ints[0]
    max = ints[0]
    for i in range(1, len(ints)-1):
        if ints[i] < min:
            min = ints[i]
        elif ints[i] > max:
            max = ints[i]
    return min, max


## Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l1 = [-8, 3, -550, 10, 0]  # edge case: array with negative integers
print ("Pass" if ((-550, 10) == get_min_max(l1)) else "Fail")

l2 = []  # edge case: empty array
print ("Pass" if ((None, None) == get_min_max(l2)) else "Fail")
