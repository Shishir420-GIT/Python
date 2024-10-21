def min_operations_to_make_perfect2(arr):
    n = len(arr)
    operations = 0

    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            operations += 1
            # Change the next element (conceptually)
            # This is just to think of it as changed; we don't actually need to change the array.
            # We can assume arr[i + 1] is replaced with a different number in our logic.

    return operations

class solution: 
    def min_operations_to_make_perfect(arr):
        n = len(arr)
        if n < 2:
            return 0  # No operations needed for an array with fewer than 2 elements

        operations = 0
        i = 0

        while i < n - 1:
            if arr[i] == arr[i + 1]:
                count = 1
                # Count consecutive duplicates
                while i < n - 1 and arr[i] == arr[i + 1]:
                    count += 1
                    i += 1
                # Calculate operations for the block of duplicates
                operations += count // 2
            i += 1

        return operations

# Example Usage:
# Example 1
arr1 = [1, 2, 2, 3, 3]
print(min_operations_to_make_perfect(arr1))  # Output: 2

# Example 2
arr2 = [1, 2, 3, 4]
print(min_operations_to_make_perfect(arr2)) # Output: 0

# Test Case 3
arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
print(min_operations_to_make_perfect(arr1))  # Output: 4