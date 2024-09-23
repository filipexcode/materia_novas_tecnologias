V=[9,8,7,12,0,13,21] 

lista_par = []
lista_impar = []

for item in V:
    if item % 2 == 0:
        lista_par.append(item)
    else:
        lista_impar.append(item)

print(lista_par)
print(lista_impar)
