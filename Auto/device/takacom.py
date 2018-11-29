from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

def VR(driver,ip,URL, LogPath, FileName):
    #タカコム登録画面に移動
    driver.get(URL)

####未設定確認###################################################################
    vr500AddBtn = driver.find_element_by_id("vr500AddBtn")
    vr500AddBtn.click()

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/%s未設定.png"%(LogPath, FileName))

    #ページを更新
    driver.refresh()
################################################################################

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

    collectFlag = driver.find_element_by_id("collectFlag")
    collectFlag.click()

    userId = driver.find_element_by_id("userId")
    userId.send_keys("1")

    passwd = driver.find_element_by_id("passwd")
    passwd.send_keys("1")

    wavChannelMode = driver.find_element_by_id("wavChannelMode")
    mode = Select(wavChannelMode)
    mode.select_by_visible_text("モノラル")

    vr500AddBtn = driver.find_element_by_id("vr500AddBtn")
    vr500AddBtn.click()

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/%s最小値設定.png"%(LogPath, FileName))

    #ページを更新
    driver.refresh()
################################################################################

####最大値設定###################################################################
    deviceName = driver.find_element_by_id("deviceName")
    deviceName.clear()
    deviceName.send_keys("aaaaabbbbbcccccdddddeeeeefffffgg")

    ipAddr = driver.find_element_by_id("ipAddr")
    ipAddr.clear()
    ipAddr.send_keys("%s"%(ip))

    #anonymousFlag = driver.find_element_by_id("anonymousFlag")
    #anonymousFlag.click()

    minPollingInterval = driver.find_element_by_id("minPollingInterval")
    minPollingInterval.clear()
    minPollingInterval.send_keys("1440")

    maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
    maxElapsedTime.clear()
    maxElapsedTime.send_keys("1440")

    maxCollectScope = driver.find_element_by_id("maxCollectScope")
    maxCollectScope.clear()
    maxCollectScope.send_keys("9999")

    userId = driver.find_element_by_id("userId")
    userId.clear()
    userId.send_keys("aaaaabbbbbcccccddddd")

    passwd = driver.find_element_by_id("passwd")
    passwd.clear()
    passwd.send_keys("aaaaabbbbbcccccddddd")

    wavChannelMode = driver.find_element_by_id("wavChannelMode")
    mode = Select(wavChannelMode)
    mode.select_by_visible_text("ステレオ")

    vr500EditBtn = driver.find_element_by_id("vr500EditBtn")
    vr500EditBtn.click()

    #スクリーンショットを取得し保存

    sfile = driver.get_screenshot_as_file("%s/%s最大値設定.png"%(LogPath, FileName))

    #ページを更新
    driver.refresh()

####本来の設定###################################################################
    deviceName = driver.find_element_by_id("deviceName")
    deviceName.clear()
    deviceName.send_keys("タカコムVR")

    ipAddr = driver.find_element_by_id("ipAddr")
    ipAddr.clear()
    ipAddr.send_keys("%s"%(ip))

    anonymousFlag = driver.find_element_by_id("anonymousFlag")
    anonymousFlag.click()

    minPollingInterval = driver.find_element_by_id("minPollingInterval")
    minPollingInterval.clear()
    minPollingInterval.send_keys("1")

    maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
    maxElapsedTime.clear()
    maxElapsedTime.send_keys("10")

    maxCollectScope = driver.find_element_by_id("maxCollectScope")
    maxCollectScope.clear()
    maxCollectScope.send_keys("365")


    wavChannelMode = driver.find_element_by_id("wavChannelMode")
    mode = Select(wavChannelMode)
    mode.select_by_visible_text("ステレオ")

    vr500EditBtn = driver.find_element_by_id("vr500EditBtn")
    vr500EditBtn.click()

    sleep(5)

    #カレントページのURLを取得
    EditUrl = driver.current_url

    if FileName == "504bri":
        #回線設定画面のURLを取得
        LineUrl = EditUrl.replace("vr504/edit", "line/vr504")

        #回線設定画面に遷移
        driver.get(LineUrl)
        sfile = driver.get_screenshot_as_file("%s/%s回線設定画面.png"%(LogPath,FileName))
        addbtn = driver.find_element_by_id("add_btn")
        addbtn.click()
        sfile = driver.get_screenshot_as_file("%s/%s回線設定追加画面.png"%(LogPath,FileName))
        driver.refresh()
    else:
        #回線設定画面のURLを取得
        LineUrl = EditUrl.replace("vr508/edit", "line/vr508")

        #回線設定画面に遷移
        driver.get(LineUrl)
        sfile = driver.get_screenshot_as_file("%s/回線設定画面%s.png"%(LogPath,FileName))
        addbtn = driver.find_element_by_id("add_btn")
        addbtn.click()
        sfile = driver.get_screenshot_as_file("%s/回線設定追加画面%s.png"%(LogPath,FileName))
        driver.refresh()
    return 0
