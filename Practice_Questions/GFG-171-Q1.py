
class Solution:
    def smallestSubstring(self, str : str, k : int) -> str:
        n = len(str)
        min_sum,curr_sum = 0,0
        for i in range(k):
            curr_sum += ord(str[i])
        start = 0
        min_sum = curr_sum
        for i in range(k,n):
            curr_sum -=  ord(str[i-k])
            curr_sum += ord(str[i])
            if min_sum > curr_sum:
                min_sum = curr_sum
                start = i - k + 1
        return str[start:start+k]


obj = Solution()
print(obj.smallestSubstring("geeksforgeeks", 5))
print(obj.smallestSubstring("hello", 2))
    


