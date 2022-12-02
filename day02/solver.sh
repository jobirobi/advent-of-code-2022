#!/usr/bin/env bash

file=input.txt
pt1=0 pt2=0
while read you me; do
  case $me in
    X)  ((pt1++)) # rock
        case $you in
          A)  ((pt1+=3)) # rock (draw)
              ((pt2+=3)) ;; # lose with scissors
          B)  ((pt2+=1)) ;; # lose with rock
          C)  ((pt1+=6)) # scissors (win)
              ((pt2+=2)) ;; # lose with paper
        esac ;;
    Y)  ((pt1+=2)) # paper
        ((pt2+=3)) # draw
        case $you in
          A)  ((pt1+=6)) # rock (win)
              ((pt2++)) ;; # draw with rock
          B)  ((pt1+=3)) # paper (draw)
              ((pt2+=2)) ;; # draw with paper
          C)  ((pt2+=3)) ;; # draw with scissors
        esac ;;
    Z)  ((pt1+=3)) # scissors
        ((pt2+=6)) # win
        case $you in
          A)  ((pt2+=2)) ;; # win with paper
          B)  ((pt1+=6)) # paper (win)
              ((pt2+=3)) ;; # win with scissors
          C)  ((pt1+=3)) # scissors (draw)
              ((pt2+=1)) ;; # win with rock
        esac ;;
  esac
done < $file

echo $pt1 $pt2
