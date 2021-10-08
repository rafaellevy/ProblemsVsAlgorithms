def binary_search(square):
    mid = square / 2
    if (mid * mid) == square:
        result= mid
    elif (mid * mid) > square:
        result = helper(square, 0, mid)
    elif (mid * mid) < square:
        result = helper(square, mid, square)
    return int(result)
    
    
def helper(square, low, high):
    mid = (low + high) / 2
    if (mid * mid) >= (square) and (mid * mid) < square + 1:
        return mid
    elif (mid * mid) > square:
        # change range of low and high
        # change the high
        # the mid will become the new high, because mid * mid is too high to be the answer
        return helper(square, low, mid)
    elif (mid * mid) < square:
        # mid is too low, so it will become the new low.
        return helper(square, mid, high)
    
print(binary_search(3))   
print(binary_search(4))
print(binary_search(25))
print(binary_search(27))