def reverse_list(lst):
    empty_list = []
    n = len(lst)
    while n > 0:
        empty_list.append(lst[n-1])
        n = n - 1
    return empty_list
    
#print(reverse_list([1,2,3,4]))