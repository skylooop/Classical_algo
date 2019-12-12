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
                
