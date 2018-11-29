from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("c:/driver/chromedriver.exe")
driver.get("http://192.168.34.26/voisplus/")


#ログイン情報入力
elem_search_word = driver.find_element_by_id("loginId")
elem_search_word.send_keys("auto_taro")
elem_search_word = driver.find_element_by_id("password")
elem_search_word.send_keys("auto_taro_001")
#ログイン
elem_search_btn = driver.find_element_by_id("login-btn")
elem_search_btn.click()

#カレントウインドウを最大化する
driver.maximize_window()

#本体設定変更画面に遷移
driver.get("http://192.168.34.26/voisplus/device/line/la6000/1")

add_btn = driver.find_element_by_id("add_btn")
add_btn.click()

###############################group_01#############################################
groupId = driver.find_element_by_id("groupId")
#セレクトタグの要素を指定してSelectクラスのインスタンスを作成
selectGroup = Select(groupId)
#セレクトタグのオプションをテキストを指定して選択する
selectGroup.select_by_visible_text("auto_group_01")

#条件入力
condBindFlagAnd = driver.find_element_by_id("condBindFlagAnd")
condBindFlagAnd.click()

save_btn = driver.find_element_by_id("save_btn")
save_btn.click()

#ページを更新(ブラウザのリフレッシュ)
driver.refresh()

add_btn = driver.find_element_by_id("add_btn")
add_btn.click()

groupId = driver.find_element_by_id("groupId")
#セレクトタグの要素を指定してSelectクラスのインスタンスを作成
selectGroup = Select(groupId)
#セレクトタグのオプションをテキストを指定して選択する
selectGroup.select_by_visible_text("auto_group_01")

#条件入力
condBindFlagAnd = driver.find_element_by_id("condBindFlagOr")
condBindFlagAnd.click()

save_btn = driver.find_element_by_id("save_btn")
save_btn.click()


#ページを更新(ブラウザのリフレッシュ)
driver.refresh()

add_btn = driver.find_element_by_id("add_btn")
add_btn.click()

groupId = driver.find_element_by_id("groupId")
#セレクトタグの要素を指定してSelectクラスのインスタンスを作成
selectGroup = Select(groupId)
#セレクトタグのオプションをテキストを指定して選択する
selectGroup.select_by_visible_text("auto_group_01")

#条件入力
condBindFlagAnd = driver.find_element_by_id("condBindFlagAll")
condBindFlagAnd.click()

save_btn = driver.find_element_by_id("save_btn")
save_btn.click()


###############################group_02#############################################
add_btn = driver.find_element_by_id("add_btn")
add_btn.click()

groupId = driver.find_element_by_id("groupId")
#セレクトタグの要素を指定してSelectクラスのインスタンスを作成
selectGroup = Select(groupId)
#セレクトタグのオプションをテキストを指定して選択する
selectGroup.select_by_visible_text("auto_group_02")

#条件入力
condBindFlagAnd = driver.find_element_by_id("condBindFlagAnd")
condBindFlagAnd.click()

##相手先電話番号
elem_search_word = driver.find_element_by_id("loginId")
elem_search_word.send_keys("auto_taro")

#自社電話番号
elem_search_word = driver.find_element_by_id("loginId")
elem_search_word.send_keys("auto_taro")

#内線番号


save_btn = driver.find_element_by_id("save_btn")
save_btn.click()

#ページを更新(ブラウザのリフレッシュ)
driver.refresh()

add_btn = driver.find_element_by_id("add_btn")
add_btn.click()

groupId = driver.find_element_by_id("groupId")
#セレクトタグの要素を指定してSelectクラスのインスタンスを作成
selectGroup = Select(groupId)
#セレクトタグのオプションをテキストを指定して選択する
selectGroup.select_by_visible_text("auto_group_02")

#条件入力
condBindFlagAnd = driver.find_element_by_id("condBindFlagOr")
condBindFlagAnd.click()

save_btn = driver.find_element_by_id("save_btn")
save_btn.click()


#ページを更新(ブラウザのリフレッシュ)
driver.refresh()

add_btn = driver.find_element_by_id("add_btn")
add_btn.click()

groupId = driver.find_element_by_id("groupId")
#セレクトタグの要素を指定してSelectクラスのインスタンスを作成
selectGroup = Select(groupId)
#セレクトタグのオプションをテキストを指定して選択する
selectGroup.select_by_visible_text("auto_group_02")

#条件入力
condBindFlagAnd = driver.find_element_by_id("condBindFlagAll")
condBindFlagAnd.click()

save_btn = driver.find_element_by_id("save_btn")
save_btn.click()





#スクリーンショットを取得し保存
sfile = driver.get_screenshot_as_file("c:/Auto/logs/Line_la6000.png")

#カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
print(sfile)
