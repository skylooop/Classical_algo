nums = [10,5,3,4,5,1,11]
cache = [1]*len(nums)
ans=0
for i in range(len(nums)):
  for j in range(0,i):
    if nums[i]>nums[j] and cache[i]<cache[j]+1:
      cache[i] = cache[j]+1
for i in range(len(nums)):
  ans = max(ans,cache[i])
print(ans)
