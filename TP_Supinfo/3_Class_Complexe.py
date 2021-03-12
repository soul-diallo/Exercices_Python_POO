class Complex:
    def __init__(self, x=0, y=0, i=-1, z=0):
        self.x = x
        self.y = y
        self.z = x + i * y

    def afficher(self):
        print(self.z)


nbr = Complex(3, 5)
nbr.afficher()
