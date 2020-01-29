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
