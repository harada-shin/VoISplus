from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import login
import log
import url
import iptable
from device import takacom
from device import webdav
from device import cfs
from device import la6000
from device import Initial
from device import callLogger
from device import setting
import search
import Line
import group
import History
import user
import batch
import ssh
import check
import SearchData



driver = webdriver.Chrome("c:/driver/chromedriver.exe")
#login.login(driver,"auto_taro","auto_taro_001")


login.login(driver,"nxgadmin","nxgadmin")

#user.add(driver, url.Useradd, "auto_taro", "auto_taro_001", "管理者")


#Initial.setting(driver, url.Setting, log.Device)

#group.add(driver,url.Group,"auto_group_01")
#group.add(driver,url.Group,"auto_group_02")


#la6000.setting(driver, iptable.VoIS, iptable.La6k, log.Device, url.La6k_add)
#Line.Register(driver, log.Device)
#ssh.PutCommand(iptable.La6k, "mkdir /home/nextgen/NXS/lumberyard/9")
#batch.Put(iptable.La6k, "C:/Auto/wav/", "/home/nextgen/NXS/lumberyard/9")
##収集ボタン入れる処理必要
##ユーザのauto_group_01の所属ボタンに✔を入れる処理
SearchData.go(driver, log.Search,iptable.VoIS)
History.VoiceOperation(driver, url.VoiceOpHistory, log.Device)
History.Login(driver, url.LoginHistory, log.Device)
History.Alarm(driver, url.AlarmHistory, log.Device)
History.Backup(driver, url.BackupHistory, log.Device)
History.Collectionfile(driver, url.CollectionFileHistory, log.Device)

setting.min(driver, log.Device , url.Setting)
setting.max(driver, log.Device , url.Setting)
setting.over(driver, log.Device , url.Setting)
setting.under(driver, log.Device , url.Setting)
setting.DecimalPoint(driver, log.Device , url.Setting)


#波形表示確認
#check.getPlayWin(driver, log.Search)


takacom.VR(driver, iptable.Takacom_508a, url.Takacom_508ah_add,log.Takacom, "508a")
Line.TakacomRegister(driver,log.Takacom)
takacom.VR(driver, iptable.Takacom_508h, url.Takacom_508ah_add,log.Takacom, "508h")
Line.TakacomRegister(driver,log.Takacom)
takacom.VR(driver, iptable.Takacom_504bri, url.Takacom_504bri_add,log.Takacom, "504bri")
Line.TakacomRegister(driver,log.Takacom)

webdav.setting_new_all(driver, url.Webdav, url.Device, log.Webdav)

webdav.setting_change(driver, url.Webdav, url.Device, log.Webdav)

webdav.move_Line(driver, url.Webdav)
Line.webdav(driver,log.Webdav)

cfs.setting(driver, url.Cfs, log.Cfs)
cfs.move_Line(driver, url.Cfs)
Line.cfs(driver, log.Cfs)
callLogger.setting(driver, url.CallLogger, iptable.CallLogger, log.CallLogger,url.CL_smb, url.CL_db )
