from selenium import webdriver
from time import sleep
import iptable

def login(driver,LoginID,PWD):

    voisIP = iptable.VoIS
    driver.get("http://%s/voisplus/"%(voisIP))

    loginId = driver.find_element_by_id("loginId")
    loginId.send_keys(LoginID)
    Password = driver.find_element_by_id("password")
    Password.send_keys(PWD)
    #ログイン
    Login_btn = driver.find_element_by_id("login-btn")
    Login_btn.click()

    #カレントウインドウを最大化する
    driver.maximize_window()

    return 0
