Mercury = 0.376
Venus = 0.889
Mars = 0.378
Jupiter = 2.36
Saturn = 1.08
Uranus = 0.81
Neptune = 1.14

def main():
    #enter weight on Earth
    weight_on_earth = float(input('Zadaj vahu na Zemi: '))
    #enter planet
    planet = str(input('Zadaj planetu: '))
    
    #weight conversion on other planets
    if planet == 'Mercury':
        converted_weight = weight_on_earth * Mercury
    #round values
        rounded_weight = round(converted_weight, 2)
    #print result
        print("The equivalent weight on",planet,':',rounded_weight)

    elif planet == 'Venus':
        converted_weight = weight_on_earth * Venus
        rounded_weight = round(converted_weight, 2)
        print("The equivalent weight on",planet,':',rounded_weight)

    elif planet == 'Mars':
        converted_weight = weight_on_earth * Mars
        rounded_weight = round(converted_weight, 2)
        print("The equivalent weight on",planet,':',rounded_weight)

    elif planet == 'Jupiter':
        converted_weight = weight_on_earth * Jupiter
        rounded_weight = round(converted_weight, 2)
        print("The equivalent weight on",planet,':',rounded_weight)

    elif planet == 'Saturn':
        converted_weight = weight_on_earth * Saturn
        rounded_weight = round(converted_weight, 2)
        print("The equivalent weight on",planet,':',rounded_weight)

    else:
        print('No planets')

main()
