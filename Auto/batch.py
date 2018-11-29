from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient
from time import sleep
import os

def Put(La6kIP, Local_Path, Remote_Path):
    list = os.listdir("%s"%(Local_Path))

    HOST = "%s"%(La6kIP)
    PORT = "22"
    USER = "nextgen"
    PSWD = "nextgen"

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(HOST, port=PORT, username=USER, password=PSWD)

    scp = SCPClient(ssh.get_transport())
    for cnt in range(len(list)):
        # Upload one fille to the remote directry
        scp.put("%s%s"%(Local_Path, list[cnt]), recursive=True, remote_path=Remote_Path)

    scp.close()

    sleep(60)

    return 0
