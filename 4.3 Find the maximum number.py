def max(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    maxCurrent = max(arr[1:]) # reduce the array until length = 2
    if arr[0] > maxCurrent:
        return arr[0]
    else:
        return maxCurrent

print(max([1, 14, 3, 19]))