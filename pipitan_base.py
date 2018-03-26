# -*- coding: utf-8 -*-
import sys
import codecs
import MeCab

class PipitanBase:
  def __init__(self,status):
    self.my_name="pipitan"
    self.in_who="taro"
    self.input_s="test"
    self.emotion = status
    self.source=[]
    self.source=self.read_nlist()
    print(self.source)

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
    self.write_log(self.my_name, self.out_s)
    return self.out_s

  def time_handler(self):
    self.startUpTime=10
    self.interval=10

  def main(self):
    who=str(input())
    while(1):
      temp_i=input()
      self.input_sentence(str(who),str(temp_i))
      print(self.create_response())

if __name__ == "__main__":
  VER="0.03"
  print("version = " + VER)
  pipi_c=PipitanBase("normal")
  pipi_c.main()
 

