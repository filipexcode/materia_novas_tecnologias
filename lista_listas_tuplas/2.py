def jogo_forca():

    palavras = ["python", "desenvolvedor", "computador"]

    print("Escolha uma palavra para jogar:")
    for idx, palavra in enumerate(palavras, 1):
        print(f"{idx}. Palavra {idx}")

    escolha = input("Digite o número da palavra escolhida (1, 2 ou 3): ")
    while escolha not in ['1', '2', '3']:
        escolha = input("Escolha inválida. Digite 1, 2 ou 3: ")

    palavra = palavras[int(escolha) - 1]

    letras_adivinhadas = ["_" for _ in palavra]

    tentativas = 6

    letras_tentadas = []

    print("\nBem-vindo ao jogo da Forca!")
    print(f"A palavra tem {len(palavra)} letras.")

    while tentativas > 0 and "_" in letras_adivinhadas:
        print("\nPalavra:", " ".join(letras_adivinhadas))
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras já tentadas: {', '.join(letras_tentadas)}")

        palpite = input("Digite uma letra: ").lower()

        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if palpite in letras_tentadas:
            print("Você já tentou essa letra, tente outra.")
            continue

        letras_tentadas.append(palpite)

        if palpite in palavra:
            print(f"Boa! A letra '{palpite}' está na palavra.")
            for idx, letra in enumerate(palavra):
                if letra == palpite:
                    letras_adivinhadas[idx] = palpite
        else:
            print(f"A letra '{palpite}' não está na palavra.")
            tentativas -= 1

    if "_" not in letras_adivinhadas:
        print("\nParabéns! Você adivinhou a palavra:", palavra)
    else:
        print("\nVocê perdeu! A palavra era:", palavra)


jogo_forca()
