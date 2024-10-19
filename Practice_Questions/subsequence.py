def is_subsequence(s, t):
    """
    Function to check if t is a subsequence of s.
    
    Parameters:
    s (str): The original string.
    t (str): The target subsequence string.
    
    Returns:
    bool: True if t is a subsequence of s, False otherwise.
    """
    if len(t) > len(s):
        return False
    i,j = 0,0
    index = 0
    found_count = 0
    while j< len(t):
        if t[j] in s:
            found_count += 1
            tmp_index = s.index(t[j])
            if index > tmp_index:
                return False
            else:
                index = tmp_index
        j += 1
    if found_count == len(t):
        return True
    return False

def is_subsequence_2(s, t):
    """
    Function to check if t is a subsequence of s.
    
    Parameters:
    s (str): The original string.
    t (str): The target subsequence string.
    
    Returns:
    bool: True if t is a subsequence of s, False otherwise.
    """
    i, j = 0, 0  # Initialize two pointers for s and t
    
    # Loop through the original string s
    while i < len(s) and j < len(t):
        # If the characters match, move the pointer for t
        if s[i] == t[j]:
            j += 1
        # Always move the pointer for s
        i += 1
    
    # If we've matched all characters of t, return True
    return j == len(t)

# Test the function
print(is_subsequence("abcde", "ace"))  # Expected output: True
print(is_subsequence("abcde", "aec"))  # Expected output: False