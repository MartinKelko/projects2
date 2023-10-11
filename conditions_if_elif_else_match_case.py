size = int(input("zadaj velk tricka:"))

if size <= 46:
    print("S")
else:
    if size <= 50:
        print("M")
    else:
        if size <= 54:
            print("L")
        else:
            if size > 54:
                print("XL")


size = int(input("zadaj velk tricka:"))

if size <= 46:
    print("S")
elif size <= 50:
    print("M")
elif size <= 54:
    print("L")
elif size <= 54:
    print("XL")
elif size > 56:
    print("XXL")

########################
    
def tricka(size):
    if size <= 46:
        print("S")
    elif size <= 50:
        print("M")
    elif size <= 54:
        print("L")
    elif size <= 54:
        print("XL")
    else:
        print("tlstoch")

tricka(65)
tricka(32)
tricka(54)
tricka(48)
tricka(53)

###################
def jab(sezona):
    if sezona == 'zima':
        stav = 'spi'
    elif sezona == 'jar':
        stav = 'kvitne'
    elif sezona == 'leto':
        stav = 'zreje'
    elif sezona == 'jesen':
        stav = 'plodi'
    else:
        return 'zla sezona: {sezona}'
    return f'ak je {sezona}, jablon {stav}'

print(f"{jab('jar')}\n{jab('jesen')}\n{jab('neviem')}")

####################
def jab(sezona):
    match sezona:
        case 'zima': stav = 'spi'
        case 'jar': stav = 'kvitne'
        case 'leto': stav = 'zreje'
        case 'jesen': stav = 'plodi'
        case _:
            return f'zla sezona: {sezona}'

print(f"{jab('jar')}\n{jab('jesen')}\n{jab('neviem')}")




