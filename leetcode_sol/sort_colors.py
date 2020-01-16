'''Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]'''
def sortColors(self, nums: List[int]) -> None:
        N = len(nums)
        i0 = 0
        i2 = N-1
        i = 0
        while i < i2+1:
            if nums[i] == 0:
                nums[i] = nums[i0]
                nums[i0] = 0
                i0 += 1
                i = max(i0, i)
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i] = nums[i2]
                nums[i2] = 2
                i2 -= 1
