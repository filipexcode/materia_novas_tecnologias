frase = input("Digite uma frase: ")

contagem_caracteres = {}

for caractere in frase:
    if caractere in contagem_caracteres:
        contagem_caracteres[caractere] += 1
    else:
        contagem_caracteres[caractere] = 1

print(contagem_caracteres)
