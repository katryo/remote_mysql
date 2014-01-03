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
        print('try connect!')

        client.connect(hostname=secrets.hostname, port=secrets.port, username=secrets.username, password=secrets.password)
        print('connect!!!!')
        sftp_connection = client.open_sftp()

        # ホームディレクトリのファイル一覧をprint
        files = sftp_connection.listdir()
        for remote_file in files:
            print(remote_file)

        # ファイルを取得
        sftp_connection.get('test.py', 'test.py')

        # ファイルを転送
        # sftp_connection.put('/path/to/localfile', '/path/to/remote')

    except:
        raise
    finally:
        if client:
            client.close()
        if sftp_connection:
            sftp_connection.close()