人口無能発展型人格インターフェース
=

通称 Pipi（ぴぴたん）
まだ実験段階です。

## 動作環境
python 3.4以上
meCab インストール環境

# 開発環境
ubuntu 16.04LTS + anaconda 3.5.1
python3.5

# Directory構成

-------------------------------------

/dic ・・・ 辞書用テキストファイル保存ディレクトリ

/sample_tools ・・・ サンプルプログラム集

pipi_if.py ... Prototype ぴぴたん

resp_if.py ... 応答確認スクリプト

-------------------------------------


## 3gram.txtの生成
  $ python make3gram.py (source text) 

## n-list.txtの生成
　$ python make_n_list.py (source text) 

## 3gram.txtから文章を生成する方法
  $ python generate_fm3.py

## n_list.txtから文章を生成する方法
  $ python generate_fm_hm.py

## **.txtから文章の品詞構成をリスト化する方法
　$ python create_grammer_list.py **.txt

##  **.txtに含まれる文章から単語をMeCabリスト形式に出力
  $ python create_mecab_data.py **.txt

## 人口無能ぴーぴとの会話
　$ python pipi_if.py

  コマンドラインコンソールで会話できます。
  テキストで呼びかけるとなんとなくn_list.txtから文章を生成して返答してくれます。

  まだ辞書と乱数から生成しているので意味の通る文章になりません。

  空白エンターを入力するとプログラムを終了します。

# Version Information
2016-08-28 :version 0.01
  初期バージョン公開

2017-02-18 :version 0.02
  resp_list.txtに記述されたルールに従い、指定された単語に反応を返す機能を追加
  単語辞書n_list.txtの単語数を追加

2018-02-18 :Directory構成のみ変更