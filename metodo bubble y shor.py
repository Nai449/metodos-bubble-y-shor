# metodo bubble
Python # type: ignore
def bubble_sort(arr):
    n = len(arr)
    # comparar todos los elementos de la lista
    for i in range(n):
        # i elementos que  ya están ordenados
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento actual es mayor que el siguiente
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



# metodo shor
Python # type: ignore
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inicializar el intervalo (gap)

    # Reducir el gap hasta 0
    while gap > 0:
        for i in range(gap, n):
            # Guardar el elemento actual
            temp = arr[i]
            j = i

            # Realizar intercambios dentro del intervalo
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Colocar el elemento en su posición correcta
            arr[j] = temp

        gap //= 2  # Reducir el intervalo



