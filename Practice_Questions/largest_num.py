def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if largest < num:
            largest = num
    return num
    
print(find_largest([9,4,5,7]))