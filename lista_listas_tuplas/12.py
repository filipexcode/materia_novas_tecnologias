bobby = {
    "tipo": "cachorro",
    "dono": "Ana"
}

mimi = {
    "tipo": "gato",
    "dono": "Carlos"
}

tweety = {
    "tipo": "pássaro",
    "dono": "Beatriz"
}

lola = {
    "tipo": "coelho",
    "dono": "Marcos"
}

pets = [bobby, mimi, tweety, lola]

for pet in pets:
    print(f"\nInformações sobre o animal de estimação:")
    print(f"  Tipo do animal: {pet['tipo'].capitalize()}")
    print(f"  Nome do dono: {pet['dono']}")
