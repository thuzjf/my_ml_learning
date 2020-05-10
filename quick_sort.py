from typing import List

def quick_sort(array: List, low, high) -> None:
    if len(array) < 2:
        return
    if low < high:
        p = partition(array, low, high)
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)


def partition(array: List, low: int, high: int) -> int:
    number = array[low]
    while low < high:
        while low < high and array[high] >= number:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] <= number:
            low += 1
        array[high] = array[low]
    array[low] = number
    return low


if __name__ == '__main__':
    import numpy as np

    array = np.random.randint(1, 40, 10).tolist()
    quick_sort(array, 0, len(array) - 1)
    print("sorted array: {}".format(array))
