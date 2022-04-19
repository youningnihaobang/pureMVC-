import puremvc.patterns.mediator
import wx
from AppFacade import ApplicationFacade

#初始化一个Mediator
class ViewMediator(puremvc.patterns.mediator.Mediator):
    def __init__(self, mediatorName=None, viewComponent=None):
        super().__init__(mediatorName, viewComponent)
        print("注册Mediator")
        #绑定一个事件
        # self.viewComponent.Bind(wx.EVT_TEXT_ENTER,self.onSubmit,self.viewComponent.txt)
        self.viewComponent.txt.Bind(wx.EVT_TEXT_ENTER,self.onSubmit)

    def listNotificationInterests(self):
        #需要重写该函数，返回可以接收的消息通知类型
        return [ApplicationFacade.TXT_CHANGE]


    #handler，是消息通知订阅函数，会时刻获得消息的通知
    def handleNotification(self, notification):
        print("handleNotification")
        #判断是否有TXT_CHANGE消息
        if notification.getName()==ApplicationFacade.TXT_CHANGE:
            print("获得文本变更的消息")
            txt=notification.getBody()
            self.viewComponent.txt.SetLabel(txt)
        
    #事件函数
    def onSubmit(self,evt):
        print('文本框回车')
        #获得文本
        txt=self.viewComponent.txt.GetValue()
        #将文字通过消息发送到Controller ,需要提前注册
        self.sendNotification(ApplicationFacade.SUBMIT,txt)
        pass

    