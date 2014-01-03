# coding=utf-8
from __future__ import print_function
from __future__ import unicode_literals
import MySQLdb
import secrets
import sql_commands

connection = MySQLdb.connect(db=secrets.db_name, user=secrets.db_root_user, passwd=secrets.db_password, charset='utf8')

cursor = connection.cursor()
cursor.execute(sql_commands.sample_2)
result = cursor.fetchall()
for row in result:
    print(row[0] + row[1] + str(row[2]) + row[3])

cursor.close()
connection.close()
