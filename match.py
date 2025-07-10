genero = input("Ingrese genero: ")

match genero: 
    case 'm':
        print("Masculino")

    case 'f':
        print("Femenino")
    case _:
        print("Otro")