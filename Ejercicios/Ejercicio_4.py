def sort_list(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print(sort_list([5, 2, 8, 1, 9]))
print(sort_list([10, 4, 6, 2, 1]))
print(sort_list([7, 3, 9, 5, 2]))
