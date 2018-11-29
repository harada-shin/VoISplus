from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
driver.get("http://192.168.34.26/voisplus/device/vr508/add")

#スクリーンショットを取得し保存
sfile = driver.get_screenshot_as_file("c:/Auto/logs/device_takacom_init.png")

#カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
print(sfile)

deviceName = driver.find_element_by_id("deviceName")
deviceName.send_keys("auto_takacom")

ipAddr = driver.find_element_by_id("ipAddr")
ipAddr.send_keys("192.168.34.26")

minPollingInterval = driver.find_element_by_id("minPollingInterval")
minPollingInterval.send_keys("1")

maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
maxElapsedTime.send_keys("10")

sshKeyExchgBtn = driver.find_element_by_id("sshKeyExchgBtn")
sshKeyExchgBtn.click()

sshPassword = driver.find_element_by_id("sshPassword")
sshPassword.send_keys("nextgen",Keys.TAB)

keyExchange = driver.find_element_by_id("key-exchange")
keyExchange.click()

keyExchangeCancel = driver.find_element_by_id("key-exchange-cancel")
keyExchangeCancel.click()

connectTest = driver.find_element_by_id("connect-test")
connectTest.click()

la6000AddBtn = driver.find_element_by_id("la6000AddBtn")
la6000AddBtn.click()

#スクリーンショットを取得し保存
sfile = driver.get_screenshot_as_file("c:/Auto/logs/device_la6000.png")

#カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
print(sfile)

#本体設定変更画面に遷移
driver.get("http://192.168.34.26/voisplus/device/")

#スクリーンショットを取得し保存
sfile = driver.get_screenshot_as_file("c:/Auto/logs/device_all.png")

#カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
print(sfile)
