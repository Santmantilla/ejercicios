def NotaProyecto(notaProyecto:int) -> float:
    print(notaProyecto*0.60)

def NotaActividades() -> float:
    notaFinal = 0.0
    sumaNotas = 0
    for i in range(4):
        sumaNotas += int(input(f'Ingrese la nota de la actividad #{i+1}'))
    notaFinal = sumaNotas / 4
    return notaFinal * 0.25

def NotaExamen(nota:int) -> float:
    print(nota*0.15)

def CalculoTotal(nombre:str,notaTotal:int,valorPrograma:int):


NotaProyecto(int(input("Ingrese su nota del proyecto: ")))
NotaExamen(int(input("Ingrese su nota de examen: ")))
NotaActividades()