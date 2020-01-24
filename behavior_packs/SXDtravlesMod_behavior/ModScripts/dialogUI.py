# -*- coding: utf-8 -*-

import random
import client.extraClientApi as clientApi
from ModScripts.modTools import logger
import ModScripts.modConfig as modConfig
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class dialogUIScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.TextCount = 0
        self.TextDict = {
            1: "1.戴金面罩青铜人头像\n戴金面罩青铜人头像，整件人头像金光熠熠，气度非凡。\n在中国的考古发现中，四川广汉三星堆遗址是我国迄今发现的最早的大规模青铜人像遗址。\n其中最具代表性的器物就是戴金面罩青铜人头像，它以其特殊的造型以及独具特色的文化内涵驰名中外。",
            2: "2.青铜戴冠纵目面具\n人像仅存上半舟，估计是在入坑前举行某种宗教仪式时坡有意火燎硬砸损所致。\n人像体态端庄抱状构势干胸前型、其所穿对襟插鳙，整个构型力图表现人像的丽。推测这尊人主持者的形苏，神情冷峻肃穆，两臂呈环，双手皆作执握中空的手衣纹饰精丽。",
            3: "3.青铜纵目面具\n青铜纵目面具为三星堆“六大国宝”之一，宽1.38米，高0.645米，眼睛呈柱状向外凸。\n一双雕有纹饰的耳朵向两侧充分展开，造型雄奇，威严四仪，为世界上年代最早，形体最大的青铜面具。\n凸出的眼睛代表了古人对于眼睛的崇拜。",
            4: "4.青铜神树\n三星堆青铜神树是世界上最早、树株最高的青铜神树，也是三星堆镇馆之宝，高384厘米，三簇树枝，每簇三枝、共九枝，上有27果九鸟，树侧有一龙缘树逶迤而下。",
            5: "5.太阳轮\n太阳和太阳神的崇拜，是人类早期共同的文化心理，在世界各地的早期岩画和文物中，有关太阳的图案或其纹饰多得不胜枚举，而这件以青铜的实物形态来表现太阳的却是很少见的，这些太阳轮上均有小孔，估计是要把他们钉挂起来，作为太阳的象征接受人们顶礼膜拜的。",
            6: "6.青铜鸡\n三星堆青铜鸡昂首引颈，尾羽丰满。造型生动，写实性强，铸造工艺精美\n它可能即是古代神话中呼唤日出的”天鸡”的象征物。",
            7: "7.金杖\n三星堆金杖是世界上最早的金杖，长142公分，直径2.3公分，重700多克，上有刻划的人头、鱼鸟纹饰。",
            8: "8.青铜大立人像\n三星堆青铜大立人像是世界上最大、最完整的青铜大立人像，通高262公分，重逾180公斤，被称为铜像之王。",
            9: "9.铜铃\n" +
            "此文物为商代的青铜器，铜铃正面略呈梯形，横断面呈椭圆形，上小下大，两腰微弧，两面中间有一纵脊，凹口，顶部有一半圆形钮。" +
            "铃身两侧有长而薄的翼。现收藏于三星堆博物馆。",
            10: "10.兽面\n三星堆铜兽面是该类型兽面中形制稍小的一件。二号祭祀坑出土。\n兽面呈夔龙形向两面展开，龙尾上卷，长眉直鼻，夔龙形耳朵，双眼硕大，方颐阔口，呲牙咧嘴，形象狰狞诡谲。"
        }

        self._color = ["0", "1", "2", "3", "4", "5", "6",
                       "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        self._textLabelPath = "/bg_img/main_text"
        self._btnText = "/bg_img/btn_next"

    def Create(self):
        pass
    # 界面的一些初始化操作

    def Destroy(self):
        pass

    def Init(self):
        pass

    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def btnNextClick(self, args):
        # logger.info("btnNextClick")
        # self.TextCountAdd()
        # self.ChangeText()
        # logger.info("dialogUI textCount"+str(self.TextCount))
        # if self.TextCount == 10:
        #     logger.info("dialogUI textCount == 10!!!!!!!!!!!!!!!")
        #     # self.NotifyToServer(
        #     #     "canAnswerEvent", args)
        #     self.SetRemove()
        # elif self.TextCount != 10:
        self.SetRemove()

        return ViewRequest.Refresh | ViewRequest.Exit

    def TextCountAdd(self):
        self.TextCount += 1

    def ChangeText(self):
        self.mainText = "点击继续开始学习"
        self.SetText(self._textLabelPath, self.TextDict[self.TextCount])
