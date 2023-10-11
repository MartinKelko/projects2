class Auto:
    wheels = 0

    def set_wheels(self, number_of_wheels):
        Auto.wheels = number_of_wheels

    def get_wheels(self) -> int:
        return Auto.wheels

# Create an instance of the class
my_auto = Auto()

# Set the number of wheels using the set_wheels method
my_auto.set_wheels(4)

# Get the number of wheels using the get_wheels method
pocet_kolies = my_auto.get_wheels()
print(pocet_kolies) # Output: 4
