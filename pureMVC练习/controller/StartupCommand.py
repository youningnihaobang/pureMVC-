import puremvc.patterns.command



class StartupCommand(puremvc.patterns.command.SimpleCommand):
    def execute(self,Notification):
        print("执行execute")

        #取得消息中的对象
        app=Notification.getBody()

        #注册View和Model

    pass