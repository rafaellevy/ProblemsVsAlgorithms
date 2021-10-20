import random
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
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