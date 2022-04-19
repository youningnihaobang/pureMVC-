import puremvc.patterns.command
from model.ModelProxy import ModelProxy
class DataSubmittedCommand(puremvc.patterns.command.SimpleCommand):
    
    def execute(self, notification):
        print("DataSubmitted 进来了")
        #接收消息通知
        label=notification.getBody()

        #通过retrieveProxy找到对象，调用函数,也可以通过消息通知
        dataProxy=self.facade.retrieveProxy(ModelProxy.Proxy_Name)
        dataProxy.SetData(label)

        
    