#k = 0; n = 3 eg {0,1,2}
def search(k):
  if k==n:
    print(subset)
  else:
    search(k+1) #k not in subset
    subset.append(k) 
    search(k+1) # k in subset
    subset.pop()
n,k = 3,0
search(k)


#Method 2
b = 0
n = 3
while b<(1<<n):
  subset = []
  for i in range(n):
    if b&(1<<i):
      subset.append(i)
  print(subset)
  b+=1
