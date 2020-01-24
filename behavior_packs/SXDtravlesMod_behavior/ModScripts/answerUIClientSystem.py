# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
from ModScripts.modTools import logger
import ModScripts.modConfig as modConfig
clientCls = clientApi.GetClientSystemCls()
comp = clientApi.CreateComponent(
    clientApi.GetLocalPlayerId(), modConfig.ModName, modConfig.scoreComponentClient)


class answerUIClientSystem(clientCls):
    def __init__(self, namespace, systemName):
        clientCls.__init__(self, namespace, systemName)
        self.PlayerId = clientApi.GetLocalPlayerId()
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(
        ), "UiInitFinished", self, self.OnUIInitFinished)
        self.ListenForEvent("SXDtravlesMod",
                            "ServerMain", "chatServerHandler", self, self.chatServerHandler)

    def Update(self):
        if comp.getScoreBool():
            self.NotifyToServer("ScoreEvent", {'score': comp.getScore()})
            comp.setScoreBool(False)
            clientApi.NeedsUpdate(comp)
        # getanswerUI的score
        pass

    def Destory(self):
        pass

    def OnUIInitFinished(self, args):
        pass
        # # TODO  创建ui
        # clientApi.RegisterUI(modConfig.ModName, modConfig.answerUI,
        #                      modConfig.answerUIclsPath, modConfig.answerUIDef)
        # locaUI = clientApi.CreateUI(modConfig.ModName,
        #                             modConfig.answerUI, {"isHud": 1})
        # logger.info("OnUIInitFinished : %s", args)

    def chatServerHandler(self, args):
        if args['message'] == "开始答题":
            clientApi.RegisterUI(modConfig.ModName, modConfig.answerUI,
                                 modConfig.answerUIclsPath, modConfig.answerUIDef)
            locaUI = clientApi.CreateUI(modConfig.ModName,
                                        modConfig.answerUI, {"isHud": 1})
