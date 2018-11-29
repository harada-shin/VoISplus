from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep


###############################登録################################
def Register(driver,GroupName,Flag,RemoteNum,LocalNum,ExtNum,AgentID):
    add_btn = driver.find_element_by_id("add_btn")
    add_btn.click()
    if Flag == "All":
        input_GroupName(driver,GroupName)
        input_flag(driver,Flag)
    else:
        input_GroupName(driver,GroupName)
        input_flag(driver,Flag)
        input_GroupName(driver,GroupName)
        input_flag(driver,Flag)
        input_remote(driver,RemoteNum)
        input_local(driver,LocalNum)
        input_ext(driver,ExtNum)
        input_agentID(driver,AgentID)

        save_btn = driver.find_element_by_id("save_btn")
        save_btn.click()

        #ページを更新(ブラウザのリフレッシュ)
        driver.refresh()

    return 0

##################################################################
def input_GroupName(driver,GroupName):
    if GroupName is None:
        cancel_btn = driver.find_element_by_id("cancel_btn")
        cancel_btn.click()
    else:
        groupId = driver.find_element_by_id("groupId")
        #セレクトタグの要素を指定してSelectクラスのインスタンスを作成
        selectGroup = Select(groupId)
        #セレクトタグのオプションをテキストを指定して選択する
        selectGroup.select_by_visible_text(GroupName)
    return 0

def input_flag(driver,Flag):
        if Flag == "And":
            #条件入力
            condBindFlagAnd = driver.find_element_by_id("condBindFlagAnd")
            condBindFlagAnd.click()
        elif Flag == "Or":
            #条件入力
            condBindFlagAnd = driver.find_element_by_id("condBindFlagOr")
            condBindFlagAnd.click()
        elif Flag == "All":
            #条件入力
            condBindFlagAnd = driver.find_element_by_id("condBindFlagAll")
            condBindFlagAnd.click()
            save_btn = driver.find_element_by_id("save_btn")
            save_btn.click()
            #ページを更新(ブラウザのリフレッシュ)
            driver.refresh()


        else:
            cancel_btn = driver.find_element_by_id("cancel_btn")
            cancel_btn.click()
        return 0

def input_remote(driver,RemoteNum):
        if RemoteNum is None:
            save_btn = driver.find_element_by_id("save_btn")
            save_btn.click()
            #ページを更新(ブラウザのリフレッシュ)
            driver.refresh()
        else:
            remoteNumber = driver.find_element_by_id("remoteNumber")
            remoteNumber.send_keys(RemoteNum)

        return 0

def input_local(driver,LocalNum):
        if LocalNum is None:
            save_btn = driver.find_element_by_id("save_btn")
            save_btn.click()
            #ページを更新(ブラウザのリフレッシュ)
            driver.refresh()
        else:
            localNumber = driver.find_element_by_id("localNumber")
            localNumber.send_keys(LocalNum)
        return 0

def input_ext(driver,ExtNum):
        if ExtNum is None:
            cancel_btn = driver.find_element_by_id("cancel_btn")
            cancel_btn.click()
        else:
            extensionNumber = driver.find_element_by_id("extensionNumber")
            extensionNumber.send_keys(ExtNum)
        return 0

def input_agentID(driver,AgentID):
        if AgentID is None:
            cancel_btn = driver.find_element_by_id("cancel_btn")
            cancel_btn.click()
        else:
            agentId = driver.find_element_by_id("agentId")
            agentId.send_keys(AgentID)
        return 0
