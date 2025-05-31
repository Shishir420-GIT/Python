# nums = [-1,0,1,2,-1,-4]
# nums.sort()
# result = []
# for i, a in enumerate(nums):
#     if i > 0 and a == nums[i-1]:
#         continue
#     l, r = i+1, len(nums) - 1
#     while r > l:
#         threeSum = a + nums[l] + nums[r]
#         if threeSum > 0:
#             r -= 1
#         elif threeSum < 0:
#             l += 1
#         else:
#             result.append([nums[i],nums[l],nums[r]])
#             l += 1
#             while l < r and nums[l] == nums[l+1]:
#                 l += 1
# print(result)


arr = [1,3,4,5,6]

# i, j = 0, len(arr)-1

# while j > i:
# 	arr[i], arr[j] = arr[j], arr[i]
# 	print(arr)
# 	i += 1
# 	j -= 1

# print(arr)

# arr = [1,3,4,5,6,7]

# max = 0
# previousMax = 0
# for i in arr:
# 	if i > max:
# 		previousMax = max
# 		max = i

# print(previousMax)
# arr = [1,3,3,3,4,5,5,6]

# i = 0

# set1 = set(arr)
# arr = list(set)

# arr2 = []
# while i < len(arr):
# 	if arr[i] not in arr2:
# 		arr2.append(arr[i])

# arrr = [0,1,1,1,0,1,0]

# for i in range(len(arrr)):
#     for j in range(i+1,len(arrr)):
#         if arrr[i] > arrr[j]:
#             arrr[i], arrr[j] = arrr[j], arrr[i]

# i, j = 0,0
# while len(arr) >= i:
#     if arrr[i] == 0:
#         arrr[j], arrr[i] = arrr[i], arrr[j]
#         j += 1
#     i += 1

# print(arrr)