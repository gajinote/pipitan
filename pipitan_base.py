# -*- coding: utf-8 -*-
import sys
import codecs

class PipitanBase:
  def __init__(self,status):
    self.in_who="taro"
    self.input_s="test"
    self.emotion = status

  def input_sentence(self, in_who, in_s):
    self.in_who=in_who
    self.input_s=in_s
    fout = codecs.open("log.csv", "a", "utf-8")
    fout.write(self.in_who + "," + self.input_s + "\n")
    fout.close

  def create_response(self):
    self.out_s = "test"
    return self.out_s

  def time_handler(self):
    self.startUpTime=10
    self.interval=10

  def main(self):
    who=input()
    while(1):
      temp_i=input()
      self.input_sentence(str(who),str(temp_i))
      print(self.create_response())

if __name__ == "__main__":
  VER="0.02"
  print("version = " + VER)
  pipi_c=PipitanBase("normal")
  pipi_c.main()
 

