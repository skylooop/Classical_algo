#O(N) solution to maximum subarray sum
def max_subar(a):
  whole_max = a[0]
  curr_max = a[0]
  for i in range(len(a)):
    curr_max = max(curr_max+a[i],curr_max)
    whole_max = max(whole_max,curr_max)
  return whole_max
