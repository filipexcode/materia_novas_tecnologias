versao_inicial = [1, 2, 3, 4, 5]
versao_alterada = [3, 4, 5, 6, 7]

conjunto_inicial = set(versao_inicial)
conjunto_alterado = set(versao_alterada)

elementos_iguais = conjunto_inicial & conjunto_alterado

novos_elementos = conjunto_alterado - conjunto_inicial

elementos_removidos = conjunto_inicial - conjunto_alterado

print("Elementos que não mudaram:", list(elementos_iguais))
print("Novos elementos:", list(novos_elementos))
print("Elementos removidos:", list(elementos_removidos))
