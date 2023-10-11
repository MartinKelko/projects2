#objektove programovanie

#atributy a metody
class WizardPlayer:

    def __ init __(self, name="anonym", age=0):
        self.name = name
        self.age = age

    def atttack(self):
        print("utok")


    def age_checker(self):
        if self.age >= 18:
            print("mozes hrat")
        else:
            print("mas malo rokov")

            
user_name = input("ake je tvoje meno")
user_age = int(input("kolko mas rokov"))

player1 = WizardPlayer(user_name, user_age)
print(player1.wizard_club)

player1.attack()
player1.attack()
player1.attack()
player1.age_checker()
