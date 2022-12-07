#!/usr/bin/env python3
# note: match/case requires python >= 3.10

pwd, dirs = [], dict()
with open("input.txt") as file:
  while True:
    line = file.readline().strip()
    if not line:
      break

    line = line.split(' ')
    match line[0]:
      case '$':  # command
        if line[1] == 'cd':  # change directory
          match line[2]:
            case '..':  # up one level
              pwd.pop()
            case '/':  # root directory
              pwd = []
            case _:  # down one level
              pwd.append(line[2])
        # else:  # ls (do nothing)
      case 'dir':  # item is a directory (do nothing)
        continue
      case _:  # item is a file
        if '/' + '/'.join(pwd) in dirs.keys():
          dirs['/' + '/'.join(pwd)] += int(line[0])
        else:
          dirs['/' + '/'.join(pwd)] = int(line[0])

        # ensure file is accounted for in all higher directories
        parent = pwd[:-1]
        while parent != []:
          if '/' + '/'.join(parent) in dirs.keys():
            dirs['/' + '/'.join(parent)] += int(line[0])
          else:
            dirs['/' + '/'.join(parent)] = int(line[0])
          parent.pop()

# here I account for a bug where / was not accounted for correctly:
dirs['/'] += sum([v for k, v in dirs.items() if k.count('/') == 1 and k != '/'])

print("Part 1:", sum([v for v in dirs.values() if v <= 100000]))
print("Part 2:", sorted([v for v in dirs.values() if v - 30000000 + 70000000 - dirs['/'] > 0])[0])
