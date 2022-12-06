#!/usr/bin/env python3

pt1, pt2 = 0, 0
with open("input.txt") as file:
  line = file.readline()
  for i in range(len(line) - 14):

    # if the number of unique chars in this 4-char substring is 4, there you go
    if pt1 == 0 and len(set(line[i:i+4])) == 4:
      pt1 = i + 4

    # ditto, but 14
    if len(set(line[i:i+14])) == 14:
      pt2 = i + 14
      break
print(pt1, pt2)
