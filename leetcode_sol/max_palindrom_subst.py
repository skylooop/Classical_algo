def expandmid(s,left,right):
  while left>=0 and right<len(s) and s[left] == s[right]:
    left-=1
    right+=1
  return right-left-1
s = input()
start = 0
end = 0
for i in range(len(s)):
  len1 = expandmid(s,i,i)
  len2 = expandmid(s,i,i+1)
  leng = max(len1,len2)
  if leng>end-start:
    start = i-((leng-1)//2)
    end  = i+(leng//2)
print(s[start:end+1])
