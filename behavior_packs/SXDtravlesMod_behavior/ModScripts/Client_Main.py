# -*- coding: utf-8 -*-
import ModScripts.modConfig as modConfig
import client.extraClientApi as clientApi
from ModScripts.modTools import logger
clientCls = clientApi.GetClientSystemCls()


class MainClientSystem(clientCls):

    def __init__(self, namespace, systemName):
        clientCls.__init__(self, namespace, systemName)
        self.timeTick = 0
        self.timeCount = 0
        self.PlayerEnterBool = False
        self.canGoAnswerBool = False
        self.sayBool = True
        self.teacherCanAnswerBool = True
        self.narratorSayListBool = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.TeacherTextList = {
            1: " 著名先秦史学者李学勤先生评价：“如果没有巴蜀文化的深入研究，便不能构成中国文明起源和发展的完整图景……中国文明研究中的不少问题，恐怕必须由巴蜀文化求得解决。",
            2: "而三星堆，则是巴蜀文化研究的核心之所在。三星堆发现的90年来，巴蜀考古成就斐然，这让曾经扑朔迷离的古巴蜀历史得以逐渐廓清其本来的面目。",
            3: "三星堆遗址位于广汉市南兴镇鸭子河南岸，最早发现于1929年燕家院子，并自20世纪30年代开始，华西协合大学古物博物馆、四川省博物馆、四川大学历史学系、四川省文物考古研究院等单位先后进行了多次调查和发掘。",
            4: "1986年发现了两个祭祀坑，出土青铜人头像、青铜大立人、青铜神树、金杖、玉璋等数百件国家一级文物，震惊世界。全国、全世界众多专家学者关注于此，围绕三星堆以及古蜀文明、巴蜀文明的研究持续不断，高潮迭起。",
            5: "近年来，四川省委省政府更是将围绕三星堆的保护、研究和利用工作，纳入到文化和旅游融合发展、文物保护利用改革、古蜀文明传承发展、世界文化遗产申报等工程的核心项目予以强力推动。国家文物局也在考古发掘、大遗址保护、博物馆建设等方面给予了大力支持。",
            6: "三星堆发现以来的90年历程，是一代代学人披荆斩棘、上下求索、砥砺前行的历程，是拨开四川远古重重迷雾、重建四川古代巴蜀历史、建构中华文明多元一体发展进程的历程，更是打造巴蜀文明金色名片、见证巴蜀文明从盆地走向世界的辉煌历程。"
        }
        self.narratorListId = ['-2190433320959', '-2190433320958', '-2190433320957', '-2190433320956',
                               '-2190433320955', '-2190433320954', '-2190433320953', '-2190433320952', '-2190433320951', '-2190433320950']
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

        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(
        ), "ApproachEntityClientEvent", self, self.ApproachEntityClientEventHandler)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(
        ), "LeaveEntityClientEvent", self, self.LeaveEntityClientEventHandler)
        self.ListenForEvent("SXDtravlesMod",
                            "ServerMain", "noPassEvent", self, self.noPassEventHandler)
        self.ListenForEvent("SXDtravlesMod",
                            "ServerMain", "answerUIEvent", self, self.answerUIEventHandler)

    def Update(self):
        self.timeTick += 1
        if self.canGoAnswerBool:
            logger.info("可以答题")
            self.NotifyToServer(
                "canAnswerEvent", {})
            self.canGoAnswerBool = False

        # if self.narratorSayListBool.count(1) == 10:
        #     self.canGoAnswerBool = True
        #     logger.info("执行canGoAnswerBool == True")
        #     self.teacherCanAnswerBool = False
        #     clientApi.GetUI(
        #         modConfig.ModName, modConfig.dialogUI).setRemove()
        if self.timeTick >= 1500+3600:
            if self.timeTick % 1800 == 0:
                self.timeCount += 1
                if self.timeCount == 6:
                    self.timeCount = 1
                if clientApi.GetUI(
                        modConfig.ModName, modConfig.dialogUI) == None and self.teacherCanAnswerBool:
                    clientApi.RegisterUI(modConfig.ModName, modConfig.dialogUI,
                                         modConfig.dialogUIclsPath, modConfig.dialogUIDef)
                    locaUI = clientApi.CreateUI(modConfig.ModName,
                                                modConfig.dialogUI, {"isHud": 1})
                    locaUI.SetText("/bg_img/main_text",
                                   "老师：  "+self.TeacherTextList[self.timeCount])

    def Destroy(self):
        pass
#############################################################################################################################

    def ApproachEntityClientEventHandler(self, args):
        # logger.info("ApproachEntityClientEventHandler_________")
        for i in range(10):
            if args['entityId'] == self.narratorListId[i]:
                # logger.info(self.TextDict[i + 1])
                if self.narratorSayListBool.count(1) == 10:
                    self.canGoAnswerBool = True
                    logger.info("执行canGoAnswerBool == True")
                    self.teacherCanAnswerBool = False
                    clientApi.GetUI(
                        modConfig.ModName, modConfig.dialogUI).setRemove()

                if clientApi.GetUI(
                        modConfig.ModName, modConfig.dialogUI) == None:
                    # comp = CreateComponent(
                    #     clientApi.GetLocalPlayerId(), "Minecraft", "operation")
                    # # 不响应屏幕拖动
                    # comp.SetCanDrag(False)
                    # self.NeedsUpdate(comp)
                    clientApi.RegisterUI(modConfig.ModName, modConfig.dialogUI,
                                         modConfig.dialogUIclsPath, modConfig.dialogUIDef)
                    locaUI = clientApi.CreateUI(modConfig.ModName,
                                                modConfig.dialogUI, {"isHud": 1})
                    locaUI.SetText("/bg_img/main_text",
                                   self.TextDict[i + 1])
                    self.narratorSayListBool[i] = 1
                    logger.info(self.narratorSayListBool)
                    logger.info(self.narratorSayListBool.count(1))
                    self.NotifyToServer(
                        "progressEvent", {'val': self.narratorSayListBool.count(1)})
                    self.NotifyToServer(
                        "TeacherTextEvent", {"text": self.TextDict[i + 1]})

    def LeaveEntityClientEventHandler(self, args):
        for i in range(10):
            if args['entityId'] == self.narratorListId[i]:
                logger.info("player away" + self.narratorListId[i])
                if self.narratorSayListBool.count(1) == 10:
                    self.canGoAnswerBool = True
                    logger.info("执行canGoAnswerBool == True")
                    self.teacherCanAnswerBool = False
                    clientApi.GetUI(
                        modConfig.ModName, modConfig.dialogUI).setRemove()

    def getPlayerPos(self):
        comp = self.CreateComponent(
            clientApi.GetLocalPlayerId(), "Minecraft", "pos")
        pos = comp.GetPos()
        self.NeedsUpdate(comp)
        return list(pos)

    def noPassEventHandler(self, args):
        for i in range(10):
            self.narratorSayListBool[i] = 0
            self.teacherCanAnswerBool = True
        logger.info("重置解说员交互")

    def answerUIEventHandler(self, args):
        self.teacherCanAnswerBool = False
        clientApi.RegisterUI(modConfig.ModName, modConfig.answerUI,
                             modConfig.answerUIclsPath, modConfig.answerUIDef)
        locaUI = clientApi.CreateUI(modConfig.ModName,
                                    modConfig.answerUI, {"isHud": 1})

    def goAnswer(self):
        pass
