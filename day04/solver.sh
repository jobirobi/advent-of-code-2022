#!/usr/bin/env bash

file=input.txt
pt1=0 pt2=0
export IFS='-,'
while read one_low one_high two_low two_high; do

  # if one assignment is fully within the other, its low will be equal or greater to the other and its high will be equal or lesser to the other:
  if [[ $one_low -le $two_low && $one_high -ge $two_high \
     || $two_low -le $one_low && $two_high -ge $one_high ]]; then
    ((pt1++))
  fi

  # if one assignment overlaps with the other, its low or its high will fall within the low and high of the other:
  if [[ $one_low -ge $two_low && $one_low -le $two_high \
     || $one_high -ge $two_low && $one_high -le $two_high \
     || $two_low -ge $one_low && $two_low -le $one_high \
     || $low_high -ge $one_high && $two_high -le $one_high ]]; then
    ((pt2++))
  fi
done < $file

echo $pt1 $pt2
