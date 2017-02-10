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
    res_list.append(tmp_list)
    n += 1
  f.close()
  return res_list

if __name__ == "__main__":
  resp_list=[]
  filename = "resp_list.txt"
  resp_list=get_source2list(filename)

  num=0

  res_len=len(resp_list)
  myname="ぴぴたん"
  print("あなた :", end="")
  input_line1 = input()
  while (input_line1 is not ""):
    for i in resp_list:
      match0=re.search(input_line1, i[0])
      if match0:
        lst_size=len(i[1])
        word = random.randrange(lst_size)
        print(myname + " :" + i[1][word].strip())
    print("あなた :", end="")
    input_line1 = input()
  print(myname + ": バイバーイ")
