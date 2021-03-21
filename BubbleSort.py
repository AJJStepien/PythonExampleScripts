lista = []
swapped = True
num = int(input("Ile elementów chcesz posortować: "))

for i in range(num):
    val = float(input("Wprowadź element listy: "))
    lista.append(val)

while swapped:
    swapped = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            swapped = True
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print("\nPosortowane:")
print(lista)
