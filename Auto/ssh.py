import paramiko
import time

def PutCommand(RemoteIP, Command ):
    R_HOST=RemoteIP
    R_HOST_USER="nextgen"
    R_HOST_PASS="nextgen"
    error_flg = False
    msg = ""

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(R_HOST, username=R_HOST_USER, password=R_HOST_PASS, port=22, timeout=15.0,look_for_keys=False)

    ssh_shell = ssh.invoke_shell()

    time.sleep(3)
    #コマンドの送信
    ssh_shell.send("%s \n"%(Command))

    time.sleep(3)

    #データの受け取りができていなければエラーとして処理をする
    if (ssh_shell.recv_ready()) and (not error_flg):
        msg += str(ssh_shell.recv(9999)).replace("\r\n", " ")
    else:
        print("error")
        error_flg=True
        ssh.close()
        return 0
