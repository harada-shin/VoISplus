from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import subprocess
import shutil


driver = webdriver.Chrome("c:/driver/chromedriver.exe")
driver.get("http://192.168.34.26/voisplus/")


#ログイン情報入力
elem_search_word = driver.find_element_by_id("loginId")
elem_search_word.send_keys("auto_taro")
elem_search_word = driver.find_element_by_id("password")
elem_search_word.send_keys("auto_taro_001")
#ログイン
elem_search_btn = driver.find_element_by_id("login-btn")
elem_search_btn.click()

#カレントウインドウを最大化する
driver.maximize_window()


#本体設定変更画面に遷移
driver.get("http://192.168.34.26/voisplus/device/la6000/edit/1")

sleep(1)

#レコードタブへ遷移
goToRecorder = driver.find_element_by_id("goToRecorder")
goToRecorder.click()
driver.execute_script("document.body.style.zoom='80%'")
sleep(1)
#初期情報をスクリーンショットを取得し保存
sfile = driver.get_screenshot_as_file("c:/Auto/logs/初期値/Recorder_init.png")
#カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
print(sfile)
driver.execute_script("document.body.style.zoom='100%'")
sleep(1)
