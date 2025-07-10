""" def sumar(a, b):
    return a+b

resultado = sumar(5,8)
print(resultado) """
from typing import Optional

def buscar_elemento(lista: list[int], valor: int) -> Optional[int]:
    if valor in lista:
        return lista.index(valor)
    return None

valores = [1,4,5,7]
print(buscar_elemento(valores,4))