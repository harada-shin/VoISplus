from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep


def search(driver,LogPath,fileName):
    """
    検索ボタン押下する

    Parameters
    -----------------
    driver :
        ドライバー
    LogPath :
        ログを保存するディレクトリの場所
    fileName :
        保存するファイル名

    Returns
    -----------------
    なし
    """
    btnSearch = driver.find_element_by_id("btnSearch")
    btnSearch.click()

    sleep(2)
    #check_stars(driver)
    #sleep(2)
    #delete(driver)
    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/%s.png"%(LogPath, fileName))

    #ページを更新
    #driver.refresh()

    return 0

def set_Time(driver,StartDate,StartTime,EndDate,EndTime):
    """
    （検索するための）開始、終了日時を設定

    Parameters
    -----------------
    driver :
        ドライバー
    StartDate :
        開始日
    StartTime :
        開始時間
    EndDate :
        終了日
    EndTime :
        終了時間

    Returns
    -----------------
    なし
    """
    SDate = driver.find_element_by_id("startDate")
    SDate.clear()
    SDate.send_keys(StartDate,Keys.TAB)

    STime = driver.find_element_by_id("startTime")
    STime.clear()
    STime.send_keys(StartTime,Keys.TAB)


    EDate = driver.find_element_by_id("endDate")
    EDate.clear()
    EDate.send_keys(EndDate,Keys.TAB)

    ETime = driver.find_element_by_id("endTime")
    ETime.clear()
    ETime.send_keys(EndTime,Keys.TAB)

    return 0


'''通話時間を設定'''
def set_CallTime(driver,Time,unit,moreless):
    ctime = driver.find_element_by_id("calltime")
    ctime.clear()
    ctime.send_keys(Time)

    set_hms(driver,unit)
    set_moreless(driver,moreless)

    return 0

def set_hms(driver,unit):
    if unit == "h":
        hour = driver.find_element_by_id("calltimeHms")
        #セレクトタグの要素を指定してSelectクラスのインスタンスを作成
        selhms = Select(hour)
        #セレクトタグのオプションをテキストを指定して選択する
        selhms.select_by_visible_text("時")
    if unit == "m":
        min = driver.find_element_by_id("calltimeHms")
        #セレクトタグの要素を指定してSelectクラスのインスタンスを作成
        selhms = Select(min)
        #セレクトタグのオプションをテキストを指定して選択する
        selhms.select_by_visible_text("分")
    if unit == "s":
        sec = driver.find_element_by_id("calltimeHms")
        #セレクトタグの要素を指定してSelectクラスのインスタンスを作成
        selhms = Select(sec)
        #セレクトタグのオプションをテキストを指定して選択する
        selhms.select_by_visible_text("秒")

        return 0

def set_moreless(driver,value):
    if value == "more":
        ijyou = driver.find_element_by_id("calltimeMoreless")
        #セレクトタグの要素を指定してSelectクラスのインスタンスを作成
        selectmoreless = Select(ijyou)
        #セレクトタグのオプションをテキストを指定して選択する
        selectmoreless.select_by_visible_text("以上")
    if value == "less":
        miman = driver.find_element_by_id("calltimeMoreless")
        #セレクトタグの要素を指定してSelectクラスのインスタンスを作成
        selectmoreless = Select(miman)
        #セレクトタグのオプションをテキストを指定して選択する
        selectmoreless.select_by_visible_text("未満")

        return 0

'''番号、回線を設定'''
def set_header(driver,remoteNum,localNum,inout,extNum,agentID):
    aite = driver.find_element_by_id("tel1")
    aite.clear()
    aite.send_keys(remoteNum)

    zibun = driver.find_element_by_id("tel2")
    zibun.clear()
    zibun.send_keys(localNum)

    set_InOutCall(driver,inout)

    naisen = driver.find_element_by_id("extensionNo")
    naisen.clear()
    naisen.send_keys(extNum)

    kaisen = driver.find_element_by_id("lineName")
    kaisen.clear()
    kaisen.send_keys(agentID)

    return 0

'''発着信を設定'''
def set_InOutCall(driver,InOut):
    if InOut == "in":
        tyakusin = driver.find_element_by_id("callOrRecieve")
        #セレクトタグの要素を指定してSelectクラスのインスタンスを作成
        InCall = Select(tyakusin)
        #セレクトタグのオプションをテキストを指定して選択する
        InCall.select_by_visible_text("着信")
    if InOut == "out":
        hassin = driver.find_element_by_id("callOrRecieve")
        #セレクトタグの要素を指定してSelectクラスのインスタンスを作成
        OutCall = Select(hassin)
        #セレクトタグのオプションをテキストを指定して選択する
        OutCall.select_by_visible_text("発信")

        return 0

def set_mark(driver, cnt):
    if cnt == "0":
        Select(driver.find_element_by_id("mark")).select_by_visible_text("マークなし")

    if cnt == "1":
        Select(driver.find_element_by_id("mark")).select_by_visible_text("マーク済み")

def check_stars(driver, Num):
    driver.find_element_by_xpath("//tr[%s]/td[3]/a/span"%(Num)).click()
    return 0

def delete(driver):
    delIcon = driver.find_element_by_class_name("delete_erase_btn")
    delIcon.click()
    return 0
