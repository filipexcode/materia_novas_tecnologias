
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8,
3, 3,-52]

media = sum(lista) / len(lista)

print(max(lista))

print(min(lista))

numeros_pares = [num for num in lista if num % 2 == 0]
print(numeros_pares)

primeiro_elemento = lista[0]
ocorrencias_primeiro = lista.count(primeiro_elemento)
print(ocorrencias_primeiro)

print(media)

soma_negativos = sum(num for num in lista if num < 0)
print(soma_negativos)