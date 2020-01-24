# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
from ModScripts.modTools import logger
import ModScripts.modConfig as modConfig
clientCls = clientApi.GetClientSystemCls()

levelId = clientApi.GetLevelId()


class dialogUIClientSystem(clientCls):
    def __init__(self, namespace, systemName):
        clientCls.__init__(self, namespace, systemName)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(
        ), "UiInitFinished", self, self.OnUIInitFinished)
        self.ListenForEvent("SXDtravlesMod",
                            "ServerMain", "AttakEventTest", self, self.AttakEventTestHandler)
        self.ListenForEvent("SXDtravlesMod",
                            "ServerMain", "chatServerHandler", self, self.chatServerHandler)
        self.ListenForEvent("SXDtravlesMod",
                            "ServerMain", "answerUIEvent", self, self.answerUIEventHandler)

    def Create(self):
        pass
        # comp = CreateComponent(
        #     clientApi.GetLocalPlayerId(), "Minecraft", "operation")
        # # 不响应屏幕拖动
        # comp.SetCanDrag(False)
        # self.NeedsUpdate(comp)

    def Update(self):
        pass

    def Destory(self):
        pass

    def AttakEventTestHandler(self, args):
        pass
        # comp = self.CreateComponent(args['playerId'], "Minecraft", "item")
        # carriedData = comp.GetCarriedItem()
        # if carriedData['itemId'] == 260:
        #     self.NotifyToServer("attackExtraDataEvent", args)

    def chatServerHandler(self, args):
        if args['message'] == "开始学习":
            clientApi.RegisterUI(modConfig.ModName, modConfig.dialogUI,
                                 modConfig.dialogUIclsPath, modConfig.dialogUIDef)
            locaUI = clientApi.CreateUI(modConfig.ModName,
                                        modConfig.dialogUI, {"isHud": 0})

    def OnUIInitFinished(self, args):
        pass
        # self.NotifyToServer("ScoreEvent", args)
        # # TODO  创建ui
        # clientApi.RegisterUI(modConfig.ModName, modConfig.dialogUI,
        #                      modConfig.dialogUIclsPath, modConfig.dialogUIDef)
        # locaUI = clientApi.CreateUI(modConfig.ModName,
        #                             modConfig.dialogUI, {"isHud": 1})
        # logger.info("OnUIInitFinished : %s", args)

    def noResposeAttack(self):
        logger.info("noResposeAttack")
        # Attackcomp = self.CreateComponent(
        #     clientApi.GetLocalPlayerI(), "Minecraft", "operation")
        # # 不响应攻击
        # Attackcomp.SetCanAttack(False)
        # self.NeedsUpdate(Attackcomp)

    def answerUIEventHandler(self):
        clientApi.RegisterUI(modConfig.ModName, modConfig.dialogUI,
                             modConfig.dialogUIclsPath, modConfig.dialogUIDef)
        locaUI = clientApi.CreateUI(modConfig.ModName,
                                    modConfig.dialogUI, {"isHud": 0})
