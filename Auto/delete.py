from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import login
import Pass
import iptable
from device import takacom
from device import webdav
import search


driver = webdriver.Chrome("c:/driver/chromedriver.exe")

login.login(driver,"auto_taro","auto_taro_001")

driver.get("http://192.168.34.26/voisplus/device")

element = driver.find_element_by_class_name("btn btn-link btn-sm")
element.click()
