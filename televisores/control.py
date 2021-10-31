class Control:

    def __init__(self):
        self.tv=None
    
    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()

    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOn()

    def volumenUp(self):
        self.tv.volumenUp()

    def canalDown(self):
        self.tv.volumenDown()

    def getTV(self):
        return self.tv

    def setTV(self, tv):
        self.tv=tv

    def enlazar(self, tv):
        self.tv=tv
        tv._control=self

    def setCanal(self, canal):
        if canal > 0 and canal < 121:
            if self.tv.estado:
                self.canal=canal
