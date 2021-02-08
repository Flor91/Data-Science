# Pandas 2 
## Split, Apply, Combine

Separar un conjunto de datos en categorías, y aplicar una función a cada grupo, que puede ser de agregación, transformación o filtro, es un paso muy frecuente en un flujo de trabajo de análisis de datos.

Después de cargar y preparar un conjunto de datos, es posible que debamos calcular estadísticas de grupo o posiblemente tablas dinámicas para generar informes o visualizaciones.

pandas provee métodos que nos permiten realizar estas tareas de forma natural.

### GroupBy

Podemos describir las operaciones sobre grupos con el término split-apply-combine

En la primera etapa del proceso, los datos en un objeto pandas (una instancia de Series o de DataFrame) se dividen en grupos (split) en base a una o más keys que definimos. Esta división se lleva a cabo por filas (axis = 0) o por columnas (axis = 1).

Como segunda etapa, aplicamos una función a cada uno de los grupos (apply) dando como resultado un nuevo valor por grupo.

Como último paso, los resultados de la aplicación de la función en cada uno de los grupos se combina en un objeto resultado (combine).

La claves por las que agrupamos pueden especificarse de varias formas distintas:

* Una lista o numpy array del mismo tamaño que el eje seleccionado

* Para objetos DataFrame, un string que indica el nombre de columna por la que vamos a agrupar.

* Un diccionario o Series que establezca un mapeo entre un valor y el nombre del grupo

* Una función python que se evaluará en cada una de las etiquetas del eje

* Una lista con cualquiera de las opciones de arriba.

Observemos que el resultado de cada una de esas opciones es producir un array de valores que usaremos para dividir el objeto Series o DataFrame

### Pivot tables
Una tabla pivote o tabal dinámica es una herramienta de resumen que está disponible generalmente en programas de hojas de cálculo.

Crea medidas de reumne por una o más keys, usando esas claves como etiquetas de filas o columnas.

Pandas provee un método pivot_table sobre DataFrame y también como una función de pandas

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html

### Joins

Las operaciones de merge o join combinan datasets asociando sus filas de acuerdo a una o más keys.

Estas operaciones son fundamentales en bases de datos relacionales.

Pandas proporciona varias métodos para combinar fácilmente objetos de tipo Series o DataFrame.

* **concat**: La función concat concatena a lo largo de un eje (index o columns) uniendo o intersecando los valores de los índice .
* **append**: Equivalente a concat con axis = 0
* **merge**:
    
    pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=True, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
    
    Los argumentos cuyos valores vamos a establecer frecuentemente son:
    
    left: una instancia de DataFrame o Series
    
    right: otra instancia de DataFrame o Series
    
    on: columnas que usaremos como clave para combinar los registros. Deben estar presentes en ambos DataFrame. Si no se especifica el valor de este argumento y left_index y right_index son False, se inferirá que la intersección de las columnas de ambos DataFrame serán la clave del join
    
    left_on: columnas pertenecientes al DataFrame de la izquierda que usaremos como clave para combinar los registros
    
    right_on: columnas pertenecientes al DataFrame de la derecha que usaremos como clave para combinar los registros
    
    left_index: Si es True, usaremos como clave el índice (etiquetas de las filas) del DataFrame de la izquierda
    
    right_index: Si es True, usaremos como clave el índice (etiquetas de las filas) del DataFrame de la derecha
    
    how: Uno de los siguientes valores 'left', 'right', 'outer', 'inner'. El valor por default es inner
    
    sort: Si es True, ordena el DataFrame resultado en orden lexicográfico de los campos clave. El valor por default es True.
    
    suffixes: Una tupla de string que serán los sufijos de las columnas que tengan el mismo nombre en ambos DataFrame
    
    Valores posibles del argumento how
    El argumento how especifica cómo determinar qué claves se incluirán en el DataFrame resultado.
    
    Si una clave no aparece en alguno de los DataFrame, los valores en el DataFrame que sí la tiene se combinará con valores NA.
    
    inner: las claves en el DataFrame resultado son la intersección de las claves del DataFrame izquierdo y del derecho
    
    outer: las claves en el DataFrame resultado son la unión de las claves del DataFrame izquierdo y del derecho
    
    left: las claves en el DataFrame resultado son las del DataFrame izquierdo
    
    right: las claves en el DataFrame resultado son las del DataFrame derecho
    
* **join**: Combina las columnas de dos DataFrame usando los índices como claves.

