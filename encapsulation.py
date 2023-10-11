#objektove programovanie
#encapsulation


#atributy a metody
class WizardPlayer:

    def __init__(self, name="anonym", age=0):
            self.name = name
            self.age = age

    def atttack(self):
        print("utok")


    def age_checker(self):
        if self.age >= 18:
            print("mozes hrat")
        else:
            print("mas malo rokov")

#print(WizardPLayer.test_function(60,100))
player1 = WizardPlayer("david", 25)
player1.name = "martin"
player1.attack() = "ahoj"
print(player1.attack)
