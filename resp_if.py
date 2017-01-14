# -*- coding: utf-8 -*-
import sys
import codecs
import random
import re

#Textを読み込みリストを返す
def get_source2list(src):
  n = 0
  res_list=[]
  tmp_list=[]
  i = []
  f = codecs.open("resp_list.txt", "r", "utf-8")
  for i in f:
    tmp_list=[]
    tmp = i.split(",")
    tmp_list.append(tmp[0])
    tmp_list.append(tmp[1:])
    # print(tmp_list)
    res_list.append(tmp_list)
    n += 1
  f.close()
  return res_list

if __name__ == "__main__":
  resp_list=[]
  filename = "resp_list.txt"
  resp_list=get_source2list(filename)

  # print(resp_list)
  num=0
  # for i in resp_list:
  #    print(i[1])

  res_len=len(resp_list)
  # print(resp_list[0])
  # out_w=res_len[0]
  # print(out_w)

  input_line1 = input()
  while (input_line1 is not ""):
    for i in resp_list:
      # if(input_line1 is resp_list[0]):
      # print(i)
      match0=re.search(input_line1, i[0])
      if match0:
        print(match0)
        print(i[1][0])
      # else:
      #   print("なんですって？")
    input_line1 = input()
  print("バイバーイ")
