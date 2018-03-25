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
  mecab=MeCab.Tagger("")
  tmplist = mecab.parse(src)
  t_list = tmplist.split("\n")
  l_size=len(t_list)
  for i in range(0, l_size-2):
    tmplist=t_list[i].split("\t")
    # print(tmplist[1])
    tmp_l1 = ""
    tmp_l1 = tmplist[1]
    tmp_l2=[]
    tmp_l2 = tmp_l1.split(",")
    tmp_l1=tmplist[0]
    tmplist = [tmp_l1, tmp_l2[0]]
    out_list.append(tmplist)

  return out_list

def create_2word_list(src):
  out_list=[]
  tmplist = src
  l_size=len(tmplist)
  for i in range(0, l_size-2):
    tmp_l1=[]
    tmp_l1=tmplist[i][0]+":"+tmplist[i][1]
    tmp_l2=tmplist[i+1][0] + ":" + tmplist[i+1][1]
    out_list.append([tmp_l1, tmp_l2])
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
  out_s=create_2word_list(out_s)
  out_s.sort()
  fout = codecs.open("n_list.txt", "w", "utf-8")
  for i in out_s:
    fout.write(i[0] + " " + i[1] + "\n")
