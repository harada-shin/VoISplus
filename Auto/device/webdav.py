from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

def setting_new_all(driver, URL, Device_URL, LogPath):
        for x in range(1,9):
            driver.get(URL)

            deviceName = driver.find_element_by_id("deviceName")
            deviceName.send_keys("通話録音グループ%s個_新規登録"%(x))

            for num in range(int("%s"%(x))):
                user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
                user1.send_keys("docomo%s"%(num))

                pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
                pwd1.send_keys("docomo%s"%(num))

            minPollingInterval = driver.find_element_by_id("minPollingInterval")
            minPollingInterval.send_keys("1")

            maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
            maxElapsedTime.send_keys("1")

            sendbtn = driver.find_element_by_id("sendbtn")
            sendbtn.click()

            #スクリーンショットを取得し保存
            sfile = driver.get_screenshot_as_file("%s/webdav_新規登録%s個.png"%(LogPath, x))



    ####同じ名前の機器名称追加
        for cnt in range(2):
            driver.get(URL)
            deviceName = driver.find_element_by_id("deviceName")
            deviceName.clear()
            deviceName.send_keys("同じ名前の機器名称追加")
            for num in range(0,8):
                user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
                user1.send_keys("docomo%s"%(num))

                pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
                pwd1.send_keys("docomo")

            minPollingInterval = driver.find_element_by_id("minPollingInterval")
            minPollingInterval.send_keys("1")

            maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
            maxElapsedTime.send_keys("1")

            sendbtn = driver.find_element_by_id("sendbtn")
            sendbtn.click()

        driver.get(Device_URL)

        sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/同じ名前の機器名称追加.png"%LogPath)

    ####同じ名前の契約グループID追加
        driver.get(URL)

        deviceName = driver.find_element_by_id("deviceName")
        deviceName.clear()
        deviceName.send_keys("同じ名前の契約グループID追加")

        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.send_keys("docomo")

            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.send_keys("docomo")

        minPollingInterval = driver.find_element_by_id("minPollingInterval")
        minPollingInterval.send_keys("1")

        maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
        maxElapsedTime.send_keys("1")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/同じ名前の契約グループID追加.png"%LogPath)



    ####全ての契約グループIDとZIPパスワードなし(Chrome)
        driver.get(URL)

        deviceName = driver.find_element_by_id("deviceName")
        deviceName.send_keys("全て同じ契約グループIDとZIPパスワードなし")

        minPollingInterval = driver.find_element_by_id("minPollingInterval")
        minPollingInterval.send_keys("1")

        maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
        maxElapsedTime.send_keys("1")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/全ての契約グループIDとZIPパスワードなし.png"%(LogPath))

    ####契約グループIDなし、ZIPパスワードあり(Chrome)
        driver.get(URL)

        deviceName = driver.find_element_by_id("deviceName")
        deviceName.send_keys("契約グループIDなし、ZIPパスワードあり")
        for num in range(0,8):
            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.send_keys("docomo")

        minPollingInterval = driver.find_element_by_id("minPollingInterval")
        minPollingInterval.send_keys("1")

        maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
        maxElapsedTime.send_keys("1")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/契約グループIDなし、ZIPパスワードあり.png"%(LogPath))

    ####契約グループIDあり、ZIPパスワードなし(Chrome)
        driver.get(URL)

        deviceName = driver.find_element_by_id("deviceName")
        deviceName.send_keys("契約グループIDあり、ZIPパスワードなし")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.send_keys("docomo%s"%(num))

        minPollingInterval = driver.find_element_by_id("minPollingInterval")
        minPollingInterval.send_keys("1")

        maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
        maxElapsedTime.send_keys("1")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/契約グループIDあり、ZIPパスワードなし.png"%(LogPath))

    ####契約グループIDに半角英字(小文字)
        driver.get(URL)

        deviceName = driver.find_element_by_id("deviceName")
        deviceName.send_keys("契約グループIDに半角英字(小文字)")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.send_keys("docomo%s"%(num))

        minPollingInterval = driver.find_element_by_id("minPollingInterval")
        minPollingInterval.send_keys("1")

        maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
        maxElapsedTime.send_keys("1")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/契約グループIDに半角英字(小文字).png"%(LogPath))

    ####契約グループIDに半角英字(大文字)
        driver.get(URL)

        deviceName = driver.find_element_by_id("deviceName")
        deviceName.send_keys("契約グループIDに半角英字(大文字)")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.send_keys("DOCOMO%s"%(num))

        minPollingInterval = driver.find_element_by_id("minPollingInterval")
        minPollingInterval.send_keys("1")

        maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
        maxElapsedTime.send_keys("1")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/契約グループIDに半角英字(大文字).png"%(LogPath))

    ####契約グループIDに全角文字(大文字)
        driver.get(URL)

        deviceName = driver.find_element_by_id("deviceName")
        deviceName.send_keys("契約グループIDに全角文字")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.send_keys("携帯どこもドコモ%s"%(num))

        minPollingInterval = driver.find_element_by_id("minPollingInterval")
        minPollingInterval.send_keys("1")

        maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
        maxElapsedTime.send_keys("1")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/契約グループIDに全角文字.png"%(LogPath))

    ####契約グループIDに"-"と"_"以外の記号
        driver.get(URL)

        deviceName = driver.find_element_by_id("deviceName")
        deviceName.send_keys("契約グループIDに-と_以外の記号")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.send_keys("~!@#$%^&*()=\][';/.,']+|}{''?><}")

        minPollingInterval = driver.find_element_by_id("minPollingInterval")
        minPollingInterval.send_keys("1")

        maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
        maxElapsedTime.send_keys("1")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/契約グループIDに-と_以外の記号.png"%(LogPath))

    ####ZIPパスワードに半角文字(Chrome)
        driver.get(URL)

        deviceName = driver.find_element_by_id("deviceName")
        deviceName.send_keys("ZIPパスワードに半角文字")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.send_keys("docomo%s"%(num))

            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.send_keys("phonedocomo")

        minPollingInterval = driver.find_element_by_id("minPollingInterval")
        minPollingInterval.send_keys("1")

        maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
        maxElapsedTime.send_keys("1")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/ZIPパスワードに半角文字.png"%(LogPath))

    ####ZIPパスワードに全角文字(Chrome)
        driver.get(URL)

        deviceName = driver.find_element_by_id("deviceName")
        deviceName.send_keys("ZIPパスワードに全角文字")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.send_keys("docomo%s"%(num))

            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.send_keys("携帯どこもドコモ")

        minPollingInterval = driver.find_element_by_id("minPollingInterval")
        minPollingInterval.send_keys("1")

        maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
        maxElapsedTime.send_keys("1")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/ZIPパスワードに全角文字.png"%(LogPath))

        sleep(2)
        driver.get(Device_URL)

        return 0

