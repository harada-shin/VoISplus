from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import login

URL = "http://192.168.33.38/voisplus/device/"
driver = webdriver.Chrome("c:/driver/chromedriver.exe")
login.login(driver,"nxgadmin","nxgadmin_001")
sleep(1)
def collection(driver, machineID):
    sleep(1)
    #
    driver.find_element_by_xpath("//tr[%s]/td[10]/button"%(machineID)).click()
    sleep(2)
    #「収集設定を変更しますか？」確認画面OKをクリック
    driver.find_element_by_xpath("//div[2]/button").click()
    sleep(1)
    return 0
