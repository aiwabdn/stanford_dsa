import numpy as np

def merge(left, right):
    i, j = 0, 0
    merged = []
    for k in range(len(left) + len(right)):
        if (i < len(left)) and (j < len(right)):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        elif i == len(left):
            merged += right[j:]
            break
        else:
            merged += left[i:]
            break
    del left, right
    return merged

def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    merged = merge(left, right)
    return merged

array = np.random.random_integers(0, 100000000, size=1000000)
sortedarray = np.sort(array)

print(np.array_equal(sortedarray, np.array(merge_sort(list(array)))))