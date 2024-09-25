sandwich_orders = ["atum", "frango", "vegetariano", "queijo", "presunto"]

finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"Preparei seu sanduíche de {sandwich}.")
    finished_sandwiches.append(sandwich)  

print("\nTodos os sanduíches foram preparados:")
for finished_sandwich in finished_sandwiches:
    print(f"- Sanduíche de {finished_sandwich}")
