lugares_vagos = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Digite o número da sala (1-5) ou 0 para sair: "))
    
    if sala == 0:
        print("Encerrando o programa...")
        break

    if sala < 1 or sala > 5:
        print("Número da sala inválido! Digite um número de 1 a 5.")
        continue
    
    lugares_solicitados = int(input("Digite a quantidade de lugares solicitados: "))
    
    if lugares_solicitados <= lugares_vagos[sala - 1]:
        lugares_vagos[sala - 1] -= lugares_solicitados
        print(f"Venda realizada! Lugares disponíveis na sala {sala}: {lugares_vagos[sala - 1]}")
    else:
        print(f"Não há lugares suficientes disponíveis na sala {sala}. Lugares vagos: {lugares_vagos[sala - 1]}")

print("Programa finalizado.")
