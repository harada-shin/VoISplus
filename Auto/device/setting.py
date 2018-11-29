from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient
import shutil

def max(driver, LogPath, URL):

    driver.get(URL)
    ####ログイン
    #ログイン―パスワード有効期限　入力
    passwordExpired = driver.find_element_by_id("passwordExpired")
    passwordExpired.clear()
    passwordExpired.send_keys("9999")

    #連続失敗チェック範囲　入力
    loginLockCheckRange = driver.find_element_by_id("loginLockCheckRange")
    loginLockCheckRange.clear()
    loginLockCheckRange.send_keys("9999")

    #連続失敗しきい値　入力
    loginLockFailCount = driver.find_element_by_id("loginLockFailCount")
    loginLockFailCount.clear()
    loginLockFailCount.send_keys("9999")

    #ログイン―パスワード有効期限　入力
    loginLockCheckRange = driver.find_element_by_id("loginLockCheckRange")
    loginLockCheckRange.clear()
    loginLockCheckRange.send_keys("9999")

    #ログインロック時間　入力
    loginLockTime = driver.find_element_by_id("loginLockTime")
    loginLockTime.clear()
    loginLockTime.send_keys("9999")

    ####収集スレッド
    #スレッド数
    threadCount = driver.find_element_by_id("threadCount")
    threadCount.clear()
    threadCount.send_keys("10")

    #実行時最低空き容量
    threadMinCapacity = driver.find_element_by_id("threadMinCapacity")
    threadMinCapacity.clear()
    threadMinCapacity.send_keys("99999")

    ####通話データ検索
    #最大検索可能範囲
    phoneCallMaxSearchRange = driver.find_element_by_id("phoneCallMaxSearchRange")
    phoneCallMaxSearchRange.clear()
    phoneCallMaxSearchRange.send_keys("3650")

    ##音声データ保持期間
    #データベース
    voiceKeepPeriodDb = driver.find_element_by_id("voiceKeepPeriodDb")
    voiceKeepPeriodDb.clear()
    voiceKeepPeriodDb.send_keys("9999")

    #音声ファイル
    voiceKeepPeriodFile = driver.find_element_by_id("voiceKeepPeriodFile")
    voiceKeepPeriodFile.clear()
    voiceKeepPeriodFile.send_keys("9999")


    ##履歴保持期間
    #ログイン履歴
    historyKeepPeriodLogin = driver.find_element_by_id("historyKeepPeriodLogin")
    historyKeepPeriodLogin.clear()
    historyKeepPeriodLogin.send_keys("9999")

    #音声操作履歴
    historyKeepPeriodVoice = driver.find_element_by_id("historyKeepPeriodVoice")
    historyKeepPeriodVoice.clear()
    historyKeepPeriodVoice.send_keys("9999")

    #アラーム履歴
    historyKeepPeriodAlarm = driver.find_element_by_id("historyKeepPeriodAlarm")
    historyKeepPeriodAlarm.clear()
    historyKeepPeriodAlarm.send_keys("9999")

    #バックアップ履歴
    historyKeepPeriodBackup = driver.find_element_by_id("historyKeepPeriodBackup")
    historyKeepPeriodBackup.clear()
    historyKeepPeriodBackup.send_keys("9999")

    #音声ファイル収集履歴
    historyKeepPeriodCollection = driver.find_element_by_id("historyKeepPeriodCollection")
    historyKeepPeriodCollection.clear()
    historyKeepPeriodCollection.send_keys("9999")

    ####バックアップ
    #実行時刻
    backupTime = driver.find_element_by_id("backupTime")
    backupTime.clear()
    backupTime.send_keys("23:59")
    backupTime.send_keys(Keys.TAB)

    #曜日にチェック
    backupSun = driver.find_element_by_id("backupSun")
    backupSun.click()
    backupMon = driver.find_element_by_id("backupMon")
    backupMon.click()
    backupTue = driver.find_element_by_id("backupTue")
    backupTue.click()
    backupWed = driver.find_element_by_id("backupWed")
    backupWed.click()
    backupThu = driver.find_element_by_id("backupThu")
    backupThu.click()
    backupFri = driver.find_element_by_id("backupFri")
    backupFri.click()
    backupSat = driver.find_element_by_id("backupSat")
    backupSat.click()


    #実行時最低空き容量
    backupCapacity = driver.find_element_by_id("backupCapacity")
    backupCapacity.clear()
    backupCapacity.send_keys("9999")


    #変更ボタン押下
    elem_search_editbtn = driver.find_element_by_id("editBtn")
    elem_search_editbtn.click()

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/本体設定_最大値.png"%(LogPath))

    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)

    return 0

