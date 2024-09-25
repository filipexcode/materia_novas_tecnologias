def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True
    
    for col in range(3):
        if tabuleiro[0][col] == jogador and tabuleiro[1][col] == jogador and tabuleiro[2][col] == jogador:
            return True
    
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    
    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

jogador_atual = "X"
jogo_ativo = True

while jogo_ativo:
    imprimir_tabuleiro(tabuleiro)
    print(f"\nVez do jogador {jogador_atual}.")
    
    try:
        linha = int(input("Escolha a linha (1, 2 ou 3): ")) - 1
        coluna = int(input("Escolha a coluna (1, 2 ou 3): ")) - 1
    except ValueError:
        print("Entrada inválida! Por favor, digite números de 1 a 3.")
        continue
    
    if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
        print("Posição inválida! Escolha números de 1 a 3 para linha e coluna.")
    elif tabuleiro[linha][coluna] != " ":
        print("Posição já ocupada! Escolha outra.")
    else:
        tabuleiro[linha][coluna] = jogador_atual
        
        if verificar_vencedor(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"\nParabéns, jogador {jogador_atual}! Você venceu!")
            jogo_ativo = False
        elif verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("\nO jogo terminou em empate!")
            jogo_ativo = False
        else:
            jogador_atual = "O" if jogador_atual == "X" else "X"

print("Obrigado por jogar!")
