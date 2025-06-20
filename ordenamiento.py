def selection_sort(lista):
    n = len(lista)
    
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = key
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivot = lista[0]
    listaMenores = [x for x in lista[1:] if x <= pivot]
    listaMayores = [x for x in lista[1:] if x > pivot]

    return quick_sort(listaMenores) + [pivot] + quick_sort(listaMayores)