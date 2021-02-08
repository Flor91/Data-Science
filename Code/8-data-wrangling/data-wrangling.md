
## Definiciones
#### Data Wrangling:

Proceso de limpieza y unificación de conjuntos de datos desordenados y complejos para facilitar su acceso, exploración, análisis o modelización posterior.

#### Data munging:

Proceso de limpiar, preparar y validar los datos.

#### Extract, Transform and Load (ETL):

Extraer, transformar y cargar los datos.

#### Exploratory data analysis (EDA):

Resumir las principales características de un dataset, a menudo con métodos visuales, sin usar un modelo estadístico o de machine learning.


### Tipos de variables
Las variables pueden ser caracterizadas como:

#### Cuantitativas:
  toman valores numéricos, como en el caso de del ingreso de una persona o el precio de una casa.

#### Cualitativas:
  toman valores en una de K diferentes clases o categorías.

  Variables cualitativas con dos posibles valores se denomina binaria o dicotómica.

  Tipos de variable cualitativa:

  * Nominal/Categórica:

  toman valores entre categorías nombradas.

  Se suele asignar valores o rótulos numéricos a las variables categóricas:Estado civil, 0 si soltero y 1 si casado y 2 si divorciado. Los números utilizados para rotular son arbitrarios. En general, el software asume que los valores numéricos reflejan cantidades algebraicas y, por tanto, un orden.

  La principal medida de posición es la moda.

  La mediana y la media no están definidas (y en general cualquier operación numérica tampoco).

  * Ordinal:

  Es una variable categórica con un orden definido.
  
  Un ejemplo puede ser la variable rango_etario, que toma valores "niño", "adolescente", "adulto", "adulto mayor" donde está definido un orden "niño" < "adolescente" < "adulto" < "adulto mayor"

#### Dummy (variable indicadora)
  son variables cualitativas que toma valores 0 o 1 para indicar la ausencia o presencia de algún atributo o efecto categórico.

  Formalmente una variable dummy puede ser expresada mediante una función indicadora:
 
 ¿Cuál es la relación entre variables categóricas y variables dummies?

Una variable categórica con N categorías puede ser expresada en términos de N−1 variables dummies (one-hot encoding).

## Eliminación de duplicados

Para determinar si un DataFrame tiene registros duplicados, primero debemos definir en qué campos deben coincidir los valores de los registros para considerar que son iguales.

El método duplicated de pandas permite definir en el argumento subset una lista de columnas a evaluar cuando queremos determinar si dos registros son duplicados. Si no establecemos el valor de este argumento, sólo seran duplicados aquellos registros cuyos valores coincidan en todos los campos.

El argumento keep toma valores

first: devuelve False (no duplicado) el primer registro encontrado, y True (duplicados) todas las demás apariciones
last: devuelve False (no duplicado) el último registro encontrado, y True (duplicados) todas las demás apariciones
False: devuelve True (duplicado) todos los registros duplicados
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html

El método drop_duplicates de pandas devuelve un nuevo DataFrame sin registros duplicados.Los argumentos subset y keep tienen el mismo comportamiento que en duplicated

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html

## Reemplazo de valores

El método replace ofrece varias formas de efectuar reemplazos sobre una serie de Pandas:

Un valor viejo por un valor nuevo.

Una lista de valores viejos por un valor nuevo.

Una lista de valores viejos por una lista de valores nuevos.

Un diccionario que mapee valores nuevos y viejos.