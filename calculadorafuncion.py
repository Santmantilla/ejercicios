def calculadora():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    operador = input("Ingrese el operador, sea +,-,*,/: ")
    match operador:
        case "+":            
            return f'El valor de la suma es {numero1+numero2}'
        case "-":
            return f'El valor de la resta es {numero1-numero2}'
        case "*":
            return f'El valor de la multiplicacion es {numero1*numero2}'
        case "/":
            return f'El valor de la division es {numero1/numero2}'
        case _:
            return 'Este operador no existe o no esta incluido.'
        
print(calculadora())
            
    