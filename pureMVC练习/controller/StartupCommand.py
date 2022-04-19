import puremvc.patterns.command
from view.ViewMediator import ViewMediator
from model.ModelProxy import ModelProxy
from view.wxForm import wxFrame

class StartupCommand(puremvc.patterns.command.SimpleCommand):
    def execute(self,Notification):
        print("执行execute")

        #取得消息中的对象
        app=Notification.getBody()

        #注册View和Model
        self.facade.registerMediator(ViewMediator(None,app))
        self.facade.registerProxy(ModelProxy(None,None))
    pass