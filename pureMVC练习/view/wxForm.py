import wx
from AppFacade import ApplicationFacade

class wxFrame(wx.Frame):
    '''
        一个无逻辑的界面展示
    '''

    def __init__(self,parent):

        super(wxFrame,self).__init__(parent)
        self.initControl()
        self.initFacade()
        pass

    #初始化控件
    def initControl(self):
        self.txt=wx.TextCtrl(self,style=wx.TE_PROCESS_ENTER)
        pass
    
    #实例化Facade
    def initFacade(self):
        self.demo_facade=ApplicationFacade.getInstance()    #直接实例化一个类是一样的
        #进行startUp后，开始注册和执行StartupCommand
        self.demo_facade.startUp(self)