import puremvc.patterns.facade

#一个入口程序

class ApplicationFacade(puremvc.patterns.facade.Facade):


    #消息列表
    STARTUP="startup"
    SUBMIT="submit"
    TXT_CHANGE="change"

    #初始化自身，不需要
    @staticmethod#静态方法，应该是作为单例使用的
    def getInstance():
        return ApplicationFacade()
        pass
    
    #这是重写Facade的方法，不要也行，可以试试
    def initializeController(self):
        super(ApplicationFacade,self).initializeController()

        #导入 .. 路径 暂且没看到有什么作用
        import sys
        if ".." not in sys.path:
            sys.path.append("..")

        #导入一些Command
        from controller.DataSubmittedCommand import DataSubmittedCommand
        #按照流程，需要先注册Commands -> Models -> Mediators ,而StartupCommand是一个注册类，用于执行其他注册流程
        from controller.StartupCommand import StartupCommand

        #==============重点：注册两个Command，分别初始化Controller、Model、View==================================================================
        super(ApplicationFacade,self).registerCommand(ApplicationFacade.STARTUP,StartupCommand) # 注册初始化的Controller，使用super（父类方法） 注册Command ,在没有重写registerCommand函数的情况下，可以使用self.registerCommand
        super(ApplicationFacade,self).registerCommand(ApplicationFacade.SUBMIT,DataSubmittedCommand)    #注册更改Data的Controller
        #=====================================================================================================================================


    #===============================================
    def startUp(self,app):
        self.sendNotification(ApplicationFacade.STARTUP,app)    #发送【启动】通知，注册的类会收到通知，通知执行StartupCommand ,app参数是向 通知的 Body里面放入对象，可以通过【订阅】的通知获得
        super(ApplicationFacade,self).removeCommand(ApplicationFacade.STARTUP)  #初始化完成后，注销 【启动】 的通知




