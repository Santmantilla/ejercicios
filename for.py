palabra = input('Ingrese una palabra: ')
letra = 0
for i in palabra:
    if(i != " "):
        letra = letra+1
        
print(f'La palabra {palabra} tiene {letra} letras.')