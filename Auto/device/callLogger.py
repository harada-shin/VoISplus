from time import sleep

def setting(driver, URL, IP, LogPath ,smb_Path, DB_url):
    #CallLogger 設定変更画面に遷移
    driver.get(URL)

    sendbtn = driver.find_element_by_id("sendbtn")
    sendbtn.click()

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/CallLogger全設定未入力.png"%(LogPath))


    deviceName = driver.find_element_by_id("deviceName")
    deviceName.send_keys("CallLogger")

    ipAddr = driver.find_element_by_id("ipAddr")
    ipAddr.send_keys("%s"%(IP))

    minPollingInterval = driver.find_element_by_id("minPollingInterval")
    minPollingInterval.send_keys("1")

    maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
    maxElapsedTime.send_keys("10")

    #ファイル共有サービス
    smbDirectory = driver.find_element_by_id("smbDirectory")
    smbDirectory.send_keys(smb_Path)

    smbUser = driver.find_element_by_id("smbUser")
    smbUser.send_keys("administrator")

    smbPasswd = driver.find_element_by_id("smbPasswd")
    smbPasswd.send_keys("admin")

    #接続テストボタン押下
    smbConnectTest = driver.find_element_by_id("connect-test-smb")
    smbConnectTest.click()

    sleep(5)

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/CallLoggerファイル共有接続確認.png"%(LogPath))


    #DB接続
    smbDirectory = driver.find_element_by_id("jdbcUrl")
    smbDirectory.send_keys(DB_url)

    smbUser = driver.find_element_by_id("dbUser")
    smbUser.send_keys("TEAC")

    smbPasswd = driver.find_element_by_id("dbPasswd")
    smbPasswd.send_keys("#lasystem!")

    #接続テストボタン押下
    jdbcConnectTest = driver.find_element_by_id("connect-test-jdbc")
    jdbcConnectTest.click()

    sleep(10)

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/CallLoggerDB接続確認.png"%(LogPath))

    sendbtn = driver.find_element_by_id("sendbtn")
    sendbtn.click()

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/CallLogger登録完了.png"%(LogPath))


    return 0
