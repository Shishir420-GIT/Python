def is_palindromic_tuple(tup):
    i = 0
    j = len(tup) - 1
    
    while i < j:
        if tup[i] == tup[j]:
            i += 1
            j -= 1
            continue
        else:
            return False
    return True