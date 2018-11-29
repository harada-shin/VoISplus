from selenium import webdriver
from selenium.webdriver.support.select import Select

def setting():
####最小値設定###################################################################
    deviceName = driver.find_element_by_id("deviceName")
    deviceName.send_keys("a")

    ipAddr = driver.find_element_by_id("ipAddr")
    ipAddr.send_keys("%s"%(ip))

    #anonymousFlag = driver.find_element_by_id("anonymousFlag")
    #anonymousFlag.click()

    minPollingInterval = driver.find_element_by_id("minPollingInterval")
    minPollingInterval.send_keys("1")

    maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
    maxElapsedTime.send_keys("1")

    maxCollectScope = driver.find_element_by_id("maxCollectScope")
    maxCollectScope.send_keys("1")

    userId = driver.find_element_by_id("userId")
    userId.send_keys("1")

    passwd = driver.find_element_by_id("passwd")
    passwd.send_keys("1")

    e1010AddBtn = driver.find_element_by_id("e1010AddBtn")
    e1010AddBtn.click()

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/%s_min.png"%(LogPath, FileName))

    #ページを更新
    driver.refresh()
################################################################################


    return 0
