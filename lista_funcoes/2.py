def formatar_data(dia, mes, ano):
    data = f"{dia}/{mes}/{ano}"
    return data

data_formatada = formatar_data(mes=11,dia=15, ano=2027)

print(data_formatada)
