import pandas as pd
"""
Rooms: cantidad de habitaciones

Price: precio en dolares

Method: S - property sold; SP - property sold prior; PI - property passed in; PN - sold prior not disclosed; SN - sold not disclosed; NB - no bid; VB - vendor bid; W - withdrawn prior to auction; SA - sold after auction; SS - sold after auction price not disclosed. N/A - price or highest bid not available.

Type: br - bedroom(s); h - house,cottage,villa, semi,terrace; u - unit, duplex; t - townhouse; dev site - development site; o res - other residential.

SellerG: agente inmobiliario

Date: fecha de venta

Distance: distancia a CBD

Regionname: región (West, North West, North, North east …etc)

Propertycount: cantidad de inmuebles que existen en ese suburbio.

Bedroom2 : Scraped # habitaciones (de distintas fuentes)

Bathroom: cantidad de baños

Car: cantidad de carspots

Landsize: superficie

BuildingArea: tamaño del edificio

CouncilArea: municipio
"""

location = "Data/melb_data.csv"

data = pd.read_csv(location)

print(data.head(5))

print(data.isnull().head(3))

print("\nNulos por columnas: ")
print(data.isnull().sum())

print("\nNo nulos por filas:")
print(data.notnull().sum(axis=1))
print("")

# Eliminar todas las columnas que tengan algún valor faltante
data_columnas_completas = data.dropna(axis=1)
print(data.shape)
print(data_columnas_completas.shape)

# Eliminar todas las filas que tengan algún valor faltante
data_columnas_completas = data.dropna()
print(data_columnas_completas.shape)

# Eliminar todas las columnas que tengan una cantidad de registros con valor (no nulos) menor a un umbral (threshold)
# quiero que como maximo haya 100 nulos por columna:
umbral = 13480
data_clean_col_with_many_null = data.dropna(axis=1, thresh=umbral)
print(data_clean_col_with_many_null.shape)

# Eliminar todas las filas que tengan una cantidad de campos con valor (no nulos) menor a un umbral (threshold)
# quiero que como maximo haya 3 columnsa en null por registro:
umbral = 18
data_clean_row_with_many_null = data.dropna(axis=0, thresh=umbral)
print(data_clean_row_with_many_null.shape)

print(pd.value_counts(data.Car))
"""
Vemos que los valores más probables para el campo Car son 1 y 2.

Vamos a imputar los valores faltantes de este campo de dos formas diferentes:

La primera, asignamos un 2 a todos los faltantes en Car
La segunda, asignamos al 45% de los valores faltantes valor 1, y al resto valor 2
"""


def print_null_cars(s):
    print("\nNull cars:")
    data_car_2_mask = s == 2
    data_car_2_count = data_car_2_mask.sum()
    print(data_car_2_count)
    print("---")
    data_car_null_mask = s.isnull()
    data_car_null_count = data_car_null_mask.sum()
    print(data_car_null_count)


print_null_cars(data.Car)

# Rellenamos
data_car_2_fill = data.Car.fillna(2)
# inventamos una columna nueva para no modificar los datos originales y
# que nos sirva para el siguiente ejercicio sin volver a leer los datos:
data["Car_fill"] = data_car_2_fill

print_null_cars(data.Car_fill)

# Asignamos al 45% de los valores faltantes valor 1, y al resto valor 2
# los registros que son null en Car:
data_car_null_mask = data.Car.isnull()
data_car_null = data.loc[data_car_null_mask, :]
print(data_car_null.shape[0])

# una muestra del 45% de los registros calculados en el paso anterior:
data_car_null_mask_sample_1 = data_car_null.sample(frac=0.45)

# los índices de ese 45%
data_car_null_ones_index = data_car_null_mask_sample_1.index
print(len(data_car_null_ones_index))

# los que van a ser rellenados con valor 2 son todos los que no fueron seleccionados en el paso anterior:
data_car_null_twos_index = data_car_null.index.difference(
    data_car_null_ones_index)
print(len(data_car_null_twos_index))

# Ahora que tenemos los index que nos sirven, asignamos los valores correspondientes a los registros seleccionados:
data.loc[data_car_null_ones_index, "Car"] = 1
data.loc[data_car_null_twos_index, "Car"] = 2
