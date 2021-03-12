class Time:
    def __init__(self, heure, minutes, secondes):
        self.__heure = heure
        self.__minutes = minutes
        self.__secondes = secondes

    def affiche(self, ):
        print("Heure:", self.__heure, "Minutes:", self.__minutes, "Secondes:", self.__secondes)

    def convert(self):
        return print((self.__heure * 60) + (self.__minutes * 60) + self.__secondes, " secondes")

    def ajout(self, ajout):
        self.__secondes += ajout


temps = Time(21, 45, 25)
temps.affiche()
temps.convert()
temps.ajout(15)
temps.convert()
