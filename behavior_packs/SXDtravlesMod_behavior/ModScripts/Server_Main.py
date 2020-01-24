# -*- coding: utf-8 -*-
from ModScripts.modTools import logger
import server.extraServerApi as serverApi
import modConfig as modConfig
serverCls = serverApi.GetServerSystemCls()


class MainServerSystem(serverCls):

    def __init__(self, namespace, systemName):
        serverCls.__init__(self, namespace, systemName)
        self.timeTick = 0
        self.UpdateBool = False
        self.reSetNarratorPosBool = False
        self.sayBool = False
        self.saytimeTick = 0
        self.player = None
        self.narratorListId = ['-2190433320959', '-2190433320958', '-2190433320957', '-2190433320956',
                               '-2190433320955', '-2190433320954', '-2190433320953', '-2190433320952', '-2190433320951', '-2190433320950']
        self.narratorListPosX = [29, 38, 55, 83, 95, 112, 136, 140, 115, 111]
        self.narratorListPosY = [66, 66, 66, 68, 67, 67, 66, 66, 67, 67]
        self.narratorListPosZ = [-136, -123, -129, -
                                 139, -112, -98, -135, -147, -120, -109]

        # logger.info("<--MainServerSystem注册成功-->")
        self.ListenForEvent(serverApi.GetEngineNamespace(
        ), serverApi.GetEngineSystemName(), "PlayerAttackEntityEvent", self, self.PlayerAttackEntityEventHandler)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(
        ), "AddServerPlayerEvent", self, self.AddServerPlayerEventHandler)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(
        ), "ServerChatEvent", self, self.ServerChatEventHandler)
        self.ListenForEvent("SXDtravlesMod", "answerUI",
                            "ScoreEvent", self, self.ScoreEventHandler)
        self.ListenForEvent("SXDtravlesMod", "dialogUI",
                            "attackExtraDataEvent", self, self.attackExtraDataEventHandler)
        self.ListenForEvent("SXDtravlesMod", "ClientMain",
                            "TeacherTextEvent", self, self.TeacherTextEventHandler)
        self.ListenForEvent("SXDtravlesMod", "ClientMain",
                            "progressEvent", self, self.progressEventHandler)
        self.ListenForEvent("SXDtravlesMod", "ClientMain",
                            "canAnswerEvent", self, self.canAnswerEventHandler)

    def Destroy(self):
        pass
    # 帧事件

    def Update(self):
        self.saytimeTick += 1
        if self.saytimeTick % 600 == 0 and self.sayBool == False:
            logger.info("sayBoolTrue")
            self.sayBool = True
        if self.UpdateBool:
            self.timeTick += 1
            if self.timeTick == 150:
                commandComp = self.CreateComponent(
                    serverApi.GetLevelId(), "Minecraft", "command")
                commandComp.command = "/tp @s 32 65 -234"
                self.NeedsUpdate(commandComp)
            if self.timeTick == 450:
                self.chatToServer("老师：  请各位先自由行动，两分钟后集合哦,在外观赏一下场景！")
                self.chatToServer("老师：  然后大家将可以自由进入场馆学习历史文化！")

            if self.timeTick == 3600:
                self.chatToServer("老师：  时间到了，接下来让我们开始文化之旅吧！")
                commandComp = self.CreateComponent(
                    serverApi.GetLevelId(), "Minecraft", "command")
                commandComp.command = "/tp @s 31 66 -166"
                self.NeedsUpdate(commandComp)

            if self.timeTick == 300+3600:
                """
                """
                self.chatToServer("老师：  同学们，接下来我们要去的是三星堆博物馆。\n三星堆博物馆（Sanxingdui Museum）于1992年8月开始建造，1997年10月建成开放。\n是一座现代化的专题博物馆。\n三星堆博物馆有两个展馆，其展示面积12000平方米。\n跟着老师开始学习吧！"
                                  )
            if self.timeTick == 750+3600:
                self.UpdateBool = False
                # 开启narrator位置重置
                self.reSetNarratorPosBool = True
                comp = self.CreateComponent(self.player, "Minecraft", "game")
                comp.SetNotifyMsg(
                    "欢迎来到三星堆博物馆，您可以自由随意的在馆内闲逛。开始你的历史学习吧！")
                self.NeedsUpdate(comp)
                self.chatToServer("§e"+"PS: 走近解说员会有自动解说哟，与所有解说员互动完成后即可答题")
            # 每隔一段时间重置narrator位置
            if self.reSetNarratorPosBool:
                self.reSetNarratorPosBool = False
                self.retSetNarratorPos()
                logger.info("narrator控制")
            if self.timeTick == 6000:
                self.timeTick = 0

                #########################################################################################################################################################

    def PlayerAttackEntityEventHandler(self, args):
        logger.info(args['victimId'])
        print args['victimId']
        # 攻击伤害设定
        args['damage'] = 0
        args['isValid'] = 1
        comp = self.CreateComponent(self.player, "Minecraft", "game")
        comp.SetNotifyMsg("不可以攻击别人哦")
        self.NeedsUpdate(comp)
        # logger.info("attackmob!!!!!!!!!!!!!!!!!!!!!!!!" + str(args))

    def AddServerPlayerEventHandler(self, args):
        self.UpdateBool = True
        self.player = args['id']

    def ServerChatEventHandler(self, args):
        if args['message'] == "开始学习":
            # 调用dialog
            self.NotifyToClient(args['playerId'], "chatServerHandler", args)
        if args['message'] == "开始答题":
            commandComp = self.CreateComponent(
                serverApi.GetLevelId(), "Minecraft", "command")
            commandComp.command = "/tp @s 70 68 -119"  # 传送指令
            self.NeedsUpdate(commandComp)
            # 调用dialog
            self.NotifyToClient(args['playerId'], "chatServerHandler", args)
        if args['message'] == "归位":
            self.retSetNarratorPos()

    def ScoreEventHandler(self, args):
        if args['score'] < 60:
            self.chatToServer("本次测试成绩为：" + str(args['score']))
            self.chatToServer("本次学习成绩未达标哦，让我们回顾一下今天都有哪些知识点吧！")
            commandComp = self.CreateComponent(
                serverApi.GetLevelId(), "Minecraft", "command")
            commandComp.command = "/tp @s 31 66 -166"
            self.NeedsUpdate(commandComp)
            self.NotifyToClient(self.player, "noPassEvent", args)
        # 不及格
        if args['score'] >= 60 and args['score'] <= 80:
            self.chatToServer("本次测试成绩为：" + str(args['score']))
            self.chatToServer("本次学习成绩还不错呢，授予你认真好学的称号！")
            self.chatToServer("游戏结束！")
        # 认真好学
        if args['score'] > 80 and args['score'] <= 90:
            self.chatToServer("本次测试成绩为：" + str(args['score']))
            self.chatToServer("本次学习成绩很棒呢，授予你三好学生的称号！")
            self.chatToServer("游戏结束！")
        # 三好学生
        if args['score'] > 90 and args['score'] <= 100:
            self.chatToServer("本次测试成绩为：" + str(args['score']))
            self.chatToServer("本次学习成绩非常非常棒呢，授予你历史大使的称号！")
            self.chatToServer("游戏结束！")
        # 历史大使

    def attackExtraDataEventHandler(self, args):
        pass
        # 获取narratorid用的回调函数，废弃，已使用完毕
        # levelcomp = self.CreateComponent(
        #     serverApi.GetLevelId(), "Minecraft", "extraData")
        # levelcomp.SetExtraData("narratorPos", None)

    def chatToServer(self, message):
        comp = self.CreateComponent(self.player, "Minecraft", "game")
        comp.SetNotifyMsg(str(message))
        self.NeedsUpdate(comp)

    def retSetNarratorPos(self):
        for i in range(10):
            # logger.info(self.narratorListId[i])
            # logger.info(self.narratorListPosX[i])
            # logger.info(self.narratorListPosY[i])
            # logger.info(self.narratorListPosZ[i])
            posComp = self.CreateComponent(
                self.narratorListId[i], 'Minecraft', 'pos')
            posComp.pos = (
                (self.narratorListPosX[i]), self.narratorListPosY[i], self.narratorListPosZ[i])
            self.NeedsUpdate(posComp)

    def TeacherTextEventHandler(self, args):
        if self.sayBool:
            self.chatToServer("解说员：  " + args['text'])
            self.sayBool = False

    def canAnswerEventHandler(self, args):
        self.chatToServer("接下来给同学们派发一份答卷，同学们记得回家完成哦！")
        commandComp = self.CreateComponent(
            serverApi.GetLevelId(), "Minecraft", "command")
        commandComp.command = "/tp @s 70 68 -119"  # 传送指令
        self.NeedsUpdate(commandComp)
        # 调用答题UI
        self.chatToServer("这次学习之旅就差不多到此结束了呢，来检测一下所学到的东西吧！！")
        self.NotifyToClient(self.player, "answerUIEvent", {})

    def progressEventHandler(self, args):
        logger.info("监听进度成功！！！！！！！！！！！！！！！")
        self.chatToServer("§e"+"已完成"+str(args['val'])+"/10")
