# from collections import Counter

# str1 = "Python"
# str2 = "HackerEarthPython"

# d1 = Counter(str1)
# d2 = Counter(str2)

# print(d1)
# print(d2)

# d = d1 & d2

# print(d)

# print()


# print(sorted(str1))
# lists = [1,2,4,6,7,3,8]
# sum = 0
# for i in lists:
#     sum += i

# print(sum)
# total = ((len(lists) + 1)*(len(lists) + 2))/2
# print(total)


# print(total - sum)

# def my_generator(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1

# # Example Usage:
# gen = my_generator(1, 5)
# for num in gen:
#     print(num)  # Output: 1 2 3 4


# def findCount(sentance, word):
# 	index = []
# 	i,j = 0,0
# 	sentance = sentance.lower()
# 	word = word.lower()
# 	n = len(sentance)
# 	empty_str = ""
# 	for c in range(n):
# 		print(sentance[c])
# 		if sentance[c] == ' ':
# 			empty_str = ""
# 			print("if")
# 			continue
# 		elif sentance[c] == word[0]:
# 			j = 1
# 			potential_index = c
# 			print("elif")
# 			for i in range(1,len(word)):
# 				if sentance[c+1]==word[i]:
# 					continue
# 				else:
# 					potential_index = -1
# 					break
# 			if potential_index >= 0:
# 				index.append(potential_index)			
# 	return len(index),index

# str1 = "Hi hello Hi"
# str2 = "Hi"
# print(findCount(str1,str2))


# str1 = "aabbbcca"
# st2 = "a2b3c2a1"
# empty_str = ""

# print(data)
# i,j = 0,0

# while i < len(str1):
#     count = 0
#     while j < len(str1) and str1[i] == str1[j]:
#         count += 1
#         j += 1
#     empty_str += str1[i] + str(count)
#     i = j 
# print(empty_str)


	
import math

def count_sequences(N):
    count = 0

    # Iterate over c as the largest number
    for c in range(1, N + 1):
        for a in range(1, c):
            for b in range(a, c):  # a <= b to avoid duplicates
                if (c - (a + b)) % 2 == 0:  # (c - (a + b)) must be even
                    k = (c - (a + b)) // 2
                    if k > 0 and k * k == a * b:  # Check if sqrt(a * b) is valid
                        count += 1
    return count + 1

# Example usage
N = 5
result = count_sequences(N)
print(f"Total number of sequences for N = {N}: {result}")

def count_sequences_pointers(N):
    count = 0

    for c in range(1, N + 1):  # Fix the largest number c
        a, b = 1, c - 1  # Initialize two pointers
        while a < b:  # Ensure a < b
            total_sum = a + b
            if total_sum >= c:  # If a + b >= c, reduce b
                b -= 1
            else:
                # Check if sqrt(a * b) is valid
                k = (c - total_sum) / 2
                if k > 0 and k == int(k) and k * k == a * b:
                    count += 1
                a += 1  # Move pointer a forward
    return count

# Example usage
N = 10
result = count_sequences_pointers(N)
print(f"Total number of sequences for N = {N}: {result}")

	
	
	
	
