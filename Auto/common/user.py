from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def add(driver, UserName, PWD, UserType,bit):

    driver.get(useradd_url())

    #名前
    Name = driver.find_element_by_id("userName")
    Name.send_keys(UserName)

    #ログインID
    id = driver.find_element_by_id("loginId")
    id.send_keys(UserName)

    #パスワード
    pwd = driver.find_element_by_id("passwd")
    pwd.send_keys(PWD)

    #パスワード（再入力）
    repwd = driver.find_element_by_id("confirmPasswd")
    repwd.send_keys(PWD)

    #コメント
    comment = driver.find_element_by_id("description")
    comment.send_keys(UserName)

    if UserType == "1":
        #ユーザ種別
        type = driver.find_element_by_id("userTypeList")
        Select(type).select_by_visible_text("一般")
        if bit == "00000":
            return 0

        if bit == "11111":
            search = driver.find_element_by_id("Search")
            search.click()

            Edit = driver.find_element_by_id("Edit")
            Edit.click()

            Play = driver.find_element_by_id("Play")
            Play.click()

            Save = driver.find_element_by_id("Save")
            Save.click()

            DelFlag = driver.find_element_by_id("DelFlag")
            DelFlag.click()

    if UserType == "0":
        #ユーザ種別
        type = driver.find_element_by_id("userTypeList")
        Select(type).select_by_visible_text("管理者")

        if bit == "111110000":
            search = driver.find_element_by_id("Search")
            search.click()

            Edit = driver.find_element_by_id("Edit")
            Edit.click()

            Play = driver.find_element_by_id("Play")
            Play.click()

            Save = driver.find_element_by_id("Save")
            Save.click()

            DelFlag = driver.find_element_by_id("DelFlag")
            DelFlag.click()

        if bit == "111111011":
            search = driver.find_element_by_id("Search")
            search.click()

            Edit = driver.find_element_by_id("Edit")
            Edit.click()

            Play = driver.find_element_by_id("Play")
            Play.click()

            Save = driver.find_element_by_id("Save")
            Save.click()

            DelFlag = driver.find_element_by_id("DelFlag")
            DelFlag.click()

            Delete = driver.find_element_by_id("Delete")
            Delete.click()

            Edit = driver.find_element_by_id("Edit")
            Edit.click()

            Device = driver.find_element_by_id("Device")
            Device.click()

            StateLogView = driver.find_element_by_id("StateLogView")
            StateLogView.click()

            StateLogEdit = driver.find_element_by_id("StateLogEdit")
            StateLogEdit.click()
