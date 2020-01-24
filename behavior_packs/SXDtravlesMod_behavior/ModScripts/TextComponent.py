import client.extraClientApi as clientApi
ClientComponentCls = clientApi.GetComponentCls()


class TextComponent(ClientComponentCls):
    def __init__(self, entityId):
        ClientComponentCls.__init__(self, entityId)
        self.text = None

    def getText(self):
        return self.text

    def setText(self, string):
        self.text = str(string)
