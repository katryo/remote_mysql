# coding=utf-8
from __future__ import print_function
from __future__ import unicode_literals
import paramiko
import secrets
import filenames

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
        put_filenames = [filenames.code_executed_in_server, filenames.password_and_etc, filenames.sql_commands]
        for filename in put_filenames:
            sftp_connection.put(filename, filename)
        command = 'python %s' % filenames.code_executed_in_server
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