with open("data.txt") as f:
  a = f.read().strip().split("\n")

for i in a:
  for j in a:
    for k in a:
      if (int(i) + int(j) + int(k)) == 2020:
        print(int(i) * int(j) * int(k))