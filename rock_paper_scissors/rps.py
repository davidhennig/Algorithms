#!/usr/bin/python

import sys

def rock_paper_scissors(n, cache=None):

  inputs = [['rock'], ['paper'], ['scissors']] 
  results = []

  if n == 0:
    return []
  if n == 1:
    return inputs
  else:
    for i in inputs:
      for j in inputs:
        results.append(i * n)
      print("This is i", i)
  return results

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
  