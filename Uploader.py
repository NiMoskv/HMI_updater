import paramiko
import paramiko

host = '192.168.1.99'
user = 'root'
secret = '1'
port = 22

transport = paramiko.Transport((host, port))
transport.connect(hostname=host, username=user, password=secret, port=port)
sftp = paramiko.SFTPClient.from_transport(transport)

remotepath = ''
localpath = ''

sftp.get(remotepath, localpath)
sftp.put(localpath, remotepath)

sftp.close()
transport.close()
