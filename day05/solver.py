#!/usr/bin/env python3

pt1, pt2, stacks1 = 0, 0, 0
with open("input.txt") as file:

  # read the initial map
  while True:
    line = file.readline()
    if line[0:2] == ' 1':
      break
    if stacks1 == 0:
      stacks1 = ["" for _ in range(int(len(line)/4))]
    for i, char in enumerate(line[1::4]):
      if char != ' ':
        stacks1[i] = char + stacks1[i]
  stacks1 = [list(x) for x in stacks1]
  stacks2 = [x[:] for x in stacks1[:]]

  # one empty line
  file.readline()

  # perform move operations
  while True:
    line = file.readline().strip()
    if not line:
      break
    line = [int(x) for x in line.split(' ')[1::2]]

    # move X from Y to Z, one at a time
    for i in range(line[0]):
      stacks1[line[2]-1].append(stacks1[line[1]-1].pop())

    # move X from Y to Z, as a group
    stacks2[line[2]-1] = stacks2[line[2]-1] + stacks2[line[1]-1][-(line[0]):]
    stacks2[line[1]-1] = stacks2[line[1]-1][:-(line[0])]

print("Part 1: " + ''.join([x[-1] for x in stacks1]))
print("Part 2: " + ''.join([x[-1] for x in stacks2]))
