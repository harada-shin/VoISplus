from time import sleep
import group

###LA-6000の回線を設定
def Register(driver, LogPath):
    sleep(1)
    group.Register(driver, "auto_group_01","And","","","","")
    sleep(1)
    group.Register(driver, "auto_group_01","Or","","","","")
    sleep(1)
    group.Register(driver, "auto_group_01","All","","","","")
    sleep(1)
    group.Register(driver, "auto_group_02","And","08012345678","","","")
    sleep(1)
    group.Register(driver, "auto_group_02","And","08012345678","0345671234","","")
    sleep(1)
    group.Register(driver, "auto_group_02","And","08012345678","0345671234","7070","")
    sleep(1)
    group.Register(driver, "auto_group_02","And","08012345678","0345671234","7070","検証本部")
    sleep(1)
    group.Register(driver, "auto_group_02","Or","08012345678","","","")
    sleep(1)
    group.Register(driver, "auto_group_02","Or","08012345678","0345671234","","")
    sleep(1)
    group.Register(driver, "auto_group_02","Or","08012345678","0345671234","7070","")
    sleep(1)
    group.Register(driver, "auto_group_02","Or","08012345678","0345671234","7070","検証本部")
    sleep(1)

    group.Register(driver, "auto_group_02","And","!@#$%^&*(_+}{:?><})'""'","!@#$%^&*(_+}{:?><})'""'","!@#$%^&*(_+}{:?><})'""'","!@#$%^&*(_+}{:?><})'""'")
    sleep(1)
    group.Register(driver, "auto_group_02","Or","!@#$%^&*(_+}{:?><})'""'","!@#$%^&*(_+}{:?><})'""'","!@#$%^&*(_+}{:?><})'""'","!@#$%^&*(_+}{:?><})'""'")
    sleep(1)


    #初期情報をスクリーンショットを取得し保存
    sfile = driver.get_screenshot_as_file("%s/LA6K回線設定.png"%(LogPath))
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)


def TakacomRegister(driver, LogPath):
    group.TakacomRegister(driver, "auto_group_01", "And", "","","","0","")
    group.TakacomRegister(driver, "auto_group_02", "All", "","","","0","")
    group.TakacomRegister(driver, "auto_group_01", "And", "08012345678","0323456789","1","0","")
    group.TakacomRegister(driver, "auto_group_01", "And", "08012345678","0323456789","8","0","")
    group.TakacomRegister(driver, "auto_group_01", "And", "08012345678","0323456789","1,2,3,4,5,6,7,8","0","")
    group.TakacomRegister(driver, "auto_group_01", "And", "08012345678","0323456789","1-3,4-6,7,8","0","")
    group.TakacomRegister(driver, "auto_group_01", "And", "検証,本部","検証,しています","1,2,3,4,5,6,7,8","0","")
    group.TakacomRegister(driver, "auto_group_01", "And", "kennsyou","honbu","1,2,3,4,5,6,7,8","0","")
    group.TakacomRegister(driver, "auto_group_01", "And", "全角入力できるか","検証しています","1,2,3,4,5,6,7,8","0","")

    group.TakacomRegister(driver, "auto_group_01", "Or", "","","","0","")
    group.TakacomRegister(driver, "auto_group_01", "Or", "08012345678","0323456789","1","0","")
    group.TakacomRegister(driver, "auto_group_01", "Or", "08012345678","0323456789","8","0","")
    group.TakacomRegister(driver, "auto_group_01", "Or", "08012345678","0323456789","1,2,3,4,5,6,7,8","0","")
    group.TakacomRegister(driver, "auto_group_01", "Or", "08012345678","0323456789","1-3,4-6,7,8","0","")
    group.TakacomRegister(driver, "auto_group_01", "Or", "検証,本部","検証,しています","1,2,3,4,5,6,7,8","0","")
    group.TakacomRegister(driver, "auto_group_01", "Or", "kennsyou","honbu","1,2,3,4,5,6,7,8","0","")
    group.TakacomRegister(driver, "auto_group_01", "Or", "全角入力できるか","検証しています","1,2,3,4,5,6,7,8","0","")


    sfile = driver.get_screenshot_as_file("%s/Takacom回線設定（登録成功）.png"%(LogPath))
    #カレントページのスクリーンショットが取得出来たか確認(取得できた場合はTRUE)
    print(sfile)
    sleep(1)
    group.TakacomRegister(driver, "auto_group_01", "And", "08012345678","0323456789","1~8","%s"%(LogPath),"Takacom回線設定（その他記号１）")
    sleep(1)
    group.TakacomRegister(driver, "auto_group_01", "And", "08012345678","0323456789","1'8","%s"%(LogPath),"Takacom回線設定（その他記号２）")
    sleep(1)
    group.TakacomRegister(driver, "auto_group_01", "And", "08012345678","0323456789","9","%s"%(LogPath),"Takacom回線設定（その他数字１）")
    sleep(1)
    group.TakacomRegister(driver, "auto_group_01", "And", "08012345678","0323456789","0","%s"%(LogPath),"Takacom回線設定（その他数字２）")

    sleep(1)
    group.TakacomRegister(driver, "auto_group_01", "And", "08012345678","0323456789","8-1","%s"%(LogPath),"Takacom回線設定（ハイフン指定右―左）")

    sleep(1)
    group.TakacomRegister(driver, "auto_group_01", "And", "08012345678","0323456789","1--8","%s"%(LogPath),"Takacom回線設定（ハイフン複数）")


    return 0

def cfs(driver, LogPath):
    group.cfsRegister(driver, "auto_group_01", "All", "08012345678","0323456789","0","" )
    sleep(1)
    group.cfsRegister(driver, "auto_group_01", "And", "08012345678","0323456789","0","" )
    sleep(1)
    group.cfsRegister(driver, "auto_group_01", "And", "08012345678","0323456789","0","" )
    sleep(1)
    group.cfsRegister(driver, "auto_group_02", "Or", "08012345678","0323456789","0","" )
    sleep(1)
    group.cfsRegister(driver, "auto_group_02", "All", "08012345678","0323456789","0","" )
    sleep(1)
    sfile = driver.get_screenshot_as_file("%s/回線設定.png"%(LogPath))
    sleep(1)
    return 0


def webdav(driver, LogPath):
    group.webdavRegister(driver, "auto_group_01", "All", "","","","0", "" )
    sleep(1)
    group.webdavRegister(driver, "auto_group_01", "And", "08012345678","0323456789","docomo1", "0", "" )
    sleep(1)
    group.webdavRegister(driver, "auto_group_01", "And", "08012345678","0323456789","docomo1", "0", "" )
    sleep(1)
    group.webdavRegister(driver, "auto_group_01", "Or", "09012345678","07223456789","docomo7", "0", "" )
    sleep(1)
    sfile = driver.get_screenshot_as_file("%s/回線設定.png"%(LogPath))
    sleep(1)
    group.webdavRegister(driver, "auto_group_01", "Or", "09012345678","07223456789","0", "%s"%(LogPath), "回線設定確認URL用識別コードを未選択" )

    return 0
