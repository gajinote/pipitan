# -*- coding: utf-8 -*-
import sys
import random
import MeCab
import codecs

resp_list = [["かわいい", [ "照れる～","知ってた"]], ["ばか", ["ひどい！", "馬鹿っていう方がばかだ"]], ["疲れる", ["なんで？", "かわいそうに"]]]

def create_resp(input_line, n_list):
  for i in resp_list:
    if i[0] == input_line:
      r_size = len(i[1])
      r_num = random.randint(0, r_size-1)
      return i[1][r_num]
  return "なんですって？もう一度お願いします" 

if __name__ == "__main__":
  # 乱数の初期化
  rnd = random.seed()
  source=""
  # response ファイルの読み込み
  #source = read3gram(source)
  ngram = resp_list

  myname="ぴぴたん"
  print( myname + ":メッセージをどうぞ")
  print("あなた :", end="")

  input_line1 = input()
  while (input_line1 is not ""):
    response = create_resp(input_line1, ngram)
    print( myname + ":" + str(response) )
    print("あなた :", end="")
    input_line1 = input()
  print( myname + ":バイばーい")
