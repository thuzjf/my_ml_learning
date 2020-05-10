# 找出array中满足和为k的两个数，如果找不到则返回最接近的
from quick_sort import quick_sort

def find_numbers(array, k):
    if len(array) < 2:
        return None
    if len(array) == 2:
        return array[0], array[1]

    length = len(array)
    quick_sort(array, 0, length - 1)
    print("sorted array: {}".format(array))

    low, high = 0, length - 1
    if array[low] + array[low + 1] >= k:
        return array[low], array[low + 1]

    if array[high] + array[high - 1] <= k:
        return array[high - 1], array[high]

    min_value = 1e10
    a, b = 0, 0
    while low < high:
        s = array[low] + array[high]
        if abs(s - k) <= min_value:
            min_value = abs(s - k)
            a = low
            b = high
        if s == k:
            return array[low], array[high]
        elif s > k:
            high -= 1
        else:
            low += 1
    return array[a], array[b]

if __name__ == '__main__':
    import numpy as np
    array = np.random.randint(1, 40, 10)
    k = np.random.randint(-10, 50, 1)[0]

    print("k: {}".format(k))
    print("array: {}".format(array))
    print("output: {}".format(find_numbers(array, k)))