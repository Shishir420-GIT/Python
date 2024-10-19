def selection_sort(lst):
    n = len(lst)
    
    for j in range(n - 1):
        min_index = j
        for i in range(j+1,n):
            if lst[min_index] < lst[i]:
                min_index = i
                print("min_index: ", min_index)
        lst[j],lst[min_index] = lst[min_index],lst[j]
        print(lst)
    return lst



print(selection_sort([64, 25, 12, 22, 11]))