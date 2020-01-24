# -*- coding: utf-8 -*-


import client.extraClientApi as clientApi
from ModScripts.modTools import logger
import ModScripts.modConfig as modConfig
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class answerUIScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.PlayerId = clientApi.GetLocalPlayerId()
        self.TextCount = 0
        self.score = 0
        self._textLabelPath = "/bg_img/main_text"
        self.problemsText = {
            1: "铜铃是商代的文物吗？",
            2: "青铜鸡是古代神话中呼唤日出的”天鸡”的象征物吗？",
            3: "以下说法请判断对错\n三星堆青铜神树不是世界上最早、树株最高的青铜神树 ",
            4: "三星堆青铜大立人像被称为铜像之王吗？",
            5: "青铜纵目面具不是为世界上年代最早，形体最大的青铜面具。",
            6: "青铜戴冠纵目面具是完整的。",
            7: "太阳是轮作为太阳的象征接受人们顶礼膜拜的。",
            8: "兽面是二号祭祀坑出土的？",
            9: "以下说法请判断对错\n三星堆金杖不是世界上最早的金杖。",
            10: "戴金面罩青铜人头像是四川广汉三星堆遗址是我国迄今发现的最早的大规模青铜人像遗址出土的？"
        }

    def Create(self):
        pass

    def Destroy(self):
        logger.info("DESTORY——————————————————————————————————")
        comp = clientApi.CreateComponent(
            clientApi.GetLocalPlayerId(), modConfig.ModName, modConfig.scoreComponentClient)
        comp.setScoreBool(True)
        comp.setScore(self.score)
        clientApi.NeedsUpdate(comp)
        self.score = 0

    def Init(self):
        pass

    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def btnYesClick(self, args):
        #   logger.info("btnYesClick Up")
        # switch
        if self.getTextCount() == 1:
            self.score += 10
        if self.getTextCount() == 2:
            self.score += 10
        if self.getTextCount() == 4:
            self.score += 10
        if self.getTextCount() == 7:
            self.score += 10
        if self.getTextCount() == 8:
            self.score += 10
        if self.getTextCount() == 10:
            self.score += 10
        self.TextCountAdd()
        self.ChangeProblemsText()
        if self.TextCount == 10:
            # self.NotifyToServer("scoreEvent", {'score': self.score})
            self.SetRemove()
        return ViewRequest.Refresh | ViewRequest.Exit

    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def btnNoClick(self, args):
        #logger.info("btnNoClick Up")
        # switch
        if self.getTextCount() == 3:
            self.score += 10
        if self.getTextCount() == 5:
            self.score += 10
        if self.getTextCount() == 6:
            self.score += 10
        if self.getTextCount() == 9:
            self.score += 10
        self.TextCountAdd()
        self.ChangeProblemsText()
        if self.TextCount == 10:
            #self.NotifyToServer("scoreEvent", {'score': self.score})
            self.SetRemove()
        return ViewRequest.Refresh | ViewRequest.Exit

    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def btnContinueClick(self, args):
        self.SetVisible("/bg_img/btn_no", True)
        self.SetVisible("/bg_img/btn_yes", True)
        self.SetVisible("/bg_img/btn_continue", False)

    def ChangeProblemsText(self):
        self.SetText(self._textLabelPath, self.problemsText[self.TextCount])

    def TextCountAdd(self):
        self.TextCount += 1
        if self.TextCount == 10:
            pass

    def getTextCount(self):
        return self.TextCount

    def getScore(self):
        return self.score
