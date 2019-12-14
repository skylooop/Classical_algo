#Input:  [1,2,3,4]
#Output: [24,12,8,6]


#Runtime: 124 ms, faster than 90.73% of Python3 online submissions for Product of Array Except Self.
#Memory Usage: 19.2 MB, less than 98.00% of Python3 online submissions for Product of Array Except Self.
def productExceptSelf(nums):
        res = []
        mul,zero,copy = 0,0,0
        ind = False
        if nums.count(0)>1:
            return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                ind = True
            else:
                if i==0:
                    mul = 1
                mul*=nums[i]
        if ind == True:
            zero = mul
            mul=0
        else:
            copy=mul
        for i in range(len(nums)):
            if nums[i]!= 0:
                res.append(mul//nums[i])
                mul = copy
            else:
                res.append(zero)
        return res
            
