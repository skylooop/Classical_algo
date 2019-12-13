#O(n) solution and Space O(1)
#Input: "abcabcbb"
#Output: 3 
#Explanation: The answer is "abc", with the length of 3. 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = {}
        start,longest = 0,0
        for i,c in enumerate(s):
            if c in data and data[c] >=start:
                start = data[c]+1
            else:
                longest = max(longest,i-start+1)
            data[c]=i
        return longest
                
#also beautiful solution
def result(s):
    data = []
    longest = 0
    for i in s:
        if i in data:
            data = data[data.index(i)+1:]
        data.append(i)
        longest = max(longest, len(data))
    return longest
