class Man:
  height = 0
  name = ' '
def manKey(man):
  return (-man.height,man.name)
n = int(input())
list = []
for i in range(n):
    temp = input.split()
    man = Man()
    man.height = int(temp[0])
    man.name = temp[1]
    list.append(man)
list.sort(key=manKey)
