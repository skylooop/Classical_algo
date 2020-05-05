def merge(intervals):
  if len(intervals)<=1:
    return intervals
  intervals.sort(key = lambda x:x[0])
  res = [intervals[0]]
  curr = intervals[0]
  for i in intervals:
    curr_s = curr[0]
    curr_e = curr[1]
    nex_s = i[0]
    nex_e = i[1]
    if curr_e >= nex_s:
      curr[1] = max(curr_e,nex_e)
    else:
      curr = i
      res.append(i)
  return res
