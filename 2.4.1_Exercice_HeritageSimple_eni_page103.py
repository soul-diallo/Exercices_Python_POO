class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translation(self, a, b):
        self.x += a
        self.y += b

    # Afin d'avoir un affichage "propre" d'un point
    def __str__(self):
        return "X: {}; Y: {}".format(self.x, self.y)


class Point3D(Point2D):
    def __init__(self, x, y, z):
        # Initialisation des coordonnées x et du point y via le constructeur de Point2D: pas d'accès direct ici.
        super(Point3D, self).__init__(x, y)
        self.z = z

    # Une translation en 3D suit le meme principe qu'une translation en 2D
    def translation(self, x, y, z):
        # On réutilise donc la méthode de Point2D: pas d'accès direct ici non plus.
        super().translation(x, y)
        # Et on y ajoute le traitement spécifique aux points 3D
        self.z += z

    def __str__(self):
        _2d = super().__str__()
        return "{}; Z = {}".format(_2d, self.z)
