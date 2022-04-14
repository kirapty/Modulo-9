

def menu():

    print("***************")
    print("***************")
    print("MODULO #9/SWAPI")
    print("***************")
    print("***************")

while True:

    print()
    print("A) ¿En cuántas películas aparecen planetas cuyo clima sea árido?: ")
    print()
    print("B) ¿Cuántos Wookies aparecen en la sexta película?: ")
    print()
    print("C) ¿Cuál es el nombre de la aeronave más grande en toda la saga?: ")
    print()
    opcion = input("Que respuestas deseas ver? ESTAS RESPUESTAS SON GRACIAS A SWAPI: ")
    print()
    if opcion == 'a':
        print()
        print("Nombre del planeta: Tatooine. ")
        print("Aparece en la pelicula 1, 3 , 4 , 5 , 6. ")
        print("SWAPI: planets/1/")
        print()
        opcion = input("DESEAS CERRAR EL PROGRAMA?? Y/N: ")
        if opcion == 'y':
            break
        elif opcion == 'n':
            continue
        else:
            print("OPCION INVALIDA. YO SOY TU PADRE...")
                
    elif opcion == 'b':
        print()
        print("Nombre de la especie: Wookies")
        print("En la sexta pelicula aparecen: 1 wookie")
        print("SWAPI: species/3/ o films/6/")
        print()
        
        opcion = input("DESEAS CERRAR EL PROGRAMA?? Y/N: ")
        if opcion == 'y':
            break
        elif opcion == 'n':
            continue
        else:
            print("OPCION INVALIDA. YO SOY TU PADRE...")
    elif opcion == 'c':
        print()
        print("La aeronave mas grande de toda la saga es: La estrella de la muerte")
        print("Tiene una longitud de: 120000")
        print("SWAPI: starships/9/")
        print()

        opcion = input("DESEAS CERRAR EL PROGRAMA?? Y/N: ")
        if opcion == 'y':
            break
        elif opcion == 'n':
            continue
        else:
            print("OPCION INVALIDA. YO SOY TU PADRE...")

