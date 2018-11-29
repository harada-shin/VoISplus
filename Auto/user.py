from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

def add(driver, url, UserName, PWD, UserType):

    driver.get(url)

    #名前
    driver.find_element_by_id("userName").send_keys(UserName)

    #ログインID
    driver.find_element_by_id("loginId").send_keys(UserName)

    #パスワード
    driver.find_element_by_id("passwd").send_keys(PWD)

    #パスワード（再入力）
    driver.find_element_by_id("confirmPasswd").send_keys(PWD)

    user = driver.find_element_by_id("userTypeList")
    #セレクトタグの要素を指定してSelectクラスのインスタンスを作成
    userTypeList = Select(user)
    #セレクトタグのオプションをテキストを指定して選択する
    userTypeList.select_by_visible_text(UserType)

    #コメント
    driver.find_element_by_id("description").send_keys(UserName)

    driver.find_element_by_id("Search").click()
    driver.find_element_by_id("Edit").click()
    driver.find_element_by_id("Play").click()
    driver.find_element_by_id("Save").click()
    driver.find_element_by_id("DelFlag").click()
    driver.find_element_by_id("Delete").click()
    driver.find_element_by_id("Human").click()
    driver.find_element_by_id("Device").click()
    driver.find_element_by_id("StateLogView").click()
    driver.find_element_by_id("StateLogEdit").click()

    #所属グループ登録
    driver.find_element_by_id("checkUserPriv-0").click()

    #追加
    driver.find_element_by_id("sendbtn").click()
