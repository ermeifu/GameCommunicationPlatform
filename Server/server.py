import wx
import socket

APP_TITLE = '博弈通讯平台（服务端）'
PORT = '9922'

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


class ServerFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, APP_TITLE)



class ServerPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.ipStr = wx.StaticText(self, label='你的IP地址：' + get_host_ip(), pos=(10, 10))

        self.portStr = wx.StaticText(self, label='请输入你要使用的端口：', pos=(10, 30))
        self.portVal = wx.TextCtrl(self, value=PORT, pos=(155, 30))

        self.portVal.SetMaxLength(5)

        gameList = ['象棋', '围棋', '五子棋', '斗地主', '麻将']
        self.gameBox = wx.RadioBox(self, label='请选择博弈类型：', pos=(10, 60), choices=gameList, majorDimension=3, style=wx.RA_SPECIFY_COLS)

        self.sendButton = wx.Button(self, label='发送广播', pos=(10, 125))



class ServerAPP(wx.App):

    def OnInit(self):
        self.Frame = ServerFrame(None)
        ServerPanel(self.Frame)
        self.Frame.Show()

        return True


if __name__ == '__main__':
    app = ServerAPP()
    app.MainLoop()

