# -*- coding: utf-8 -*-
import sys
import codecs

# Textを読み込む
def getsource(src):
  n = 0
  for i in src:
    n += len(i)
  return n

# 3-gramの作成
def output_target(target):
  i = 0
  ret_list=[]
  output=target
  s = len(target)
  while(i+2 < s):
      if (output[i] != "\n" and output[i+1] != "\n" and output[i+2] !="\n"):
          ret_list.append(output[i]+output[i+1]+output[i+2])
      i += 1
  return ret_list

if __name__ == "__main__":
  source = ""
  out_s=[]
  param = sys.argv
  f = codecs.open(param[1], "r", "utf-8")
  count=getsource(f)
  f.close()

  f = open(param[1], "r")
  for i in f:
    source += i
  f.close()

  out_s=output_target(source)
  out_s.sort() 

  fout = codecs.open("3gram.txt", "w", "utf-8")
  for i in out_s:
    fout.write(i + "\n")
