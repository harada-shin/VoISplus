from time import sleep
from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient
import shutil

#本体設定の初期画面確認
def setting(driver, URL, LogPath):
    #本体設定変更画面に遷移
    driver.get(URL)

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/本体設定＿初期画面.png"%LogPath)

    return 0
'''
#LA-6000の初期画面確認
def La6k(driver, URL, LogPath,La6kIP):

    #本体設定変更画面に遷移
    driver.get(URL)

    sleep(1)

    #レコードタブへ遷移
    goToRecorder = driver.find_element_by_id("goToRecorder")
    goToRecorder.click()
    driver.execute_script("document.body.style.zoom='80%'")
    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/Recorder_初期画面.png"%LogPath)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)
    driver.execute_script("document.body.style.zoom='100%'")
    sleep(1)


    #ネットワークデバイスタブへ遷移
    goToDevice = driver.find_element_by_id("goToDevice")
    goToDevice.click()
    driver.execute_script("document.body.style.zoom='60%'")
    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/Device_初期画面.png"%LogPath)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)
    driver.execute_script("document.body.style.zoom='100%'")
    sleep(1)


    #VOIPタブへ遷移
    goToVoip = driver.find_element_by_id("goToVoip")
    goToVoip.click()
    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/Voip_初期画面.png"%LogPath)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)

    #録音チャネルタブへ遷移
    goToChannel = driver.find_element_by_id("goToChannel")
    goToChannel.click()
    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/Chanel_初期画面.png"%LogPath)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)

    #端末設定タブへ遷移
    goToTel = driver.find_element_by_id("goToTel")
    goToTel.click()
    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/Tel_初期画面.png"%LogPath)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)


    #ファイル転送
    send_vliuser(La6kIP, LogPath, "初期設定")

    return 0
'''

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
