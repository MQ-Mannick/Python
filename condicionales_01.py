

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspendido"
    return valoracion


print("Programa de evaluacion")

nota_alumno=input("introducir nota: ")

print(evaluacion(int(nota_alumno)))



