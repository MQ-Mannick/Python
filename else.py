email = input("Introduce tu email: ")

for i in email:

    if i == "@":
        arroba = True
        break; # en cuanto encuentre la arroba el break; hace que siga con el bucle for, se sale

else: 
    arroba = False


print(arroba)