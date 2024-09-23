def verifica_parenteses(expressao):
    
    pilha = []

    
    for caractere in expressao:
       
        if caractere == '(':
            pilha.append(caractere)
      
        elif caractere == ')':
          
            if not pilha:
                return "Erro"
            
            pilha.pop()

    if not pilha:
        return "OK"
    else:
        return "Erro"

expressoes = ["(())", "()()(()())", "( ) )", "((())", "()(()))", ""]

for expressao in expressoes:
    resultado = verifica_parenteses(expressao)
    print(f"Expressão: {expressao} - Resultado: {resultado}")
