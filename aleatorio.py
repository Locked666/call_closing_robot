import random
apelidos_carinho = [
    "meu bem",
    "gata",
    "flor",
    "meu anjo",
    "linda",
    "meu amor",
    "fofa",
    "princesa",
    "meu raio de sol",
    "querida",
    "doçura",
    "estrela",
    "bebê",
    # "mozão",
    "fofinha",
    "meu coração",
    "meu chamego",
    "paixão",
    "meu docinho",
    "luz da minha vida"
]


def aleatorio():
    return random.choice(apelidos_carinho)

print("---"*20)
print(f"Será usado hoje:\n {aleatorio().capitalize()}\n")
print("---"*20)
