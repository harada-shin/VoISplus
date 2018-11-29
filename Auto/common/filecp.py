from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient
import iptable
import shutil

def La6kToLocal(la6k_filename, newFilename):
    HOST = iptable.la6k()
    PORT = "22"
    USER = "nextgen"
    PSWD = "nextgen"

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(HOST, port=PORT, username=USER, password=PSWD)

    scp = SCPClient(ssh.get_transport())
    scp.get("/home/nextgen/NXS/conf/%s"%(la6k_filename))

    shutil.move('vliuser.ini', '%s'%(newFilename))

    return 0
