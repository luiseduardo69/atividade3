class Ponto:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def setx(self, x):
        self._x = x
        
    def setY(self, y):
        self._y = y    

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def qualQuadrante(self):
        if (self._x > 0  & self._y > 0):
            return 1
        elif (self._x < 0  & self._y > 0):
            return 2
        elif (self._x < 0  & self._y < 0):
            return 3
        elif (self._x > 0  & self._y < 0):
            return 4
        elif (self._x == 0  & self._y ==0):
            return 'Origem'


class Quadrilátero:
    def __init__(self, P2, P1):
        self.P2 = P2 
        #P1 eixo X
        self.P1 = P1
        #P2 eixo Y
     
    def contidoEmQ(self, point):
        if (self.P1 >= point.getY()) & (self.P2 >= point.getX()):
            return True
        else:
            return False