"""
Leer los datos del archivo /M1/CLASE_03/Data/sales_data_sample_excercise.csv

Este archivo tiene algunos datos numéricos y otros de tipo cadena de caracteres.

Las columnas son:

ORDERNUMBER: int, id de la orden

SALES: float, monto abonado

MONTH_ID: int, mes

YEAR_ID: int, año

PRODUCTLINE: str, producto

COUNTRY: str, país de venta

¿Recuerdan que todos los elementos de una instancia de ndarray deben ser del mismo tipo? Entonces vamos a leer el archivo y crear una instancia de ndarray de tipo cadena de caracteres.

¿Qué pasaría si intentáramos crear una instancia de tipo int? ¿Y de tipo float?
"""
import numpy as np
import seaborn as sns

file = "Data/sales_data_sample_excercise.csv"

data_str = np.genfromtxt(file, delimiter="\t", skip_header=True, dtype=str)
print("\nSring dtype")
print(data_str)

data_int = np.genfromtxt(file, delimiter="\t", skip_header=True, dtype=int)
print("\nInt dtype")
print(data_int)

data_float = np.genfromtxt(file, delimiter="\t", skip_header=True, dtype=float)
print("\nFloat dtype")
print(data_float)

data = np.genfromtxt(file, delimiter="\t", skip_header=True)
print("\nNo specified dtype")
print(data)

# Crear un array numérico que tenga como valores las columna SALES y otro array de str que tenga como valores la columna COUNTRY

sales = data_float[:, 1]
print(sales)

country = data_str[:, -1]
print(country)

# Sobre los datos de precios de ventas (columna SALES) calcular:
# mínimo máximo promedio cantidad suma

print(f"\nPrecio minimo sales: {sales.min()}")
print(f"Precio máximo sales: {sales.max()}")
print(f"Precio promedio sales: {sales.mean()}")
print(f"Precio cantidad sales: {len(sales)}")
print(f"Precio suma sales: {sales.sum()}")

print("\n¿Cuántas ventas se hicieron en USA?")
usa_mask = country == "USA"
usa_sales = sales[usa_mask]
print(usa_sales.sum())

print(
    "\n¿Cuáles son los precios de las 5 ventas que están en las filas 6 a 10 del dataset?"
)
print(sales[6:11])

print(f"Precio media sales: {sales.mean()}")
print(f"Precio mediana sales: {np.median(sales)}")
print(f"Precio desvio sales: {sales.std()}")
print(f"Precio rango sales: {sales.max() - sales.min()}")


def distribution_plotter(data, label):
    sns.set(rc={"figure.figsize": (10, 7)})
    sns.set_style("white")
    dist = sns.distplot(data,
                        hist_kws={"alpha": 0.2},
                        kde_kws={"linewidth": 5})
    dist.set_title("Distribucion de " + label + "\n", fontsize=16)


random_generator = np.random.default_rng(1234)
birthday = random_generator.integers(low=1, high=366, size=30)
distribution_plotter(birthday, "Cumple")
