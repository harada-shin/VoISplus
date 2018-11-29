from time import sleep

def getPlayWin(driver, LogPath):
    for num in range(1, 4):
        #検索結果一番上の音声ファイルを再生
        driver.find_element_by_xpath("//tr[1]/td[3]/a[2]/span").click()
        sleep(4)
        sfile = driver.get_screenshot_as_file("%s/波形表示（閉じる）_%s.png"%(LogPath, num))
        sleep(2)
        #閉じるボタンを押下
        driver.find_element_by_id("btnClose").click()
        sleep(2)


    for num in range(1, 4):
        #検索結果2番目の音声ファイルを再生
        driver.find_element_by_xpath("//tr[2]/td[3]/a[2]/span").click()
        sleep(4)
        sfile = driver.get_screenshot_as_file("%s/波形表示（×ボタン）_%s.png"%(LogPath, num))
        sleep(2)
        #右上の✖ボタン押下
        driver.find_element_by_xpath("//div[6]/div/div/div/button/span").click()
        sleep(2)
    return 0
