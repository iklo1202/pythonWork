def binarySearch_iterative(list, x):
    left = 0
    right = len(list)-1
    
    while (right >= left):
        mid = (left+right) / 2
        mid = int(mid)
        if list[mid] > x:
            right = mid - 1
        elif list[mid] < x:
            left = mid + 1
        else:
            return mid


    return -1



if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binarySearch_iterative(arr, x)
    print("Element is at index %d" % result)
            
