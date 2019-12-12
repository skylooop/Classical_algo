def hamming(a,b):
  x = a^b
  return bin(x).count('1')
print(hamming(1,4))
