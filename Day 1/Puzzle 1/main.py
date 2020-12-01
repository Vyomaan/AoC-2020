with open("data.txt") as f:
  a = f.read().strip().split("\n")

for i in a:
  for j in a:
    if (int(i) + int(j)) == 2020:
      print(int(i) * int(j))