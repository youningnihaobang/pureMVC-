import puremvc.patterns.facade

#一个入口程序

class ApplicationFacade(puremvc.patterns.facade.Facade):

    STARTUP="startup"



    #初始化自身，不需要
    @staticmethod#静态方法，应该是作为单例使用的
    def getInstance(self):
        return ApplicationFacade()
        pass

    def initializeController(self):
        super(ApplicationFacade,self).initializeController()

        #导入 .. 路径 暂且没看到有什么作用
        import sys
        if ".." not in sys.path:
            sys.path.append("..")

        #按照流程，需要先注册Commands -> Models -> Mediators ,而StartupCommand是一个注册类，用于执行其他注册流程
        from controller.StartupCommand import StartupCommand

        super(ApplicationFacade,self).registerCommand(ApplicationFacade.STARTUP,StartupCommand) #使用super（父类方法） 注册Command ,在没有重写registerCommand函数的情况下，可以使用self.registerCommand

    def startUp(self,app):
        self.sendNotification(ApplicationFacade.STARTUP,app)    #发送【启动】通知，注册的类会收到通知，通知执行StartupCommand ,app参数是向 通知的 Body里面放入对象，可以通过【订阅】的通知获得
        super(ApplicationFacade,self).removeCommand(ApplicationFacade.STARTUP)  #初始化完成后，注销 【启动】 的通知




