import os
import sys

with open("input.txt") as f:
  lines = f.readlines()

a = []
b = []

for line in lines:
  a.append(int(line.split('   ')[0]))
  b.append(int(line.split('   ')[1]))

a.sort()
b.sort()

total = 0

for a,b in zip(a,b):
  total += abs(a-b)

print(total)
