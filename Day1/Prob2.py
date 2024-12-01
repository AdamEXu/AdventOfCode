import os
import sys

with open("input.txt") as f:
  lines = f.readlines()

a = []
b = []

for line in lines:
  a.append(int(line.split('   ')[0]))
  b.append(int(line.split('   ')[1]))

total = 0

for a_,b_ in zip(a,b):
  total += b.count(a_)*a_

print(total)
