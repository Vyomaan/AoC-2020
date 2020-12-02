import re

numcount = 0
with open("data.txt") as f:
    for line in f:
      n, (c, _), password = line.split(' ')
      letter = c
      l = re.findall(letter, password)
      length = len(l)
      chunks = n.split('-')
      x = int(chunks[0])
      y = int(chunks[1])
      if x <= length <= y:
        numcount = numcount + 1 


print(numcount)