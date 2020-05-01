print("Programa de verificacion de becas")

edad_postulante = int(input("Ingrese la edad porfavor: "))
puntaje_postulante = int(input("Ingrese el puntaje de tres digitos del postulante porfavor: "))

if 18 <= edad_postulante <= 20 and 800 <= puntaje_postulante <= 850 :
    print("usted obtuvo " + str(puntaje_postulante) +" puntos y su edad es de " + str(edad_postulante) + " años")
    print("Los terminos son correctos, puede postular")
else: 
    
    print("lo siento")



