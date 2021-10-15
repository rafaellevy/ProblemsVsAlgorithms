def swap(array, i, j):
    array[i],array[j] = array[j], array[i]

def sort(array):
    one = 1
    start = 0
    currentIdx = 0
    end = len(array) -1

    while currentIdx <= end:
        if array[currentIdx] < 1:
            swap(array,currentIdx,start)
        elif array[currentIdx] > 1:
            swap(array,currentIdx,end)
        else:
            

