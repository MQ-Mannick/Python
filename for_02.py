print("Su mail debe ser de la forma nombre@gmail.com para seguir")
numero = 0;

while numero != 2:
    miEmail = input("Ingrese su mail: ")
    numero_arroba = 0
    numero_punto = 0
    for arrobas in miEmail:
        if arrobas == "@":
            numero_arroba = numero_arroba + 1
    for puntos in miEmail:
        if puntos == ".":
            numero_punto = numero_punto + 1     
    numero = numero_arroba + numero_punto

if numero == 2:
    print("su gmail es correcto")




















    
  
    


# for i in miEmail:
#     if(i == "@" or i == ".")
#         contador = contador + 1

# if contador == 2:
#     print("email bueno")
# else:
#     print("El email no es correcto")


    

