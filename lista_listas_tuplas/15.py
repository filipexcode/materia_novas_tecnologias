agenda = []

def grava():
    with open("agenda.txt", "w") as file:
        for contato in agenda:
            linha = f"{contato['nome']}|{contato['telefone']}|{contato['tipo_telefone']}|{contato['email']}|{contato['aniversario']}\n"
            file.write(linha)
    print("Agenda gravada com sucesso!")

def le():
    global agenda
    try:
        with open("agenda.txt", "r") as file:
            agenda = []
            for linha in file:
                nome, telefone, tipo_telefone, email, aniversario = linha.strip().split("|")
                agenda.append({
                    "nome": nome,
                    "telefone": telefone,
                    "tipo_telefone": tipo_telefone,
                    "email": email,
                    "aniversario": aniversario
                })
        print("Agenda carregada com sucesso!")
    except FileNotFoundError:
        print("Arquivo de agenda não encontrado. Criando uma nova agenda.")

def lista():
    if not agenda:
        print("Agenda vazia.")
    else:
        print("Lista de contatos:")
        for idx, contato in enumerate(agenda):
            print(f"{idx+1}: Nome: {contato['nome']}, Telefone: {contato['telefone']} ({contato['tipo_telefone']}), Email: {contato['email']}, Aniversário: {contato['aniversario']}")

def apaga():
    nome = input("Digite o nome do contato a ser apagado: ").strip()
    for idx, contato in enumerate(agenda):
        if contato['nome'].lower() == nome.lower():
            del agenda[idx]
            print(f"Contato '{nome}' apagado com sucesso.")
            return
    print(f"Contato '{nome}' não encontrado.")

def altera():
    nome = input("Digite o nome do contato a ser alterado: ").strip()
    for contato in agenda:
        if contato['nome'].lower() == nome.lower():
            print(f"Alterando dados do contato '{nome}':")
            contato['telefone'] = input("Novo telefone: ")
            contato['tipo_telefone'] = input("Novo tipo de telefone (celular, fixo, residência, trabalho): ").lower()
            contato['email'] = input("Novo email: ")
            contato['aniversario'] = input("Nova data de aniversário (dd/mm/aaaa): ")
            print(f"Dados do contato '{nome}' alterados com sucesso.")
            return
    print(f"Contato '{nome}' não encontrado.")

def adicionar():
    nome = input("Nome: ").strip()
    for contato in agenda:
        if contato['nome'].lower() == nome.lower():
            print("Erro: Contato com o mesmo nome já existe na agenda.")
            return
    
    telefone = input("Telefone: ").strip()
    tipo_telefone = input("Tipo de telefone (celular, fixo, residência, trabalho): ").strip().lower()
    email = input("Email: ").strip()
    aniversario = input("Data de aniversário (dd/mm/aaaa): ").strip()
    
    agenda.append({
        "nome": nome,
        "telefone": telefone,
        "tipo_telefone": tipo_telefone,
        "email": email,
        "aniversario": aniversario
    })
    print(f"Contato '{nome}' adicionado com sucesso.")

def ordenar():
    agenda.sort(key=lambda contato: contato["nome"].lower())
    print("Agenda ordenada por nome.")

def menu():
    while True:
        print("\n===== Menu Principal =====")
        print(f"Total de contatos na agenda: {len(agenda)}")
        print("1. Listar contatos")
        print("2. Adicionar novo contato")
        print("3. Alterar contato existente")
        print("4. Apagar contato")
        print("5. Ordenar agenda por nome")
        print("6. Gravar agenda em arquivo")
        print("7. Ler agenda de arquivo")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            lista()
        elif opcao == "2":
            adicionar()
        elif opcao == "3":
            altera()
        elif opcao == "4":
            apaga()
        elif opcao == "5":
            ordenar()
        elif opcao == "6":
            grava()
        elif opcao == "7":
            le()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

le()  
menu()  
