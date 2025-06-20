from ordenamiento import selection_sort, quick_sort, bubble_sort, insertion_sort
from busqueda import busqueda_binaria, busqueda_lineal

# Metodos de ordenamiento
print(" - Selection Sort:   ", selection_sort([1, 12, 3, 8, 13, 2, 4]))
print(" - Bubble Sort:      ", bubble_sort([2, 12, 3, 8, 14, 4, 1]))
print(" - Insertion Sort:   ", insertion_sort([3, 12, 5, 18, 31, 22, 4, 1]))
print(" - Quick Sort:       ", quick_sort([5, 12, 3, 8, 22, 2, 4, 1]))

lista1 = [17, 12, 3, 8, 11, 2, 4, 1]

# Busqueda lineal
numero = int(input("Búsqueda lineal - Ingrese número: "))
pos = busqueda_lineal(lista1, numero)
if pos != -1:
    print(f"El número {numero} fue encontrado en la posición {pos}")
else:
    print(f"El número {numero} no se encuentra en la lista")

# Busqueda binaria
lista2 = [7, 12, 3, 8, 11, 2, 4, 1]
lista_ordenada = sorted(lista2)
numero = int(input("Búsqueda binaria - Ingrese número: "))
pos = busqueda_binaria(lista_ordenada, numero)
if pos != -1:
    print(f"El número {numero} fue encontrado en la posición {pos}")
else:
    print(f"El número {numero} no se encuentra en la lista")