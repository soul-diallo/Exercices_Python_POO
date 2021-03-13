class Base:
    def __init__(self):
        self.a = "a"
        self.b = "b"
        self.c = "c"

    def A(self):
        print(self.a)

    def B(self):
        print(self.b)

    def C(self):
        print(self.c)


class Derivee(Base):
    def init(self):
        self.a = "aa"
        super().init()
        self.c = "ce"

    def A(self):
        print(self.a)

    def B(self):
        self.b = "bb"
        super().B()
        print(self.b)


base = Base()
derivee = Derivee()

# Appel de la méthode Base.A() qui affiche l'attribut Base.a initialisé à "a" dans le constructeur
base.A()

# Appel de la méthode Derivee.A() qui affiche l'attribut Derivee.a qui a ete initialisé à "aa" dans le constructeur
# de Derivee. Mais ce constructeur appelle celui de la classe mère après cette initialisation à "aa". Or, celui-ci
# assigne "aa" à l'attribut a. Cette valeur écrase la précédente.
derivee.A()
print()

# Appel de la méthode Base.B() qui affiche l'attribut Base.b, initialisé à "b" dans le constructeur.
base.B()

# La méthode Derivee.B() assigne la valeur "bb" à l'attribut b. Ensuite, elle appelle la méthode du même nom
# de la classe mère, qui affiche l'attribut b. Comme celui-ci a été modifié en "bb" juste avant,
# c'est cette valeur qui est présente dans l'instance de Derivee, c'est donc elle qui est affichée.
# Enfin, la méthode affiche de nouveau l'attribut b.
derivee.B()

# Appel de la méthode Base.C() qui affiche l'attribut Base.c, initialisé à "c" dans le constructeur ,
base.C()

# La classe Derivee ne possède pas de méthode C(), c'est donc celle de la classe Base qui est appelée.
# L'attribut c de l'instance de Derivee est d'abord initialisé  "c" dans la classe de base, mais cette valeur
# est écrasée, dans le constructeur de la classe dérivée, par "cc”.
derivee.C()

derivee = base
# derivee référence désormais la variable base. Cet appel est identique à base.C().
derivee.C()
