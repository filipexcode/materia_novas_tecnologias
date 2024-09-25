pessoa_1 = {
    "first_name": "João",
    "last_name": "Oliveira",
    "age": 35,
    "city": "Rio de Janeiro"
}

pessoa_2 = {
    "first_name": "Maria",
    "last_name": "Silva",
    "age": 28,
    "city": "São Paulo"
}

pessoa_3 = {
    "first_name": "Carlos",
    "last_name": "Santos",
    "age": 40,
    "city": "Belo Horizonte"
}

people = [pessoa_1, pessoa_2, pessoa_3]

for pessoa in people:
    print(f"\nInformações sobre {pessoa['first_name']} {pessoa['last_name']}:")
    print(f"  Primeiro nome: {pessoa['first_name']}")
    print(f"  Sobrenome: {pessoa['last_name']}")
    print(f"  Idade: {pessoa['age']}")
    print(f"  Cidade: {pessoa['city']}")
