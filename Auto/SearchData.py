##通話データ検索
import search
from time import sleep


def go(driver, logPath, IP):
    driver.get("http://%s/voisplus/search/list"%(IP))
    '''
    #2233
    search.set_Time(driver, "2018/10/09", "00:00:00", "2018/10/09", "23:59:59")
    search.search(driver, logPath, "時間検索_開始日時が終了日時より古い")
    sleep(1)
    driver.refresh()
    sleep(1)
    #2234
    search.set_Time(driver, "2018/10/02", "11:21:22", "2018/10/02", "11:21:22")
    search.search(driver, logPath, "時間検索_開始日時と終了日時が全く同一")
    sleep(1)
    driver.refresh()
    sleep(1)

    #2235
    search.set_Time(driver, "2018/10/02", "12:00:00", "2018/10/01", "00:00:00")
    search.search(driver, logPath, "時間検索_開始日時が終了日時より新しい")
    sleep(1)
    driver.refresh()
    sleep(1)

    #2236
    search.set_Time(driver, "2020/10/01", "00:00:00", "2018/10/01", "00:00:00")
    search.search(driver, logPath, "時間検索_開始日時が未来")
    sleep(1)
    driver.refresh()
    sleep(1)

    search.set_Time(driver, "2020/10/01", "12:00:00", "2018/10/01", "00:00:00")
    search.search(driver, logPath, "時間検索_「開始日」と「終了日」が同一日で開始時間が終了時間より新しい")
    sleep(1)
    driver.refresh()
    sleep(1)

    search.set_Time(driver, "", "", "", "")
    search.search(driver, logPath, "時間検索_空白")
    sleep(1)
    driver.refresh()
    sleep(1)


    search.set_Time(driver, "2018/10/09", "00:00:00", "2018/10/09", "23:59:59")
    search.set_CallTime(driver, "0", "s", "more")
    search.search(driver, logPath, "通話時間_0秒以上")
    sleep(1)
    driver.refresh()
    sleep(1)

    #0秒未満
    search.set_CallTime(driver, "0", "s", "less")
    search.search(driver, logPath, "通話時間_0秒未満")
    sleep(1)
    driver.refresh()
    sleep(1)

    search.set_Time(driver, "2018/10/09", "00:00:00", "2018/10/09", "23:59:59")
    search.set_CallTime(driver, "0", "m", "more")
    search.search(driver, logPath, "通話時間_0分以上")
    sleep(1)
    driver.refresh()
    sleep(1)

    #0分未満
    search.set_CallTime(driver, "0", "m", "less")
    search.search(driver, logPath, "通話時間_0分未満")
    sleep(1)
    driver.refresh()
    sleep(1)

    #0時未満
    search.set_CallTime(driver, "0", "h", "less")
    search.search(driver, logPath, "通話時間_0時未満")
    sleep(1)
    driver.refresh()
    sleep(1)

    search.set_Time(driver, "2018/10/09", "00:00:00", "2018/10/09", "23:59:59")
    search.set_CallTime(driver, "0", "h", "more")
    search.search(driver, logPath, "通話時間_0時以上")
    sleep(1)
    driver.refresh()
    sleep(1)

    search.set_Time(driver, "2018/10/09", "11:21:22", "2018/10/09", "11:53:14")
    search.set_header(driver, "05021002003", "", "", "", "")
    search.search(driver, logPath, "相手先電話番号_相手先電話番号")
    sleep(1)
    driver.refresh()
    sleep(1)

    search.set_Time(driver, "2018/10/09", "11:21:22", "2018/10/09", "11:53:14")
    search.set_header(driver, "05021002002", "", "", "", "")
    search.search(driver, logPath, "相手先電話番号_自社電話番号")
    sleep(1)
    driver.refresh()
    sleep(1)

    search.set_Time(driver, "2018/10/09", "11:21:22", "2018/10/09", "11:53:14")
    search.set_header(driver, "99999999", "", "", "", "")
    search.search(driver, logPath, "相手先電話番号_架空の番号")
    sleep(1)
    driver.refresh()
    sleep(1)


    search.set_Time(driver, "2018/10/09", "11:21:22", "2018/10/09", "11:53:14")
    search.set_header(driver, "", "05021002002", "", "", "")
    search.search(driver, logPath, "自社電話番号_自社電話番号")
    sleep(1)
    driver.refresh()
    sleep(1)

    search.set_Time(driver, "2018/10/09", "11:21:22", "2018/10/09", "11:53:14")
    search.set_header(driver, "", "05021002003", "", "", "")
    search.search(driver, logPath, "自社電話番号_相手先電話番号")
    sleep(1)
    driver.refresh()
    sleep(1)

    search.set_Time(driver, "2018/10/09", "11:21:22", "2018/10/09", "11:53:14")
    search.set_header(driver, "", "99999999", "", "", "")
    search.search(driver, logPath, "自社電話番号_架空の番号")
    sleep(1)
    driver.refresh()
    sleep(1)
'''
    search.set_Time(driver, "2018/10/09", "00:00:00", "2018/10/09", "23:59:59")
    search.search(driver, logPath, "")
    sleep(1)
    search.check_stars(driver, "2")
    search.check_stars(driver, "3")
    sleep(1)
    driver.refresh()
    sleep(1)
    search.set_Time(driver, "2018/10/09", "00:00:00", "2018/10/09", "23:59:59")
    search.set_mark(driver, "1")
    search.search(driver, logPath, "マーク_マーク済み")
    sleep(1)
    driver.refresh()
    sleep(1)

    search.set_Time(driver, "2018/10/09", "00:00:00", "2018/10/09", "23:59:59")
    search.set_mark(driver, "0")
    search.search(driver, logPath, "マーク_マークなし")
    sleep(1)
    driver.refresh()
    sleep(1)