def min(driver, LogPath, URL):

    #本体設定変更画面に遷移
    driver.get(URL)

    ####ログイン
    #ログイン―パスワード有効期限　入力
    passwordExpired = driver.find_element_by_id("passwordExpired")
    passwordExpired.clear()
    passwordExpired.send_keys("1")

    #連続失敗チェック範囲　入力
    loginLockCheckRange = driver.find_element_by_id("loginLockCheckRange")
    loginLockCheckRange.clear()
    loginLockCheckRange.send_keys("1")

    #連続失敗しきい値　入力
    loginLockFailCount = driver.find_element_by_id("loginLockFailCount")
    loginLockFailCount.clear()
    loginLockFailCount.send_keys("1")

    #ログイン―パスワード有効期限　入力
    loginLockCheckRange = driver.find_element_by_id("loginLockCheckRange")
    loginLockCheckRange.clear()
    loginLockCheckRange.send_keys("1")

    #ログインロック時間　入力
    loginLockTime = driver.find_element_by_id("loginLockTime")
    loginLockTime.clear()
    loginLockTime.send_keys("1")

    ####収集スレッド
    #スレッド数
    threadCount = driver.find_element_by_id("threadCount")
    threadCount.clear()
    threadCount.send_keys("1")

    #実行時最低空き容量
    threadMinCapacity = driver.find_element_by_id("threadMinCapacity")
    threadMinCapacity.clear()
    threadMinCapacity.send_keys("1")

    ####通話データ検索
    #最大検索可能範囲
    phoneCallMaxSearchRange = driver.find_element_by_id("phoneCallMaxSearchRange")
    phoneCallMaxSearchRange.clear()
    phoneCallMaxSearchRange.send_keys("1")

    ##音声データ保持期間
    #データベース
    voiceKeepPeriodDb = driver.find_element_by_id("voiceKeepPeriodDb")
    voiceKeepPeriodDb.clear()
    voiceKeepPeriodDb.send_keys("1")

    #音声ファイル
    voiceKeepPeriodFile = driver.find_element_by_id("voiceKeepPeriodFile")
    voiceKeepPeriodFile.clear()
    voiceKeepPeriodFile.send_keys("1")


    ##履歴保持期間
    #ログイン履歴
    historyKeepPeriodLogin = driver.find_element_by_id("historyKeepPeriodLogin")
    historyKeepPeriodLogin.clear()
    historyKeepPeriodLogin.send_keys("1")

    #音声操作履歴
    historyKeepPeriodVoice = driver.find_element_by_id("historyKeepPeriodVoice")
    historyKeepPeriodVoice.clear()
    historyKeepPeriodVoice.send_keys("1")

    #アラーム履歴
    historyKeepPeriodAlarm = driver.find_element_by_id("historyKeepPeriodAlarm")
    historyKeepPeriodAlarm.clear()
    historyKeepPeriodAlarm.send_keys("1")

    #バックアップ履歴
    historyKeepPeriodBackup = driver.find_element_by_id("historyKeepPeriodBackup")
    historyKeepPeriodBackup.clear()
    historyKeepPeriodBackup.send_keys("1")

    #音声ファイル収集履歴
    historyKeepPeriodCollection = driver.find_element_by_id("historyKeepPeriodCollection")
    historyKeepPeriodCollection.clear()
    historyKeepPeriodCollection.send_keys("1")

    ####バックアップ
    #実行時刻
    backupTime = driver.find_element_by_id("backupTime")
    backupTime.clear()
    backupTime.send_keys("0")

    #実行時最低空き容量
    backupCapacity = driver.find_element_by_id("backupCapacity")
    backupCapacity.clear()
    backupCapacity.send_keys("1")


    #変更ボタン押下
    elem_search_editbtn = driver.find_element_by_id("editBtn")
    elem_search_editbtn.click()

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/本体設定_最小値.png"%(LogPath))

    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)

    return 0

