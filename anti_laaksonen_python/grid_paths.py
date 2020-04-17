#O(n^2) 
data = [[3,7,9,2,7],
        [9,8,3,5,5],
        [1,7,9,8,5],
        [3,8,6,4,10],
        [6,3,9,7,8]]
res = [[0 for i in range(len(data))] for j in range(len(data))]
ans = 0
for i in range(1,len(data)):
  for j in range(1,len(data[i])):
    res[i][j] = max(data[i][j-1],data[i-1][j])+data[i][j]
for i in range(len(res)):
  ans+=max(res[i])
print(res)
print(ans)
