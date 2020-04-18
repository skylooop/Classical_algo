def hanoi(height,left= 'left',middle = 'middle',right = 'right'):
  if height:
    hanoi(height-1,left,middle,right)
    print(left, "->",right)
    hanoi(height-1,middle,right,left)
    