def over(driver, LogPath, URL):

    driver.get(URL)
    ####ログイン
    #ログイン―パスワード有効期限　入力
    passwordExpired = driver.find_element_by_id("passwordExpired")
    passwordExpired.clear()
    passwordExpired.send_keys("10000")

    #連続失敗チェック範囲　入力
    loginLockCheckRange = driver.find_element_by_id("loginLockCheckRange")
    loginLockCheckRange.clear()
    loginLockCheckRange.send_keys("10000")

    #連続失敗しきい値　入力
    loginLockFailCount = driver.find_element_by_id("loginLockFailCount")
    loginLockFailCount.clear()
    loginLockFailCount.send_keys("10000")

    #ログイン―パスワード有効期限　入力
    loginLockCheckRange = driver.find_element_by_id("loginLockCheckRange")
    loginLockCheckRange.clear()
    loginLockCheckRange.send_keys("10000")

    #ログインロック時間　入力
    loginLockTime = driver.find_element_by_id("loginLockTime")
    loginLockTime.clear()
    loginLockTime.send_keys("10000")

    ####収集スレッド
    #スレッド数
    threadCount = driver.find_element_by_id("threadCount")
    threadCount.clear()
    threadCount.send_keys("11")

    #実行時最低空き容量
    threadMinCapacity = driver.find_element_by_id("threadMinCapacity")
    threadMinCapacity.clear()
    threadMinCapacity.send_keys("100000")

    ####通話データ検索
    #最大検索可能範囲
    phoneCallMaxSearchRange = driver.find_element_by_id("phoneCallMaxSearchRange")
    phoneCallMaxSearchRange.clear()
    phoneCallMaxSearchRange.send_keys("3651")

    ##音声データ保持期間
    #データベース
    voiceKeepPeriodDb = driver.find_element_by_id("voiceKeepPeriodDb")
    voiceKeepPeriodDb.clear()
    voiceKeepPeriodDb.send_keys("10000")

    #音声ファイル
    voiceKeepPeriodFile = driver.find_element_by_id("voiceKeepPeriodFile")
    voiceKeepPeriodFile.clear()
    voiceKeepPeriodFile.send_keys("10000")


    ##履歴保持期間
    #ログイン履歴
    historyKeepPeriodLogin = driver.find_element_by_id("historyKeepPeriodLogin")
    historyKeepPeriodLogin.clear()
    historyKeepPeriodLogin.send_keys("10000")

    #音声操作履歴
    historyKeepPeriodVoice = driver.find_element_by_id("historyKeepPeriodVoice")
    historyKeepPeriodVoice.clear()
    historyKeepPeriodVoice.send_keys("10000")

    #アラーム履歴
    historyKeepPeriodAlarm = driver.find_element_by_id("historyKeepPeriodAlarm")
    historyKeepPeriodAlarm.clear()
    historyKeepPeriodAlarm.send_keys("10000")

    #バックアップ履歴
    historyKeepPeriodBackup = driver.find_element_by_id("historyKeepPeriodBackup")
    historyKeepPeriodBackup.clear()
    historyKeepPeriodBackup.send_keys("10000")

    #音声ファイル収集履歴
    historyKeepPeriodCollection = driver.find_element_by_id("historyKeepPeriodCollection")
    historyKeepPeriodCollection.clear()
    historyKeepPeriodCollection.send_keys("10000")

    ####バックアップ
    #実行時刻
    backupTime = driver.find_element_by_id("backupTime")
    backupTime.clear()
    backupTime.send_keys("23:59")
    backupTime.send_keys(Keys.TAB)

    #曜日にチェック
    backupSun = driver.find_element_by_id("backupSun")
    backupSun.click()
    backupMon = driver.find_element_by_id("backupMon")
    backupMon.click()
    backupTue = driver.find_element_by_id("backupTue")
    backupTue.click()
    backupWed = driver.find_element_by_id("backupWed")
    backupWed.click()
    backupThu = driver.find_element_by_id("backupThu")
    backupThu.click()
    backupFri = driver.find_element_by_id("backupFri")
    backupFri.click()
    backupSat = driver.find_element_by_id("backupSat")
    backupSat.click()


    #実行時最低空き容量
    backupCapacity = driver.find_element_by_id("backupCapacity")
    backupCapacity.clear()
    backupCapacity.send_keys("10000")


    #変更ボタン押下
    elem_search_editbtn = driver.find_element_by_id("editBtn")
    elem_search_editbtn.click()

    driver.execute_script("document.body.style.zoom='90%'")

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/本体設定over.png"%(LogPath))

    driver.execute_script("document.body.style.zoom='100%'")

    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)

    return 0

