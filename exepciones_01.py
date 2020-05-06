def divide():
    while True:
        try:
            op1 = (float(input("introduce el primer numero: ")))
            op2 = (float(input("introduce el segundo numero: ")))
            print("La division es: " + str(op1/op2))
            break

        except ValueError:
            print("//-INTRODUCE VALORES VALIDOS PORFAVOR-//")
        except ZeroDivisionError:
            print("No se puede dividir entre 0!")
        finally:
            print("calculo finalizado")


divide()