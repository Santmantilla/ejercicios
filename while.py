"""
i = 0
while (i<10):
    print(i)
    i += 1
"""
import os
mensajeInicial = 'Desea iniciar la calculadora? S(Si) o Enter(No): '
opcionesMenu = '1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n0. Salir'
while True:
    os.system('clear')
    print(opcionesMenu)
    opcion = int(input('Ingrese una opcion: '))
    match opcion:
        case 1:
            numeroA = int(input('Ingrese el numero A: '))
            numeroB = int(input('Ingrese el numero B: '))
            print(f'EL resultado de la suma entre {numeroA} + {numeroB} es: {numeroA+numeroB}')
            x = bool(input('Quiere seguir en la sesion? S(Si) o Enter(No): '))
            if (x == True):
                continue
            else:
                break
        case 2:
            numeroA = int(input('Ingrese el numero A: '))
            numeroB = int(input('Ingrese el numero B: '))
            print(f'EL resultado de la resta entre {numeroA} - {numeroB} es: {numeroA-numeroB}')
            x = bool(input('Quiere seguir en la sesion? S(Si) o Enter(No): '))
            if (x == True):
                continue
            else:
                break
        case 3:
            numeroA = int(input('Ingrese el numero A: '))
            numeroB = int(input('Ingrese el numero B: '))
            print(f'EL resultado de la multiplicacion entre {numeroA} x {numeroB} es: {numeroA*numeroB}')
            x = bool(input('Quiere seguir en la sesion? S(Si) o Enter(No): '))
            if (x == True):
                continue
            else:
                break
        case 4:
            numeroA = int(input('Ingrese el numero A: '))
            numeroB = int(input('Ingrese el numero B: '))
            print(f'EL resultado de la division entre {numeroA} / {numeroB} es: {numeroA/numeroB}')
            x = bool(input('Quiere seguir en la sesion? S(Si) o Enter(No): '))
            if (x == True):
                continue
            else:
                break
        case 0:
            rta = bool(input('Esta seguro de querer salir de la sesion? S(Si) o Enter(No): '))
            if (rta == True):
                break
            else:
                continue
        case _:
            print('Error, esa opcion no existe.')
