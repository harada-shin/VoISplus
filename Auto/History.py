from selenium import webdriver
from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient
from selenium.webdriver.common.keys import Keys
from time import sleep
import shutil
import datetime

def VoiceOperation(driver, URL, LogPath):
    driver.get(URL)
    sleep(1)
    driver.find_element_by_id("startDate").clear()
    driver.find_element_by_id("startDate").send_keys("2018/10/01",Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB)
    sleep(1)
    driver.find_element_by_id("searchBtn").click()
    sleep(1)

    driver.execute_script("document.body.style.zoom='25%'")
    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/音声操作履歴.png"%LogPath)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)
    driver.execute_script("document.body.style.zoom='100%'")
    sleep(1)

    #履歴をエクスポートする
    driver.find_element_by_id("exportBtn").click()
    d = datetime.datetime.now()
    print("OperationHistoryDownloadTime:", d)
    sleep(2)
    return 0

def Login(driver, URL, LogPath):
    driver.get(URL)
    sleep(1)
    #driver.find_element_by_id("startDate").clear()
    #driver.find_element_by_id("startDate").send_keys("2018/10/01",Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB)
    #sleep(1)
    driver.find_element_by_id("btnSearch").click()
    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/ログイン履歴.png"%LogPath)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)

    sleep(1)

    #履歴をエクスポートする
    driver.find_element_by_id("exportBtn").click()
    d = datetime.datetime.now()
    print("LoginHistoryDownloadTime:", d)
    sleep(2)
    return 0

def Alarm(driver, URL, LogPath):
    driver.get(URL)
    sleep(1)
    driver.find_element_by_id("startDate").clear()
    driver.find_element_by_id("startDate").send_keys("2018/09/27",Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB)
    sleep(1)
    driver.find_element_by_id("btnSearch").click()
    sleep(1)

    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/アラーム履歴.png"%LogPath)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)

    sleep(1)

    #履歴をエクスポートする
    driver.find_element_by_id("exportBtn").click()
    d = datetime.datetime.now()
    print("AlarmHistoryDownloadTime:", d)
    sleep(2)
    return 0

def Backup(driver, URL, LogPath):
    driver.get(URL)
    sleep(1)
    driver.find_element_by_id("startDate").clear()
    driver.find_element_by_id("startDate").send_keys("2018/09/20",Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB)
    sleep(1)
    driver.find_element_by_id("searchBtn").click()
    sleep(1)
    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/バックアップ履歴.png"%LogPath)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)
    sleep(1)

    #履歴をエクスポートする
    driver.find_element_by_id("exportBtn").click()
    d = datetime.datetime.now()
    print("BackupHistoryDownloadTime:", d)
    sleep(2)
    return 0

def Collectionfile(driver, URL, LogPath):
    driver.get(URL)
    sleep(1)
    driver.find_element_by_id("startDate").clear()
    driver.find_element_by_id("startDate").send_keys("2018/09/20",Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB)
    sleep(1)
    driver.find_element_by_id("searchBtn").click()
    sleep(1)
    #履歴をエクスポートする
    driver.find_element_by_id("exportBtn").click()
    d = datetime.datetime.now()
    print("CollectionfileHistoryDownloadTime:", d)
    sleep(2)
    sfile = driver.get_screenshot_as_file("%s/音声ファイル収集履歴1.png"%LogPath)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    sfile = driver.get_screenshot_as_file("%s/音声ファイル収集履歴2.png"%LogPath)
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)

    return 0
