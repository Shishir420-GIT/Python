# Comparing each value in a loop

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

linear_search([3, 7, 2, 5], 2)