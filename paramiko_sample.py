# coding=utf-8
from __future__ import print_function
from __future__ import unicode_literals
import paramiko
import secrets

if __name__ == '__main__':

    client = None
    sftp_connection = None
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print('try connecting...')
        client.connect(hostname=secrets.hostname, port=secrets.port, username=secrets.username, password=secrets.password)
        print('connected!')
        sftp_connection = client.open_sftp()

        # ファイルを取得
        # sftp_connection.get('test.py', 'test.py')

        # ファイルを転送
        sftp_connection.put('load_from_mysql.py', 'load_from_mysql.py')
        sftp_connection.put('secrets.py', 'secrets.py')
        command = 'python load_from_mysql.py'
        (stdin, stdout, stderr) = client.exec_command(command)
        for line in stdout.readlines():
            print(line)

    except:
        raise
    finally:
        if client:
            client.close()
        if sftp_connection:
            sftp_connection.close()