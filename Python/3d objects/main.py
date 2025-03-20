import panda3d

from direct.showbase.ShowBase import ShowBase


class MyApp(ShowBase):
    def __init__(self):
        super().__init__()

        self.scene = self.loader.loadModel("models/enviroment")