def under(driver, LogPath, URL):

    driver.get(URL)
    ####ログイン
    #ログイン―パスワード有効期限　入力
    passwordExpired = driver.find_element_by_id("passwordExpired")
    passwordExpired.clear()
    passwordExpired.send_keys("0")

    #連続失敗チェック範囲　入力
    loginLockCheckRange = driver.find_element_by_id("loginLockCheckRange")
    loginLockCheckRange.clear()
    loginLockCheckRange.send_keys("0")

    #連続失敗しきい値　入力
    loginLockFailCount = driver.find_element_by_id("loginLockFailCount")
    loginLockFailCount.clear()
    loginLockFailCount.send_keys("0")

    #ログイン―パスワード有効期限　入力
    loginLockCheckRange = driver.find_element_by_id("loginLockCheckRange")
    loginLockCheckRange.clear()
    loginLockCheckRange.send_keys("0")

    #ログインロック時間　入力
    loginLockTime = driver.find_element_by_id("loginLockTime")
    loginLockTime.clear()
    loginLockTime.send_keys("0")

    ####収集スレッド
    #スレッド数
    threadCount = driver.find_element_by_id("threadCount")
    threadCount.clear()
    threadCount.send_keys("0")

    #実行時最低空き容量
    threadMinCapacity = driver.find_element_by_id("threadMinCapacity")
    threadMinCapacity.clear()
    threadMinCapacity.send_keys("0")

    ####通話データ検索
    #最大検索可能範囲
    phoneCallMaxSearchRange = driver.find_element_by_id("phoneCallMaxSearchRange")
    phoneCallMaxSearchRange.clear()
    phoneCallMaxSearchRange.send_keys("0")

    ##音声データ保持期間
    #データベース
    voiceKeepPeriodDb = driver.find_element_by_id("voiceKeepPeriodDb")
    voiceKeepPeriodDb.clear()
    voiceKeepPeriodDb.send_keys("0")

    #音声ファイル
    voiceKeepPeriodFile = driver.find_element_by_id("voiceKeepPeriodFile")
    voiceKeepPeriodFile.clear()
    voiceKeepPeriodFile.send_keys("0")


    ##履歴保持期間
    #ログイン履歴
    historyKeepPeriodLogin = driver.find_element_by_id("historyKeepPeriodLogin")
    historyKeepPeriodLogin.clear()
    historyKeepPeriodLogin.send_keys("0")

    #音声操作履歴
    historyKeepPeriodVoice = driver.find_element_by_id("historyKeepPeriodVoice")
    historyKeepPeriodVoice.clear()
    historyKeepPeriodVoice.send_keys("0")

    #アラーム履歴
    historyKeepPeriodAlarm = driver.find_element_by_id("historyKeepPeriodAlarm")
    historyKeepPeriodAlarm.clear()
    historyKeepPeriodAlarm.send_keys("0")

    #バックアップ履歴
    historyKeepPeriodBackup = driver.find_element_by_id("historyKeepPeriodBackup")
    historyKeepPeriodBackup.clear()
    historyKeepPeriodBackup.send_keys("0")

    #音声ファイル収集履歴
    historyKeepPeriodCollection = driver.find_element_by_id("historyKeepPeriodCollection")
    historyKeepPeriodCollection.clear()
    historyKeepPeriodCollection.send_keys("0")

    ####バックアップ
    #実行時刻
    backupTime = driver.find_element_by_id("backupTime")
    backupTime.clear()
    backupTime.send_keys("23:59")
    backupTime.send_keys(Keys.TAB)

    #曜日にチェック
    backupSun = driver.find_element_by_id("backupSun")
    backupSun.click()
    backupMon = driver.find_element_by_id("backupMon")
    backupMon.click()
    backupTue = driver.find_element_by_id("backupTue")
    backupTue.click()
    backupWed = driver.find_element_by_id("backupWed")
    backupWed.click()
    backupThu = driver.find_element_by_id("backupThu")
    backupThu.click()
    backupFri = driver.find_element_by_id("backupFri")
    backupFri.click()
    backupSat = driver.find_element_by_id("backupSat")
    backupSat.click()


    #実行時最低空き容量
    backupCapacity = driver.find_element_by_id("backupCapacity")
    backupCapacity.clear()
    backupCapacity.send_keys("0")


    #変更ボタン押下
    elem_search_editbtn = driver.find_element_by_id("editBtn")
    elem_search_editbtn.click()

    driver.execute_script("document.body.style.zoom='90%'")

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/本体装置設定under.png"%(LogPath))

    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)

    driver.execute_script("document.body.style.zoom='100%'")

    return 0

