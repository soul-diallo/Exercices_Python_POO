import math


class Cercle:
    pi = 3.14159

    def __init__(self, rayon, absCentre, ordCentre):
        self.__rayon = abs(rayon)
        self.__absCentre = absCentre
        self.__ordCentre = ordCentre

    def aire(self):
        return self.pi * self.__rayon ** 2

    def perimetre(self):
        return 2 * self.pi * self.__rayon

    def __str__(self):
        return "Rayon: {}; Abscisse: {}; Ordonée: {}".format(self.__rayon, self.__absCentre, self.__ordCentre)

    def setRayon(self, rayon):
        self.__rayon = rayon

    def setAbsCentre(self, absCentre):
        self.__absCentre = absCentre

    def setOrdCentre(self, ordCentre):
        self.__ordCentre = ordCentre

    def getRayon(self):
        return self.__rayon

    def getAbsCentre(self):
        return self.__absCentre

    def getOrdCentre(self):
        return self.__ordCentre

    def interieurCercle(self, absPoint, ordPoint):
        if math.sqrt((absPoint - self.__absCentre) ** 2 + (ordPoint - self.__ordCentre) ** 2) < self.__rayon:
            return True
        else:
            return False


cerc = Cercle(0, 0, 0)
cerc.setRayon(6)
cerc.setAbsCentre(4)
cerc.setOrdCentre(3)

print(cerc)
print(cerc.aire())
print(cerc.perimetre())
print(cerc.interieurCercle(5,1))
