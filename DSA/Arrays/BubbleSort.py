def bubble_sort_normal(lst):
    length = len(lst)
    
    for j in range(length-1):
        for i in range(length-1):
            if lst[i] > lst [i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
    return lst
    
# Optimized

def bubble_sort(lst):
    length = len(lst)
    for j in range(length):
        for i in range(length-1-j):
            if lst[i] > lst [i+1]:
                lst[i],lst[i+1] = lst[i+1], lst[i]
    return lst

print(bubble_sort_normal([5,4,3,2,1]))
print(bubble_sort([5,4,3,2,1]))
