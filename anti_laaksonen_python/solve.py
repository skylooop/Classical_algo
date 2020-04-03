#Construct given sum n using as few coins as possible
import math
def solve(a):
  for i in range(len(a)):
    if x<0:
      return math.inf
    if x==0:
      return 0
    for i in range(len(c)):
      best = min(best,solve(x-c)+1)
  return best
