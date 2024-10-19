def canJump(nums):
    lastIndex = len(nums) - 1
    first_position = nums[0]
    if first_position == lastIndex or first_position == 0:
        return True
    for i in range(len(nums) -1, -1, -1):
        print(i,nums[i])
        if i + nums[i] >= lastIndex:
            lastIndex = i
    
    return lastIndex == 0

arr = [3,2,1,0,4]
print(canJump(arr))

arr2 = [2,3,1,1,4]
print(canJump(arr2))
