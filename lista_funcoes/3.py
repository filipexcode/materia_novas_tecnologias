def cpf(n,d):
    cpf = n
    
    # Tratamento de excessão para não informar todos os dados de erro ao usuário(Excessão tratada)
    try:
        if len(cpf) != 9:
            raise ValueError("O CPF deve conter 9 dígitos iniciais.")
    except ValueError as error:
        print(error)
        quit()

    # Cálculo primeiro digito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11    
    dv1 =  0 if resto < 2 else 11 - resto

    # Cálculo segundo digito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(9)) + dv1 * 2
    resto = soma % 11
    dv2 = 0 if resto < 2 else 11 - resto

    # Verifica se o digito verificador informado é igual ao calculado
    return True if d == f"{dv1}{dv2}" else False

teste = cpf("345702519","74")

print(teste)