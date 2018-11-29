from selenium import webdriver
from time import sleep

def setting(driver, URL, LogPath):
    input_data(driver, URL, "KDDI01", "Add")
    EditUrl01 = driver.current_url
    sleep(1)
    input_data(driver, URL, "KDDI01", "Add")
    EditUrl02 = driver.current_url
    sleep(1)
    input_data(driver, URL, "KDDI02", "Add")
    EditUrl03 = driver.current_url
    sleep(1)

    EditUrl = driver.current_url

    #録音装置設定のURLを取得
    DeviceAllUrl = EditUrl.replace("kddi/add", "")
    driver.get(DeviceAllUrl)
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sfile = driver.get_screenshot_as_file("%s/複数新規登録(同名も含む).png"%(LogPath))

    input_data(driver, EditUrl01, "変更しましたKDDI01", "Edit")
    sleep(1)
    input_data(driver, EditUrl02, "変更しましたKDDI01", "Edit")
    sleep(1)
    input_data(driver, EditUrl03, "変更しましたKDDI02", "Edit")

    #録音装置設定のURLを取得
    driver.get(DeviceAllUrl)
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sfile = driver.get_screenshot_as_file("%s/複数変更(同名も含む).png"%(LogPath))


    return 0

def move_Line(driver, URL):
    input_data(driver, URL, "KDDI回線設定用", "Add")
    sleep(1)
    AddUrl = driver.current_url
    LineUrl = AddUrl.replace("kddi/edit", "line/kddi")
    driver.get(LineUrl)

    return 0



def input_data(driver, URL, Name, Flag):
    driver.get(URL)
    deviceName = driver.find_element_by_id("deviceName")
    deviceName.clear()
    deviceName.send_keys(Name)

    minPollingInterval = driver.find_element_by_id("minPollingInterval")
    minPollingInterval.clear()
    minPollingInterval.send_keys("1")

    maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
    maxElapsedTime.clear()
    maxElapsedTime.send_keys("1")
    if Flag == "Add":
        kddiAddBtn = driver.find_element_by_id("kddiAddBtn")
        kddiAddBtn.click()
    if Flag == "Edit":
        kddiEditBtn = driver.find_element_by_id("kddiEditBtn")
        kddiEditBtn.click()

    return 0
