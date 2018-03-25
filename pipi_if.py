# -*- coding: utf-8 -*-
import sys
import random
import MeCab
import codecs
import re

# 3-gram ファイルの読み込み
def read3gram(source):
  f = codecs.open("n_list.txt", "r", "utf-8")
  for cnt in f:
    source += cnt
  f.close()
  return source

# 文字列集合の作成
def create_aggregation(top, source):
  # print(top)
  aggregate=[]
  for i in source:
    tmp=len(i)
    if i.startswith(top) != False :
      print(i[0:tmp])
      tmp_l=i[0:tmp].split(" ")
      tmp_m=tmp_l[0].split(":")
      aggregate.append(tmp_m)
  return aggregate

# 文字列の生成
def generate_sentence(inp, ngram):
  if  inp.startswith(inp) == True:
    top_char = inp[-1]
  else:
    top_char = "ゃ"

  size_ng=len(ngram)
  word = random.randrange(size_ng-1)
  
  prn_string=inp
  out_str=top_char
  count = 0
  for count in range(1, 30):
    i = 0
    extr_str=create_aggregation(top_char, ngram)
    if (extr_str == False) or (extr_str is None):
      prn_string+="にゃ？"
      top_char ="？"
      continue
    size_ng=len(extr_str)
    if (size_ng < 2) or (size_ng is None):
      prn_string += "メール"
      top_char ="メール"
      continue
    word = random.randrange(size_ng)
    out_str=extr_str[word]
    prn_string = prn_string + out_str[1]

    i += 1
    top_char = out_str[-1]
  return prn_string

# Response_listを読みだす
def get_source2list():
  n=0
  res_lst=[]
  i=[]
  f = codecs.open("resp_list.txt", "r", "utf-8")
  for i in f:
    tmp_lst=[]
    tmp = i.split(",")
    tmp_lst.append(tmp[0])
    tmp_lst.append(tmp[1:])
    res_lst.append(tmp_lst)
  f.close()
  return res_lst

# 応答の作成
def create_resp(input_l, ngram, resp_l):
  mecab=MeCab.Tagger()
  output=mecab.parse(input_l)

  # print(output)
  # lists=output
  
  # resp_l内の単語が一致したら応答を返す
  # for i_l in lists:
  #    for r_l in resp_l:
  #      match0=re.search(i_l, r_l[0])
  #      if match0:
  #       lst_size=len(r_l[1])
  #       word = random.randrange(lst_size)
  #       return r_l[1][word].strip()
  
  lists = output.split()
  tmp_l=""
  tmp_l = lists[0]
  # lst_size=len(lists)
  # word = random.randrange(lst_size)
  # tmp_l = lists[word].split(":")
  return tmp_l
  # return generate_sentence(lists[word], ngram)

if __name__ == "__main__":
  prog_version="0.02"
  print("ぴぴたん Version: " + prog_version + " Start!!")
  # 乱数の初期化
  rnd = random.seed()
  source=""
  # 3-gram ファイルの読み込み
  source = read3gram(source)
  ngram = source.split("\n")

  # response listの読み込み
  resp_list=[]
  resp_list=get_source2list()

  myname="ぴぴたん"
  print( myname + ":メッセージをどうぞ")
  print("あなた :", end="")

  input_line1 = input()
  while (input_line1 is not ""):
    response = create_resp(input_line1, ngram, resp_list)
    print( myname + ":" + str(response) )
    print("あなた :", end="")
    input_line1 = input()
  print( myname + ":バイばーい")
  
    
