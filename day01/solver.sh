#!/usr/bin/env bash

file="input.txt"
elf=0
calories=(0)

while read line; do
  if [[ -z $line ]]; then
    ((elf++))
    ((calories[elf]=0))
  else
    ((calories[elf]+=line))
  fi
done < $file

printf "%d\n" ${calories[@]} | sort -nr | head -3
