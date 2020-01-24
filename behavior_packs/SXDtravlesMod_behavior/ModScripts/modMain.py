from common.mod import Mod
import client.extraClientApi as clientApi
import server.extraServerApi as serverApi
import ModScripts.modConfig as modConfig
from ModScripts.modTools import logger


@Mod.Binding(name=modConfig.ModName, version=modConfig.ModVersion)
class SXDtravlesMod(object):
    def __init__(self):
        pass

    @Mod.InitServer()
    def init_server(self):
        logger.info(
            '\n\n##########===============---------->>>>>  Server initializing.          <<<<<----------===============##########\n\n')

        serverApi.RegisterSystem(
            modConfig.ModName, modConfig.ServerMain, modConfig.ServerMainclsPath)
        logger.info(
            '\n\n##########===============---------->>>>>  Server initialized.           <<<<<----------===============##########\n\n')

    @Mod.DestroyServer()
    def destroy_server(self):
        logger.info(
            '\n\n##########===============---------->>>>>  Server destroyed.             <<<<<----------===============##########\n\n')

    @Mod.InitClient()
    def init_client(self):
        logger.info(
            '\n\n##########===============---------->>>>>  Client component registering. <<<<<----------===============##########\n\n')

        clientApi.RegisterComponent(
            modConfig.ModName, modConfig.scoreComponentClient, modConfig.scoreComponentClientclsPath)
        clientApi.RegisterComponent(
            modConfig.ModName, modConfig.TextComponent, modConfig.TextComponentclsPath)

        logger.info(
            '\n\n##########===============---------->>>>>  Client component registered.  <<<<<----------===============##########\n\n')

        logger.info(
            '\n\n##########===============---------->>>>>  Client initializing.          <<<<<----------===============##########\n\n')
        clientApi.RegisterSystem(
            modConfig.ModName, modConfig.ClientMain, modConfig.ClientMainclsPath)

        # dialogUI
        clientApi.RegisterSystem(
            modConfig.ModName, modConfig.dialogUI, modConfig.dialogUIClientSystemclsPath)
        # answerUI
        clientApi.RegisterSystem(
            modConfig.ModName, modConfig.answerUI, modConfig.answerUIClientSystemclsPath)
        logger.info(
            '\n\n##########===============---------->>>>>  Client initialized.           <<<<<----------===============##########\n\n')

    @Mod.DestroyClient()
    def destroy_client(self):
        logger.info(
            '\n\n##########===============---------->>>>>  Client destroyed.             <<<<<----------===============##########\n\n')
