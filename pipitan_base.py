# -*- coding: utf-8 -*-
import sys
import codecs
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
      source.append(str(cnt))
    f.close()
    return source


  def write_log(self, name, words):
    fout = codecs.open("log.csv", "a", "utf-8")
    fout.write(name + "," + words + "\n")
    fout.close

  def input_sentence(self, in_who, in_s):
    self.in_who=in_who
    self.input_s=in_s
    self.write_log(self.in_who, self.input_s)

  def create_response(self):
    self.out_s = "test"
    tmp_list=[]
    mecab=MeCab.Tagger()
    temp_s = mecab.parse(self.input_s)
    temp_list=temp_s.split("\n")
    for row in temp_list:
      out_list=row.split()
      if len(out_list) > 1:
        mecab_k = out_list
        mecab_b = mecab_k[1].split(",")
        if mecab_b[0] == "動詞" or mecab_b[0] == "名詞" or mecab_b[0] == "感動詞":
          tmp_list.append(mecab_k[0])
    self.out_s = str(tmp_list)
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
 

