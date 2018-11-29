from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import shutil

voisIP = "192.168.33.71"
LogPath = "C:\Auto\phone"

driver = webdriver.Chrome("c:/driver/chromedriver.exe")
driver.get("http://%s/voisplusm/"%(voisIP))
sleep(1)
#スクリーンショットを取得し保存
sfile = driver.get_screenshot_as_file("%s/携帯ログイン画面.png"%(LogPath))

sleep(1)
driver.find_element_by_class_name("text-input").send_keys("nxgadmin",Keys.TAB,"nxgadmin")
sleep(1)
driver.find_element_by_class_name("button").click()
sleep(1)
#スクリーンショットを取得し保存
sfile = driver.get_screenshot_as_file("%s/携帯検索画面.png"%(LogPath))


##検索画面
StartTime = driver.find_element_by_class_name("text-input")
StartTime.send_keys("2018",Keys.TAB,"10","22",Keys.TAB,"17", "10", Keys.TAB,"2018",Keys.TAB,"10","23",Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB)
sleep(1)
driver.find_element_by_class_name("button").click()
sleep(1)
#スクリーンショットを取得し保存
sfile = driver.get_screenshot_as_file("%s/携帯検索結果画面.png"%(LogPath))



#検索結果画面から再生画面への遷移が難しいので後回し
driver.find_element_by_xpath("//ons-list-item/div[2]").click()
sleep(1)
#スクリーンショットを取得し保存
sfile = driver.get_screenshot_as_file("%s/音声データ再生画面.png"%(LogPath))
sleep(1)
