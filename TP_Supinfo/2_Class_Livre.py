class Livre():
    # Ajouter des valeurs par défaut sur les parametre du constructeur pour pouvoir instancier la classe sans mettre de valeur
    def __init__(self, titre="Livre", auteur="Soul", prix=25000, annee=2021):
        self.titre = titre
        self.auteur = auteur
        self.prix = prix
        self.annee = annee

    def afficher(self):
        print("Le titre du livre est ", self.titre)
        print("L'auteur du livre est ", self.auteur)
        print("Le prix du livre est ", self.prix)
        print("L'annee de parution du livre est ", self.annee)


livre1 = Livre("Gang", "OG")
livre1.afficher()
