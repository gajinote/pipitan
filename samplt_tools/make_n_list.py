# -*- coding: utf-8 -*-
import sys
import MeCab
import codecs

# Textを読み込む
def getsource(src):
  n = 0
  for i in src:
    n += len(i)
  return n

def create_word_list(src):
  out_list=[]
  mecab=MeCab.Tagger("-Owakati")
  tmplist = mecab.parse(src)
  t_list = tmplist.split(' ')
  l_size=len(t_list)
  for i in range(0, l_size-2):
    tmplist=[t_list[i], t_list[i+1]]
    out_list.append(tmplist)

  return out_list

if __name__ == "__main__":
  source = ""
  param = sys.argv
  f = open(param[1], "r")
  for i in f:
    source += i
  f.close
  
  out_s=[]

  out_s=create_word_list(source)
  out_s.sort()

  fout = codecs.open("n_list.txt", "w", "utf-8")
  for i in out_s:
    fout.write(i[0] + " " + i[1] + "\n")
