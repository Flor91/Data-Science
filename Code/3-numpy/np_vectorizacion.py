"""
1) Generemos un array de 1 dimension con 1000 elementos con distribución normal de media 5 y desvío 2, inicialicemos la semilla en el valor 4703.

2) Usando algunas de las funciones de Numpy listadas en Métodos matemáticos y estadísticos, calculemos la media y el desvío de los elementos del array que construimos en el punto 1.

3) Generemos otro array de dimensiones 100 filas, 20 columnas con distribución normal de media 5 y desvío 2.

4) Usando las mismas funciones que en 2) calculemos la media y el desvío de cada fila del resultado de 3.

5) Usando las mismas funciones que en 2) calculemos la media y el desvío de cada columna del resultado de 3.
"""
import numpy as np
from random_distribuciones import random_binomial


def print_stats(a, axis):
    print(f"Media: {a.mean(axis=axis)}")
    print(f"Desvio: {a.std(axis=axis)}")


array_normal_1 = random_binomial(seed=4703, size=1000, n=5, p=2)
print(array_normal_1[:5])

print_stats(array_normal_1, 0)

array_normal_2 = random_binomial(seed=4703, size=(100, 20), n=5, p=2)
print(array_normal_2[:5, :2])

print_stats(array_normal_2, 0)

print_stats(array_normal_2, 1)
