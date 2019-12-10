def binary(a,val):
  low,hi = 0,len(a)-1
  while low<=hi:
    mid = (hi+low)//2
    if a[mid]<val:
      low=mid+1
    elif a[mid]>val:
      hi = mid-1
    else:
      return mid
 
  
