import iptable

VoisIP = iptable.VoIS
CallLoggerIP = iptable.CallLogger

Useradd = "http://%s/voisplus/user/edit"%(VoisIP)
Group = "http://%s/voisplus/group"%(VoisIP)
Device = "http://%s/voisplus/device"%(VoisIP)
Takacom_508ah_add = "http://%s/voisplus/device/vr508/add"%(VoisIP)
Takacom_504bri_add = "http://%s/voisplus/device/vr504/add"%(VoisIP)
Webdav = "http://%s/voisplus/device/docomo/add"%(VoisIP)
Cfs = "http://%s/voisplus/device/kddi/add"%(VoisIP)
Setting = "http://%s/voisplus/setting/"%(VoisIP)
La6k_edit = "http://%s/voisplus/device/la6000/edit/"%(VoisIP)
La6k_add = "http://%s/voisplus/device/la6000/add"%(VoisIP)
La6k_line = "http://%s/voisplus/device/line/la6000/1"%(VoisIP)
CallLogger = "http://%s/voisplus/device/calllogger/add"%(VoisIP)
VoiceOpHistory = "http://%s/voisplus/history/operation/"%(VoisIP)
LoginHistory = "http://%s/voisplus/history/login/"%(VoisIP)
AlarmHistory = "http://%s/voisplus/history/alarm/"%(VoisIP)
BackupHistory = "http://%s/voisplus/history/backup/"%(VoisIP)
CollectionFileHistory = "http://%s/voisplus/history/collection/"%(VoisIP)

CL_smb = "smb://%s/la5k_data$"%(CallLoggerIP)
CL_db = "jdbc:sqlserver://%s;databaseName=STDL5SQL"%(CallLoggerIP)
