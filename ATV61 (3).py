def inverter_string(texto):
    return texto[::-1]


textos = [
    "python2023",
    "0203programacao2023",
    "luz azul",
    "arara rara",
    "anotaram a data da maratona"
]

letras = ["a", "b", "c", "d", "e"]

for i in range(len(textos)):
    print(f"{letras[i]}. '{textos[i]}' invertida fica '{inverter_string(textos[i])}'")
