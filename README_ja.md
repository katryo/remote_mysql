remote_mysql
============

Python2を使って、

1. MySQLを操作するPythonコードのファイルをサーバに転送する
2. 転送先サーバでPythonコードを実行してMySQLからデータを取得する
3. 実行結果をクライアント側端末で取得する

という一連の流れを1コマンドで順次実行するツールです。

## 依存ライブラリ・バージョン
- [paramiko](https://github.com/paramiko/paramiko)
- [MySQLdb](http://mysql-python.sourceforge.net/)

に依存しています。

2014年1月7日現在、どちらもPython2系列で動きます。Python3系列では動きません。

なので、Python2系列で使ってください。

## 使い方
### パスワードなど設定
secrets.pyというファイルを作って、

```
hostname = 'ourserver'
port = 22
server_username = 'katryo'
server_password = 'abcedfg'
db_name = 'mydatabase'
db_username = 'katryo'
db_password = 'hijklmn'
```

という風に、外部に知られたくないことがらを設定します。

### 実行する

```
$ python put_code_and_exec_it_in_server.py
```

ですべての処理を行い、結果がターミナルに出ます。

### SQLを変更する
初期状態ではsql_commands.pyは

```
sample_1 = 'select * from all_hyponymy where hyponym = "カードゲーム" limit 5;'
sample_2 = 'select * from all_hyponymy where hypernym = "経験" limit 5;'

```

となっており、sample_2のSQLコマンドを実行するようになっています。

sql_commands.pyを書き換えるか、load_from_mysql.pyの

```
cursor.execute(sql_commands.sample_2)
```

の部分を書き換えてください。


## 目的
[京都大学情報学研究科社会情報学専攻田中研究室](http://www.dl.kuis.kyoto-u.ac.jp/)のサーバ作業支援を目的に作りました。

## 参考
Thanks to http://d.hatena.ne.jp/yuheiomori0718/20121031/1351692579