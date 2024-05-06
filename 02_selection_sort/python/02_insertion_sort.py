# Insertion sort: [5, 3, 6, 2, 10]

from typing import List


def insertion_sort(arr: List[int]):
    n = len(arr)

    for i in range(n):
        # [2,3,5,6,10]

        j = i - 1 # second pointer

        while j >= 0 and (arr[j] > arr[j+1]):
            # comparing ith and jth element. Not using i instead j + 1 since
            # using i does not allow to compare with already sorted elements in the list.
            
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1

    return arr

print(insertion_sort([5, 3, 6, 2, 10]))