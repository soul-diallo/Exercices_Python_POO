class Domino:
    def __init__(self, faceA=0, faceB=0):
        self.faceA = faceA
        self.faceB = faceB

    def affiche_points(self,):
        return print("Face A = ", self.faceA, "  Face B = ", self.faceB)

    def valeur(self):
        return print(self.faceA + self.faceB)


d1 = Domino(2, 6)
d2 = Domino(4,3)
d1.affiche_points()
d1.valeur()

