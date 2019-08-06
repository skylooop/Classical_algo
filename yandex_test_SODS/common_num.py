n = int(input())
a = list(map(int,input().split()))
r ={}
max_cnt = -9999999999999999999999999
max_num = -9999999999999999999999999
for i in a:
  r[i] = r.get(i,0)+1
  if r[i]>max_cnt:
    max_cnt = r[i]
    max_num = i
  elif r[i]==max_cnt:
    if i>max_num:
      max_num = i
print(max_num)
