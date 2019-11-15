class Information:
    def __init__(self, id, posX, posY):
        self.id = id
        self.posX = posX
        self.posY = posY

    def __str__(self):
        return "Id: {}, PosX: {}, PosY: {}".format(str(self.id), str(self.posX), str(self.posY))
