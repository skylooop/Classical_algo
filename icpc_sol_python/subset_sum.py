#Given a set of n numbers ai sum up to M, and any K ≤ M, whether there is a subset of the
#numbers such that they sum up to (hit) K?

def subset(a,n,k):
  if k ==0:
    return True
  if n==0 and k!=0:
    return False
  if a[n-1]>k:
    return subset(a,n-1,k)
  return subset(a,n-1,k) or subset(a,n-1,k-a[n-1])
