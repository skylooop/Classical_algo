'''
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        maxi = 0
        letters = set()
        for i in s:
            if i in letters:
                maxi+=2
                letters.remove(i)
            else:
                letters.add(i)
        return maxi+bool(letters)
 
