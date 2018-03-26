# -*- coding: utf-8 -*-
import sys
import MeCab

# ファイルの読み込み
def fs_open(param):
  source=""
  f = open(param, "r")
  for i in f:
    source += i
  f.close()
  return source

# MeCabによる形態素分解
def output_mecab(target):
  mecab=MeCab.Tagger("")
  retVal=mecab.parse(target)
  return retVal.split("\n")

# convert mecab to list
def conv_mecab_to_list(mecab):
  tmp_list=[]
  tmp2_list=[]
  hdn_list=[]
  out_list=[]
  for i in mecab:
    tmp_list=i.split("\t")
    if tmp_list[0] != "EOS":
      cnt = 0
      for j in tmp_list:
        if cnt == 0:
          hdn_list.append(j)
        elif cnt == 1:
          tmp2_list=j.split(",")
          for k in tmp2_list:
             hdn_list.append(k)
        cnt += 1
      # hdn_list.append(tmp_list[1])
      #tmp2_list=tmp_list[1].split(",")
      #for j in tmp2_list:
      #  hdn_list.append(j)
    out_list.append(hdn_list)
    hdn_list=[]
  return out_list

if __name__ == "__main__":
  f_source=""
  m_list=[]
  param = sys.argv
  f_source = fs_open(param[1])
  o_mecab = output_mecab(f_source)
  
  m_list = conv_mecab_to_list(o_mecab)
 
  m_list.sort() 
  for i in m_list:
    print(i)
