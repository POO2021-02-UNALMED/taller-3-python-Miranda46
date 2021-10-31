class TV:
    numTV=0
    def __init__(self, marca, estado):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._volumen=1
        self._precio=500
        self.numTV+=1

    def getMarca(self):
        return self._marca
    
    def getControl(self):
        return self._control

    def getPrecio(self):
        return self._precio

    def getVolumen(self):
        return self._volumen

    def getEstado(self):
        return self._estado

    def setMarca(self, marca):
        self._marca=marca
    
    def setControl(self, control):
        self._control=control
    
    def setPrecio(self, precio):
        self._precio=precio

    def setVolumen(self, volumen):
        self._volumen=volumen

    def setEstado(self, estado):
        self._estado=estado

    @staticmethod
    def getNumTV():
        return TV.numTV

    def canalUp(self):
        if self._estado:
            if self._canal<120:
                self._canal+=1

    def canalDown(self):
        if self._estado:
            if self._canal>1:
                self._canal-=1

    def turnOn(self):
        self._estado=True

    def turnOff(self):
        self._estado=False

    def volumenUp(self):
        if self._estado:
            if self._volumen<7:
                self._volumen+=1

    def canalDown(self):
        if self._estado:
            if self._volumen>0:
                self._volumen-=1

    def setCanal(self, canal):
        if canal > 0 and canal < 121:
            if self.tv.estado:
                self.canal=canal






    
