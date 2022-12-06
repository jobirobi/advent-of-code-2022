#!/usr/bin/env python3

pt1, pt2, counter, group = 0, 0, 0, [0,0,0]
with open('input.txt') as file:
  while True:
    line = file.readline().strip()
    if not line:
      break

    # find the intersection of the two sets (first half of line, second half of line) and convert to a string
    single_line_repeat = list(set(line[:int(len(line)/2)]).intersection(set(line[int(len(line)/2):])))[0]

    if single_line_repeat < 'a':
      pt1 += ord(single_line_repeat) - 38  # capital letters A-Z have ASCII values 65-90 => 27-52
    else:
      pt1 += ord(single_line_repeat) - 96  # lowercase letters a-z have ASCII values 97-122 => 1-26

    group[counter] = set(line)
    if counter == 2:

      # find the intersection of the three sets (line 3n + 0, line 3n + 1, line 3n + 2) and convert to a string
      three_line_repeat = list(group[0].intersection(group[1], group[2]))[0]

      if three_line_repeat < 'a':
        pt2 += ord(three_line_repeat) - 38
      else:
        pt2 += ord(three_line_repeat) - 96

    counter = (counter + 1) % 3

print(pt1, pt2)
