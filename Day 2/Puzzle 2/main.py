numcount = 0
with open("data.txt") as f:
    for line in f:
      n, (c, _), password = line.split(' ')
      letter = c
      chunks = n.split('-')
      x = int(chunks[0])
      y = int(chunks[1])
     
      
      d = password[x - 1]
      e = password[y - 1] 
      if d == c:
        if e == c:
          numcount = numcount + 0
        else:
          numcount = numcount + 1
      elif e == c:
        numcount = numcount + 1
      else:
        numcount = numcount + 0

     
print(numcount)
