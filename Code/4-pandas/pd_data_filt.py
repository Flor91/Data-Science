import pandas as pd
"""
Dataset: versión muy resumida de datos de la Encuesta Permanentes de Hogares (relevamiento llevado adelante por el INDEC)

ch06: int, edad
nivel_ed: string, nivel educativo
htot: int, cantidad de horas totales trabajadas en el período
calif: string, calificación de la tarea
p47t: int, ingreso
"""

location = "Data/data_filt.csv"

data = pd.read_csv(location, sep=",", encoding="latin1")

# Miremos ahora los primeros tres registros del DataFrame data, y los ultimos cinco registros.
print(data.head(3))
print(data.tail(5))

filas, columnas = data.shape
print(f"\nFilas: {filas} - Columnas: {columnas}")

print("\nIndices:")
print(data.index)

print("\nColumnas:")
print(data.keys())
print(data.columns)

# Renombremos nuestras columnas

data.columns = [
    "edad",
    "nivel_educativo",
    "hs_trabajados",
    "calif_ocupacional",
    "ingreso_ult_mes",
]
print("\nColumnas:")
print(data.keys())

# Vamos a modificar ahora el índice de data, así el valor del índice no coincide con la posición
data.index = data.index + 5

print("\nIndices Nuevos:")
print(data.index)
print(data.head(5))

# Accedamos al valor del indice de la cuarta fila
print(data.loc[8])
print(data.iloc[3])
print(data.index[3])

# ¿Cuál es el tipo de datos de la cuarta columna de data?
print(f"\nTipo dato de la cuarta columna: {data.iloc[:, 3].dtype}")

print("\nDistribucion por nivel educativo")
print(data.nivel_educativo.value_counts())

print("")
# construir un objeto DataFrame con los registros de edad menor a 15 o mayor igual a 70
mask_edad_menores = data["edad"] < 15
mask_edad_mayores = data["edad"] >= 70

data_jr_sr = data.loc[mask_edad_menores | mask_edad_mayores]
print(data_jr_sr.head(5))

print("\nIngreso Promedio")
print(data["ingreso_ult_mes"].mean())

print("\nPromedio edad")
print(data["edad"].mean())

print("\nMaximo horas trabajadas")
print(data["hs_trabajados"].max())

print("\nMediana ingreso")
print(data["ingreso_ult_mes"].median())
