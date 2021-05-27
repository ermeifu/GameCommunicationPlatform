import wx

APP_TITLE = '博弈通讯平台（客户端）'
PORT = '9922'
HOST = '127.0.0.1'

class ClientFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, APP_TITLE)



class ClientPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.ipStr = wx.StaticText(self, label='请输入服务器的IP地址：', pos=(10, 10))
        self.ipVal = wx.TextCtrl(self, value=HOST, pos=(200, 10))
        self.ipVal.SetMaxLength(15)

        self.portStr = wx.StaticText(self, label='请输入服务器使用的端口：', pos=(10, 30))
        self.portVal = wx.TextCtrl(self, value=PORT, pos=(200, 30))

        self.portVal.SetMaxLength(5)

        gameList = ['象棋', '围棋', '五子棋', '斗地主', '麻将']
        self.gameBox = wx.RadioBox(self, label='请选择博弈类型：', pos=(10, 60), choices=gameList, majorDimension=3, style=wx.RA_SPECIFY_COLS)

        self.sendButton = wx.Button(self, label='向服务器发起连接', pos=(10, 125))



class ServerAPP(wx.App):

    def OnInit(self):
        self.Frame = ClientFrame(None)
        ClientPanel(self.Frame)
        self.Frame.Show()

        return True


if __name__ == '__main__':
    app = ServerAPP()
    app.MainLoop()

