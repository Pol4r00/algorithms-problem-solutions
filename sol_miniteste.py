def func_in(val, lista):
    for el in lista:
        if el == val:
            return True

    return False

def encontra_unicos(lista):
    unicos = []

    for i in range(len(lista)):
        if not func_in(lista[i], unicos):
            unicos.insert(len(unicos)+1, lista[i])

    return unicos

def encontra_duplas(lista, unicos):
    duplas = []

    count = 0
    
    for el in unicos:
        for i in range(len(lista)):
            if lista[i] == el:
                count += 1

        if count == 2:
            duplas.insert(len(duplas)+1, el)

        count = 0

    return duplas
        

def remove_duplas(lista):
    unicos = encontra_unicos(lista)
    duplas = encontra_duplas(lista, unicos)
    
    for i in range(len(lista)-1, -1, -1):
        if func_in(lista[i], duplas):
            lista.pop(i)


lista = [20, 20, 5, 1, 1]
remove_duplas(lista)
print(lista)
