import client.extraClientApi as clientApi
ClientComponentCls = clientApi.GetComponentCls()


class scoreComponentClient(ClientComponentCls):
    def __init__(self, entityId):
        ClientComponentCls.__init__(self, entityId)
        self.mScoreBool = False
        self.mScore = 0

    def getScoreBool(self):
        return self.mScoreBool

    def setScoreBool(self, bool):
        self.mScoreBool = bool

    def getScore(self):
        return self.mScore

    def setScore(self, num):
        self.mScore = num
