# for letra in "Python":

#     if letra == "h":
#         continue

#     print("la letra h no está:" + letra)


nombre = "gatos locos"
contador = 0

for i in nombre:

    if i == " ":
        continue
    contador += 1

print(contador)