# from collections import Counter
# import re

# def count_word_occurrences(sentence):
#     # Convert the sentence to lowercase and use regex to extract words (ignores punctuation)
#     words = re.findall(r'\b\w+\b', sentence.lower())
    
#     # Use Counter to count the occurrences of each word
#     word_counts = Counter(words)
    
#     return word_counts

# # Example usage
# sentence = "Bhola and 'shambhu .are having a good conversation, having in between Bhola, Shambhu."
# word_counts = count_word_occurrences(sentence)

# # Printing the word count
# for word, count in word_counts.items():
#     print(f"{word}: {count}")


def myList(arr):
    val = set()
    result = []
    
    for num in arr:
        if num not in val:
            val.add(num)
            result.append(num)
    
    for num in arr:
        if arr.count(num) > 1 and num in val:
            result.append(num)
            val.remove(num)
            
    return result

def transform_list(arr):
    result = []
    i = 0
    
    while i < len(arr):
        if i + 1 < len(arr) and arr[i] == arr[i + 1]:
            i += 2
        else:
            result.append(arr[i])
            i += 1
            
    return result

def myList2(arr):
    result = []
    i = 0
    while i < len(arr):
        if i + 1 < len(arr) and arr[i] == arr[i+1]:
            i += 2
        else:
            result.append(arr[i])
            i += 1            
    return result

nums = [1,2,2,3,4,5,5,3]
print(transform_list(nums))
print(myList2(nums))

