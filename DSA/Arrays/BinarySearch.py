def find_using_binary(nums,target):
    start = 0
    end = len(nums) -1
    mid = (start + end)//2

    while start <= end:
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end)//2
    
    return -1

print(find_using_binary([1,2,3,4,5],5))