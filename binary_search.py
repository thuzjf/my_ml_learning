from typing import List


# def binary_search(array, x, low, high):
#     if x < array[low] or x > array[high]:
#         return False
#     mid = (low + high) // 2
#     if array[mid] == x:
#         return True
#     elif array[mid] < x:
#         return binary_search(array, x, mid + 1, high)
#     else:
#         return binary_search(array, x, low, mid - 1)


# non-recurrent
def search(nums: List, target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    import numpy as np

    array = np.random.randint(10, 30, 10).tolist()
    array.sort()
    x = np.random.randint(6, 31, 1)[0]

    print("array is : {}".format(array))
    print("x is : {}".format(x))
    print(search(array, x))
