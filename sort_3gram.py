# -*- coding : utf-8 -*-
import sys

if __name__ == "__main__":
  param = sys.argv
  f = open(param[1], "r")
  org = []
  for i in f:
    tmp=len(i) - 1
    org.append(i[0:tmp])
  f.close()
  org.sort()

  for i in org:
    print(i)
  
