class WizardPlayer:

    def __ init__(self, name="anonym", age=0):
            self.name = name
            self.age = age

    def atttack(self):
        return "utok 1. stupna"


class HeadWizard(WizardPlayer):

    def __init__(self,type, name, age):
        super().__init__(name, age)
        self.type = type

    def atttack(self):
        return "utok 2. stupna"

    def avada_kedavra(self):
        return "Avada Kedavra"

player1 = WizardPlayer("david", 25)
print(player1.attack())

print("-----------------------")

player2 = HeadWizard("good","david", 35)
print(player2.type)
print(player2.name)
print(player2.age)

#introspection/Dunder Methods
print(dir(player2))
print("-----------------------")
print([player2.__dir__())

#rovnaky zapis
print(len([5,8,9]))
print("-----------------------")
print([5,8,9].__len__())

#rovnaky zapis
print(str(player2))
print("-----------------------")
print(player2.__str__())

#method resolution order = MRO
print(HeadWizar.mro())


print("-----------------------")

#isinstance
print(isinstance(player1, WizardPlayer))
print(isinstance(player1, HeadWizard))
print(isinstance(player2, HeadWizard))
