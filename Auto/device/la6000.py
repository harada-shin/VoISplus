from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient
import shutil
from time import sleep

#LA-6000の装置登録
def setting(driver,voisIP, la6kIP, LogPass, URL):
    #本体設定変更画面に遷移
    driver.get(URL)
    sleep(1)
    deviceName = driver.find_element_by_id("deviceName")
    deviceName.send_keys("auto_la6000")
    sleep(1)
    ipAddr = driver.find_element_by_id("ipAddr")
    ipAddr.send_keys("%s"%(voisIP))
    sleep(1)
    minPollingInterval = driver.find_element_by_id("minPollingInterval")
    minPollingInterval.send_keys("1")
    sleep(1)
    maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
    maxElapsedTime.send_keys("10")
    sleep(1)
    sshKeyExchgBtn = driver.find_element_by_id("sshKeyExchgBtn")
    sshKeyExchgBtn.click()
    sleep(1)
    sshPassword = driver.find_element_by_id("sshPassword")
    sshPassword.send_keys("nextgen",Keys.TAB)
    sleep(1)
    keyExchange = driver.find_element_by_id("key-exchange")
    keyExchange.click()
    sleep(1)
    keyExchangeCancel = driver.find_element_by_id("key-exchange-cancel")
    keyExchangeCancel.click()
    sleep(1)
    connectTest = driver.find_element_by_id("connect-test")
    connectTest.click()
    sleep(1)
    la6000AddBtn = driver.find_element_by_id("la6000AddBtn")
    la6000AddBtn.click()
    sleep(1)
    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/la6000登録完了.png"%(LogPass))

    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)
    sleep(1)
    #カレントページのURLを取得
    EditUrl = driver.current_url
    La6k(driver, EditUrl, LogPass, la6kIP)


    #回線設定画面のURLを取得
    LineUrl = EditUrl.replace("la6000/edit", "line/la6000")
    sleep(1)
    #回線設定画面に遷移
    driver.get(LineUrl)
    sfile = driver.get_screenshot_as_file("%s/LA6K回線設定画面.png"%(LogPass))
    addbtn = driver.find_element_by_id("add_btn")
    addbtn.click()
    sfile = driver.get_screenshot_as_file("%s/LA6K回線設定追加画面.png"%(LogPass))
    driver.refresh()

    return 0


#LA-6000の初期画面確認
def La6k(driver, URL, LogPass,La6kIP):

    #本体設定変更画面に遷移
    driver.get(URL)

    sleep(1)

    #レコードタブへ遷移
    goToRecorder = driver.find_element_by_id("goToRecorder")
    goToRecorder.click()
    driver.execute_script("document.body.style.zoom='80%'")
    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/Recorder_初期画面.png"%LogPass)
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
    sfile = driver.get_screenshot_as_file("%s/Device_初期画面.png"%LogPass)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)
    driver.execute_script("document.body.style.zoom='100%'")
    sleep(1)


    #VOIPタブへ遷移
    goToVoip = driver.find_element_by_id("goToVoip")
    goToVoip.click()
    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/Voip_初期画面.png"%LogPass)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)

    #録音チャネルタブへ遷移
    goToChannel = driver.find_element_by_id("goToChannel")
    goToChannel.click()
    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/Chanel_初期画面.png"%LogPass)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)

    #端末設定タブへ遷移
    goToTel = driver.find_element_by_id("goToTel")
    goToTel.click()
    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/Tel_初期画面.png"%LogPass)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)


    #ファイル転送
    send_vliuser(La6kIP, LogPass, "初期設定")

    return 0

def send_vliuser(La6kIP, LogPass, Filename):
        HOST = "%s"%(La6kIP)
        PORT = "22"
        USER = "nextgen"
        PSWD = "nextgen"

        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(HOST, port=PORT, username=USER, password=PSWD)

        scp = SCPClient(ssh.get_transport())
        scp.get("/home/nextgen/NXS/conf/vliuser.ini")

        shutil.move("vliuser.ini", "%s/vliuser_%s.ini"%(LogPass, Filename))

        return 0
