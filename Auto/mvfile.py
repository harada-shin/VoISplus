from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(HOST, port=PORT, username=USER, password=PSWD)

scp = SCPClient(ssh.get_transport())
scp.get("/home/nextgen/NXS/conf/vliuser.ini")
