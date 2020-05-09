import random

valores_hex = []
contador = 0

while contador < 6:
        valores_hex.append(str(random.randint(0, 15)))
        contador = contador + 1

for n, i in enumerate(valores_hex):
        if i == "10":
                valores_hex[n] = "A"
        if i == "11":
                valores_hex[n] = "B"
        if i == "12":
                valores_hex[n] = "C"
        if i == "13":
                valores_hex[n] = "D"
        if i == "14":
                valores_hex[n] = "E"
        if i == "15":
                valores_hex[n] = "F"
                
codigo_hex = "#"

for num in valores_hex:
        codigo_hex = codigo_hex + num
print(codigo_hex)
        