def setting_change(driver, URL, Device_URL, LogPath):

        driver.get(URL)

        for num in range(8):

            deviceName = driver.find_element_by_id("deviceName")
            deviceName.clear()
            deviceName.send_keys("【変更】通話録音グループ%s個"%(num))

            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.send_keys("docomo%s"%(num))

            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.send_keys("docomo%s"%(num))

            minPollingInterval = driver.find_element_by_id("minPollingInterval")
            minPollingInterval.clear()
            minPollingInterval.send_keys("1")

            maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
            maxElapsedTime.clear()
            maxElapsedTime.send_keys("1")

            sendbtn = driver.find_element_by_id("sendbtn")
            sendbtn.click()

            #スクリーンショットを取得し保存
            sfile = driver.get_screenshot_as_file("%s/【変更】webdav_change_%s.png"%(LogPath, num))

            #sendbtn = driver.find_element_by_id("sendbtn")
            #sendbtn.click()

            #ページを更新
            driver.refresh()

    ####同じ名前の契約グループID追加
        deviceName = driver.find_element_by_id("deviceName")
        deviceName.clear()
        deviceName.send_keys("【変更】同じ名前の契約グループID追加")

        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.clear()
            user1.send_keys("docomo")

            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.clear()
            pwd1.send_keys("docomo")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/【変更】同じ名前の契約グループID追加.png"%LogPath)



    ####全ての契約グループIDとZIPパスワードなし(Chrome)
        deviceName = driver.find_element_by_id("deviceName")
        deviceName.clear()
        deviceName.send_keys("【変更】全て同じ契約グループIDとZIPパスワードなし")

        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.clear()

            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.clear()

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/【変更】全ての契約グループIDとZIPパスワードなし.png"%(LogPath))

    ####契約グループIDなし、ZIPパスワードあり(Chrome)
        deviceName = driver.find_element_by_id("deviceName")
        deviceName.clear()
        deviceName.send_keys("【変更】契約グループIDなし、ZIPパスワードあり")
        for num in range(0,8):
            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.send_keys("docomo")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/【変更】契約グループIDなし、ZIPパスワードあり.png"%(LogPath))

    ####契約グループIDあり、ZIPパスワードなし(Chrome)
        deviceName = driver.find_element_by_id("deviceName")
        deviceName.clear()
        deviceName.send_keys("【変更】契約グループIDあり、ZIPパスワードなし")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.send_keys("docomo%s"%(num))

            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.clear()

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/【変更】契約グループIDあり、ZIPパスワードなし.png"%(LogPath))

    ####契約グループIDに半角英字(小文字)
        deviceName = driver.find_element_by_id("deviceName")
        deviceName.clear()
        deviceName.send_keys("【変更】契約グループIDに半角英字(小文字)")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.clear()
            user1.send_keys("docomo%s"%(num))

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/【変更】契約グループIDに半角英字(小文字).png"%(LogPath))

    ####契約グループIDに半角英字(大文字)
        deviceName = driver.find_element_by_id("deviceName")
        deviceName.clear()
        deviceName.send_keys("【変更】契約グループIDに半角英字(大文字)")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.clear()
            user1.send_keys("DOCOMO%s"%(num))

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/【変更】契約グループIDに半角英字(大文字).png"%(LogPath))

    ####契約グループIDに全角文字(大文字)
        deviceName = driver.find_element_by_id("deviceName")
        deviceName.clear()
        deviceName.send_keys("【変更】契約グループIDに全角文字")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.clear()
            user1.send_keys("携帯どこもドコモ%s"%(num))

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/【変更】契約グループIDに全角文字.png"%(LogPath))

    ####契約グループIDに"-"と"_"以外の記号
        deviceName = driver.find_element_by_id("deviceName")
        deviceName.clear()
        deviceName.send_keys("【変更】契約グループIDに-と_以外の記号")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.clear()
            user1.send_keys("~!@#$%^&*()=\][';/.,']+|}{''?><}")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/【変更】契約グループIDに-と_以外の記号.png"%(LogPath))

    ####ZIPパスワードに半角文字(Chrome)
        deviceName = driver.find_element_by_id("deviceName")
        deviceName.clear()
        deviceName.send_keys("【変更】ZIPパスワードに半角文字")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.clear()
            user1.send_keys("docomo%s"%(num))

            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.clear()
            pwd1.send_keys("phonedocomo")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/【変更】ZIPパスワードに半角文字.png"%(LogPath))

    ####ZIPパスワードに全角文字(Chrome)
        deviceName = driver.find_element_by_id("deviceName")
        deviceName.clear()
        deviceName.send_keys("【変更】ZIPパスワードに全角文字")
        for num in range(0,8):
            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.clear()
            pwd1.send_keys("携帯どこもドコモ")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/【変更】ZIPパスワードに全角文字.png"%(LogPath))

    ####同じ名前の機器名称追加
        deviceName = driver.find_element_by_id("deviceName")
        deviceName.clear()
        deviceName.send_keys("同じ名前の機器名称追加")
        for num in range(0,8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.clear()
            user1.send_keys("docomo%s"%(num))

            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.clear()
            pwd1.send_keys("docomo")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        driver.get(Device_URL)

        sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        sleep(1)

        #スクリーンショットを取得し保存
        sfile = driver.get_screenshot_as_file("%s/【変更】同じ名前の機器名称追加.png"%LogPath)


        return 0

'''今後きれいに書くようの関数'''
def NewRegistar(driver, Name, user, pwd):
    driver.get(URL)

    deviceName = driver.find_element_by_id("deviceName")
    deviceName.send_keys(Name)
    for num in range(0,8):
        user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
        user1.send_keys("docomo%s"%(num))

        pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
        pwd1.send_keys(pwd)

    minPollingInterval = driver.find_element_by_id("minPollingInterval")
    minPollingInterval.send_keys("1")

    maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
    maxElapsedTime.send_keys("1")

    sendbtn = driver.find_element_by_id("sendbtn")
    sendbtn.click()

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/%s.png"%(LogPath,Name))

    return 0


def move_Line(driver,URL):
        driver.get(URL)

        deviceName = driver.find_element_by_id("deviceName")
        deviceName.send_keys("docomo回線設定用")

        for num in range(8):
            user1 = driver.find_element_by_id("docomoInfoList%s.confirmUrlCd"%(num))
            user1.send_keys("docomo%s"%(num))
            pwd1 = driver.find_element_by_id("docomoInfoList%s.zipPasswd"%(num))
            pwd1.send_keys("docomo%s"%(num))

        minPollingInterval = driver.find_element_by_id("minPollingInterval")
        minPollingInterval.send_keys("1")

        maxElapsedTime = driver.find_element_by_id("maxElapsedTime")
        maxElapsedTime.send_keys("1")

        sendbtn = driver.find_element_by_id("sendbtn")
        sendbtn.click()

        #webdavの回線設定
        EditUrl = driver.current_url
        LineUrl = EditUrl.replace("docomo/edit", "line/docomo")
        driver.get(LineUrl)

        return 0
