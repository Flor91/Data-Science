import os.path

import numpy as np


def precipitaciones(data):
    result = data[:, 4]
    return result


def cant_dias_sin_lluvia(precip):
    result = precip[precip == 0]
    return len(result)


def cant_dias_con_lluvia(precip):
    result = precip[precip > 0]
    return len(result)


def cant_dias_con_lluvia_mayor_100(precip):
    result = precip[precip > 100]
    return len(result)


def cant_dias_con_lluvia_menorigual_100(precip):
    result = precip[(precip > 0) & (precip < 100)]
    return len(result)


"""
Tenemos un dataset que representa la cantidad de precipitaciones del 2014 en la ciudad de Seattle

La cantidad de precipitaciones está en la cuarta columna, completa el código de una función que reciba el dataset y devuelva estos valores.
"""
data_location = os.path.abspath("../Data/Seattle2014.csv")
data = np.genfromtxt(data_location, skip_header=1, delimiter=",")
data

valores_precipitaciones = precipitaciones(data)
print(valores_precipitaciones[:20])
print(cant_dias_sin_lluvia(valores_precipitaciones))
print(cant_dias_con_lluvia(valores_precipitaciones))
print(cant_dias_con_lluvia_mayor_100(valores_precipitaciones))
print(cant_dias_con_lluvia_menorigual_100(valores_precipitaciones))
