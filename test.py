from wxauto import WeChat
wx = WeChat()
print(wx.GetSessionList())

with open("D:\\log.txt","r",encoding="gbk")as f:  #这个.txt里写要发送的文字
    for line in f.readlines():
        who = 'gc' #这里填要发送的人的备注
        wx.ChatWith(who)
        wx.SendMsg(line)