# Algoritmos de búsqueda y ordenamiento

## Introducción
Los algoritmos de búsqueda y ordenamiento son fundamentales para el procesamiento eficiente de datos. Estos algoritmos permiten organizar la información de forma que se facilite su consulta, análisis o modificación, optimizando así el rendimiento.  

Los algoritmos de ordenamiento tienen como objetivo organizar una colección de datos(como números, letras o registros) según un criterio específico, generalmente de menor a mayor o alfabéticamente. Existen distintos tipos de ordenamientos, como Bubble Sort, Selection Sort, Insertion Sort y Quick Sort, cada uno con sus ventajas, desventajas y niveles de eficiencia según el tamaño y la naturaleza de los datos.  

Por otro lado los algoritmos de búsqueda permiten localizar un elemento específico dentro de una estructura de datos. Los más comunes son la búsqueda lineal y la búsqueda binaria.

## Algoritmo de búsqueda
Un algoritmo de búsqueda es un conjunto de pasos o instrucciones que permite localizar un elemento dentro de una estructura de datos, como una lista o arreglo.  
 Su objetivo es determinar si el elemento está presente y, en caso afirmativo, devolver su posición(índice).  
Hay distintos tipos de algoritmos, pero los más comunes son:

### Búsqueda lineal
Recorre la lista elemento por elemento desde el principio hasta el final y no requiere que la lista esté ordenada

```python
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1
```

*Ventaja: Es simple y funciona con cualquier tipo de lista*  
*Desventaja: Es lento si la lista es muy grande, porque puede necesitar recorrer toda la lista.*  

### Búsqueda binaria
Divide la lista ordenada a la mitad repetidamente para encontrar el valor. Compara el elemento del medio con el buscado y decide si debe buscar a la izquierda o derecha  

```python
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1
```

*Ventaja: Mucho más rápida que la búsqueda lineal (complejidad O(log n))*
*Desventaja: Requiere que la lista esté ordenada previamente*

## Algoritmo de ordenamiento

Un algoritmo de ordenamiento es un conjunto de instrucciones que permite organizar los elementos de una lista o arreglo según un determinado criterio, generalmente de menor a mayor o de mayor a menor.  
Hay distintos tipos de algoritmos de ordenamiento, cada uno con sus propias ventajas, desventajas y niveles de eficiencia dependiendo del tipo de datos o tamaño de la lista.  
Para los ejemplos utilizamos listas de enteros y el ordenamiento de menor a mayor.

### Ordenamiento por selección – SelectionSort

Busca el elemento más pequeño del arreglo y lo pone en la posición correcta, repitiendo el proceso con el resto de los valores de la lista.

![SelectionSort](images/selection-sort-animation.gif)

*Ventaja: Es fácil de entender e implementar. No requiere memoria adicional.
Desventaja: Es lento en listas grandes y realiza muchas comparaciones innecesarias, incluso si ya está ordenada.*


### Ordenamiento de burbuja – BubleSort

Compara elementos adyacentes e intercambia si están en orden incorrecto. Al final de cada pasada, el mayor queda al final.

![BubbleSort](images/bubble-sort.gif)

*Ventaja: Muy fácil de implementar y entender. Y útil para listas pequeñas o casi ordenadas.*
*Desventaja: Es muy ineficiente en listas grandes y hace muchos pasos innecesarios si no se optimiza.*

### Ordenamiento por inserción – InsertionSort

Recorre la lista e inserta cada elemento en la posición correcta respecto a los elementos anteriores ya ordenados.

![InsertionSort](images/insertion-sort-example.gif)

*Ventaja: Muy eficiente para listas pequeñas o que ya están parcialmente ordenadas.*
*Desventaja: No es adecuado para listas grandes y desordenadas. Puede hacer muchos desplazamientos.*


### Ordenamiento rápido – QuickSort

Utiliza un elemento pivote para dividir la lista en dos partes: menores y mayores. Ordena cada parte de forma recursiva.

![QuickSort](images/Sorting_quicksort.gif)

*Ventaja: Muy rápido y eficiente en la mayoría de los casos, con complejidad promedio.*
*Desventaja: Si el pivote se elige mal, puede volverse muy lento. Además usa recursividad, lo cual puede consumir mucha memoria.*

## Referencias

 - [Algoritmos de búsqueda y ordenamiento - Medium](https://medium.com/@mise/algoritmos-de-b%C3%BAsqueda-y-ordenamiento-7116bcea03d0)

 - [Algoritmos de ordenamiento - Wikipedia](https://es.wikipedia.org/wiki/Algoritmo_de_ordenamiento)

 - [Algoritmos de búsqueda](https://es.wikipedia.org/wiki/Algoritmo_de_b%C3%BAsqueda)