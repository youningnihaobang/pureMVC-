import puremvc.patterns.proxy
from model.model_data import Data
from AppFacade import ApplicationFacade


class ModelProxy(puremvc.patterns.proxy.Proxy):
    Proxy_Name="Data_Proxy"

    def __init__(self, proxyName=None, data=None):
        super().__init__(self.Proxy_Name, data)
        print("初始化Proxy")
        #界面启动将data的文本丢到文本框中
        self.model_data=Data()
        #发送消息通知
        self.sendNotification(ApplicationFacade.TXT_CHANGE,self.model_data.data)

    #通过Controller用facade的retrieveProxy来获得Proxy调用SetData
    def SetData(self,data):
        self.model_data.data=data

        print("data数据已变更：%s"%self.model_data.data)
        #发送消息通知
        self.sendNotification(ApplicationFacade.TXT_CHANGE,data)