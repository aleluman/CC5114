# Tarea 2
En este repositorio se encuentra la implementación de una librería básica de un algoritmo genético, además de tres ejemplos del uso de esta:
* Encontrar un string binario (archivo binary_finder.py)
* Encontrar un string cualquiera (archivo string_finder.py)
* Encontrar una solución al problema unbound Knapsack (archivo knapsack.py)
Esta librería fue escrita en python 3.7 con la ayuda de algunas librerías (numpy, matplotlib).

### Implementación
La implementación completa de la librería se encuentra en el archivo genetic_algorithm.py. En el se implementaron dos clases, una para representar
a un individuo con sus genes y otra para representar a una población de estos. Se tuvo cuidado de mantener la implementación lo 
más genérica posible para permitir la implementación de los ejemplos sin ninguna modificación.
Se implementó directamente el proceso de elitismo para mantener al mejor individuo de cada generación y que el fitness máximo no baje.
En cuanto al problema escogido (unbound knapsack), se definió cada gen como una tupla (x, y) en donde x representa el peso de una caja
e y representa su valor. Además de las cajas especificadas se agregó la caja (0, 0) para representar la no elección de las otras.

En cuanto a la función de firness para el problema, se escogió como la suma del valor de todas las cajas escogidas como valor de fitness, pero
se penalizaba fuertemente (con fitness 0) a individuos en donde la suma total de los pesos de las cajas sobrepasara los 15kg. Cabe destacar que
cada individuo puede tener un máximo de 15 genes (15 cajas), ya que teniendo en cuenta los valores predeterminados es el máximo número de cajas
del tipo (1, 1) que aún cumplen con el requisito de no sobrepasar el peso

### Resultados
En primer lugar se hizo un gráfico de como evoluciona la población en el problema knapsack para una población de 1000 individuos con una tasa de mutaciópn del 10%:
![fitness evolution](/Tarea2/img/Figure_2.png)

Se puede observar que el máximo valor de fitness se alcanza a las 20 generaciones, al igual que el fitness promedio de la población.

Luego se hizo un gráfico de configuración de hiperparámetros (cantidad de individuos y tasa de mutación) para poder observar los parámetros óptimos
que permiten llevar a la solución:
![configuration heatmap](/Tarea2/img/Figure_1.png)

Lo que se codifica en color es el fitness promedio de la población hasta encontrar el óptimo (o superar las 200 generaciones, en tal caso el óptimo no se encontró).

### Análisis
Del primer gráfico se puede desprender que el algoritmo funciona según lo previsto, se alcanza el óptimo en pocas generaciones y el elitismo funciona correctamente. El mínimo se mantiene constante debido a que en cada generación se pueden generar con alta probabilidad individuos con peso mayor a 15kg en el proceso de crossover.

Del segundo gráfico, se puede decir que para la codificación escogida del problema de knapsack, se favorecen hiperparámetros con baja mutación, independiente del tamaño de la población, en cuanto a fitness promedio se refiere.

Como conclusión general, se obtuvieron buenos resultados con el algoritmo, el cual puede resultar útil para resolver diversos problemas de optimización mientras se puedan adaptar con una codificación adecuada.