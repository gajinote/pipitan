# -*- coding: utf-8 -*-
import sys
import codecs
import random
import MeCab

class PipitanBase:
  def __init__(self,status):
    self.my_name="ぴぴたん"
    self.in_who="たろう"
    self.input_s="test"
    self.emotion = status
    self.source=[]
    self.source=self.read_nlist()

  def read_nlist(self):
    f = codecs.open("./dic/n_list.txt", "r", "utf-8")
    source=[]
    for cnt in f:
      source.append(str(cnt.replace("\n","")))
    f.close()
    return source


  def write_log(self, name, words):
    fout = codecs.open("./log/log.csv", "a", "utf-8")
    fout.write(name + "," + words + "\n")
    fout.close

  def input_sentence(self, in_who, in_s):
    self.in_who=in_who
    self.input_s=in_s
    self.write_log(self.in_who, self.input_s)

  # 文章の生成
  def generate_sentence(self, t_list):
    output_str=""
    next_list=[]
    size_nl=len(self.source)
    word = random.randrange(size_nl-1)

    cnt=0
    while cnt < 30: 
      for s_list in self.source:
        if s_list.startswith(t_list) == True:
          next_list.append(s_list)
      if len(next_list) > 0:
        pick=random.randrange(len(next_list))
        # print(str(next_list[pick]))
        t_list=next_list[pick].split()[1]
      else:
        t_list="メール"
      output_str+=t_list
      next_list=[]
      cnt += 1
    return output_str

  def create_response(self):
    self.out_s = "test"
    tmp_list=[]
    mecab=MeCab.Tagger()
    temp_s = mecab.parse(self.input_s).split("\n")
    for row in temp_s:
      out_list=row.split()
      if len(out_list) > 1:
        mecab_k = out_list
        mecab_b = mecab_k[1].split(",")
        if mecab_b[0] == "動詞" or mecab_b[0] == "名詞" or mecab_b[0] == "感動詞":
          tmp_list.append(mecab_k[0])
    # キーワードの抽出
    word=random.randrange(len(tmp_list))

    self.out_s = str(tmp_list) + str(word)
    # print("tmp out = " + str(self.out_s), tmp_list[word]) 
    self.out_s = self.generate_sentence(tmp_list[word])

    self.write_log(self.my_name, self.out_s)
    return self.out_s

  def time_handler(self):
    self.startUpTime=10
    self.interval=10

  def main(self):
    print("あなたの名前は？:", end="")
    who=str(input())
    print(self.my_name + " : " + "こんにちは、" + who + "さん")
    print(self.my_name + " : メッセージをどうぞ")
    print("あなた : ", end="")
    temp_i=input()
    while(temp_i is not ""):
      self.input_sentence(str(who),str(temp_i))
      print(self.my_name + " : " + self.create_response())
      print("あなた : ", end="")
      temp_i=input()
    print(self.my_name + ": バイバーイ")

if __name__ == "__main__":
  VER="0.03"
  print("version = " + VER)
  pipi_c=PipitanBase("normal")
  pipi_c.main()
 

