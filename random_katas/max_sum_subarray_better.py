#O(N) solution to maximum subarray sum
def maxSubArray(self, nums: List[int]) -> int:
     maxi = float('-inf')
     end_here = 0
     for num in nums:
        if end_here>0:
            end_here +=num
        else:
            end_here = num
        maxi = max(maxi,end_here)
     return maxi
