# Website: AlgoExpert: Coding Interview Questions
# Problem: Binary Search
# Difficulty: Easy
# https://www.algoexpert.io/questions/Binary%20Search


def binarySearch(array, target):
    '''
    :type array: list[int], sorted array of ints
    :type target: int, target int
    :rtype: int, index if target in array
                 -1 otherwise

    [1, 2, 4, 5]

    min = 6, max = 5, mid = 6
    current = 61, target = 47
    45 < 47

    Time = O(log n)
    Space = O(1)
    '''

    min_index = 0
    max_index = len(array) - 1
    mid_index = (min_index + max_index) // 2

    while min_index <= max_index:
        current = array[mid_index]

        if current == target:
            return mid_index
        elif current < target:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1

        mid_index = (min_index + max_index) // 2

    return -1
