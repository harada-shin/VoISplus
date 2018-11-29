from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient
import shutil

def send_vliuser(La6kIP, LogPath, Filename):
        HOST = "%s"%(La6kIP)
        PORT = "22"
        USER = "nextgen"
        PSWD = "nextgen"

        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(HOST, port=PORT, username=USER, password=PSWD)

        scp = SCPClient(ssh.get_transport())
        scp.get("/home/nextgen/NXS/conf/vliuser.ini")

        shutil.move("vliuser.ini", "%s/vliuser_%s.ini"%(LogPath, Filename))

    return 0
