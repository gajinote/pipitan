# -*- coding : utf-8 -*-
import sys
import random

# 3-gramのファイル読み込み
def read3gram(source):
  f = open("../dic/3gram.txt", "r")
  n = 0
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
      aggregate.append(i[0:tmp])
    #else:
    #  aggregate.append("にゃ")
  return aggregate

# 文字列の生成
def generate_sentence(inp, ngram):
  if  inp.startswith(inp) == True:
    top_char = inp[0]
  else:
    top_char = "ゃ"
  print("開始文字は" + "'" + inp + "'")

  size_ng=len(ngram)
  word = random.randrange(size_ng-1)
  
  prn_string=""
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
      prn_string += "にょお"
      top_char ="お"
      continue
    word = random.randrange(size_ng)
    out_str=extr_str[word]
    prn_string = prn_string + out_str[0] + out_str[1]

    i += 1
    top_char = out_str[-1]
    #print(top_char)
    #print(prn_string)
    # prn_string = out_str[3]
  return prn_string

if __name__ == "__main__":
  # 乱数の初期化
  rnd = random.seed()
  source = ""
  #print(random.random())
  # 3-gram ファイルの読み込み
  source = read3gram(source)
  #print(type(source))

  ngram = source.split("\n")

  input_char=""
  while(input_char =="" ):
    print("開始文字を入力してください")
    input_char = input()
  
  print(generate_sentence(input_char,ngram))

