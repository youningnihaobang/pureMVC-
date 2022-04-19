'''
这是主入口

author：youningnihaoban
'''

import wx
from view.wxForm import wxFrame





app=wx.App()

#在wxFrame类中调用了Facade实例化
frame=wxFrame(None)
frame.Show()

app.MainLoop()