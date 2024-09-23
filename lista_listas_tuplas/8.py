lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [5, 6, 7, 8, 9, 10]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

valores_comuns = conjunto1 & conjunto2
print("Valores comuns às duas listas:", valores_comuns)

valores_somente_primeira = conjunto1 - conjunto2
print("Valores que só existem na primeira lista:", valores_somente_primeira)

valores_somente_segunda = conjunto2 - conjunto1
print("Valores que existem apenas na segunda lista:", valores_somente_segunda)

elementos_unicos = conjunto1 ^ conjunto2
print("Elementos não repetidos das duas listas:", elementos_unicos)

primeira_sem_repetidos = conjunto1 - valores_comuns
print("Primeira lista sem os elementos repetidos na segunda:", primeira_sem_repetidos)