def DecimalPoint(driver, LogPath, URL):

    driver.get(URL)
    ####ログイン
    #ログイン―パスワード有効期限　入力
    passwordExpired = driver.find_element_by_id("passwordExpired")
    passwordExpired.clear()
    passwordExpired.send_keys("1.0")
    sleep(1)

    #連続失敗チェック範囲　入力
    loginLockCheckRange = driver.find_element_by_id("loginLockCheckRange")
    loginLockCheckRange.clear()
    loginLockCheckRange.send_keys("1.0")
    sleep(1)

    #連続失敗しきい値　入力
    loginLockFailCount = driver.find_element_by_id("loginLockFailCount")
    loginLockFailCount.clear()
    loginLockFailCount.send_keys("1.0")
    sleep(1)

    #ログインロック時間　入力
    loginLockTime = driver.find_element_by_id("loginLockTime")
    loginLockTime.clear()
    loginLockTime.send_keys("1.0")
    sleep(1)

    ####収集スレッド
    #スレッド数
    threadCount = driver.find_element_by_id("threadCount")
    threadCount.clear()
    threadCount.send_keys("1.0")
    sleep(1)

    #実行時最低空き容量
    threadMinCapacity = driver.find_element_by_id("threadMinCapacity")
    threadMinCapacity.clear()
    threadMinCapacity.send_keys("1.0")
    sleep(1)

    ####通話データ検索
    #最大検索可能範囲
    phoneCallMaxSearchRange = driver.find_element_by_id("phoneCallMaxSearchRange")
    phoneCallMaxSearchRange.clear()
    phoneCallMaxSearchRange.send_keys("1.0")
    sleep(1)

    ##音声データ保持期間
    #データベース
    voiceKeepPeriodDb = driver.find_element_by_id("voiceKeepPeriodDb")
    voiceKeepPeriodDb.clear()
    voiceKeepPeriodDb.send_keys("1.0")
    sleep(1)

    #音声ファイル
    voiceKeepPeriodFile = driver.find_element_by_id("voiceKeepPeriodFile")
    voiceKeepPeriodFile.clear()
    voiceKeepPeriodFile.send_keys("1.0")
    sleep(1)


    ##履歴保持期間
    #ログイン履歴
    historyKeepPeriodLogin = driver.find_element_by_id("historyKeepPeriodLogin")
    historyKeepPeriodLogin.clear()
    historyKeepPeriodLogin.send_keys("1.0")
    sleep(1)

    #音声操作履歴
    historyKeepPeriodVoice = driver.find_element_by_id("historyKeepPeriodVoice")
    historyKeepPeriodVoice.clear()
    historyKeepPeriodVoice.send_keys("1.0")
    sleep(1)

    #アラーム履歴
    historyKeepPeriodAlarm = driver.find_element_by_id("historyKeepPeriodAlarm")
    historyKeepPeriodAlarm.clear()
    historyKeepPeriodAlarm.send_keys("1.0")
    sleep(1)

    #バックアップ履歴
    historyKeepPeriodBackup = driver.find_element_by_id("historyKeepPeriodBackup")
    historyKeepPeriodBackup.clear()
    historyKeepPeriodBackup.send_keys("1.0")
    sleep(1)

    #音声ファイル収集履歴
    historyKeepPeriodCollection = driver.find_element_by_id("historyKeepPeriodCollection")
    historyKeepPeriodCollection.clear()
    historyKeepPeriodCollection.send_keys("1.0")
    sleep(1)

    ####バックアップ
    #実行時刻
    backupTime = driver.find_element_by_id("backupTime")
    backupTime.clear()
    backupTime.send_keys("23:59")
    backupTime.send_keys(Keys.TAB)
    sleep(1)

    #曜日にチェック
    backupSun = driver.find_element_by_id("backupSun")
    backupSun.click()
    backupMon = driver.find_element_by_id("backupMon")
    backupMon.click()
    backupTue = driver.find_element_by_id("backupTue")
    backupTue.click()
    backupWed = driver.find_element_by_id("backupWed")
    backupWed.click()
    backupThu = driver.find_element_by_id("backupThu")
    backupThu.click()
    backupFri = driver.find_element_by_id("backupFri")
    backupFri.click()
    backupSat = driver.find_element_by_id("backupSat")
    backupSat.click()
    sleep(1)

    #実行時最低空き容量
    backupCapacity = driver.find_element_by_id("backupCapacity")
    backupCapacity.clear()
    backupCapacity.send_keys("1.0")
    sleep(1)


    #変更ボタン押下
    elem_search_editbtn = driver.find_element_by_id("editBtn")
    elem_search_editbtn.click()
    sleep(1)

    #スクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/本体設定_小数点.png"%(LogPath))

    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)
    sleep(1)
    driver.refresh()

    return 0
