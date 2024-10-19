def rotate_list(lst, k):
    new_list=[]
    for i in range(k,len(lst)):
        new_list.append(lst[i])
    for j in range(0,k):
        new_list.append(lst[j])
    return new_list

# Test the function
lst = [1, 2, 3, 4, 5]
k = 2
print(rotate_list(lst, k))  # Output: [3, 4, 5, 1, 2]