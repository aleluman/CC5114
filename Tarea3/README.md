# Tarea 3
 En este repositorio se encuentra la implementación de una librería de programación genética (en base al algoritmo genético de la tarea 2), además de diversos ejemplos que muestran su uso para encontrar números y expresiones determinadas. Estos ejemplos se encuentran en el archivo exercises.py y corresponden a los siguientes:
 * Encontrar una expresión que se evalúe al número 10 (usando las operaciones +, - y * y los números 2, 3 y 5).
 * Encontrar una expresión que se evalúe al número 65346 (usando las operaciones +, -, * y máx() y los números 25, 7, 8, 100, 4 y 2).
 * Lo mismo que anteriormente pero limitando el tamaño de los árboles generados para prevenir problemas de rendimiento.
 * Lo mismo que anteriormente pero limitando el uso de los números a solo una repetición cada uno.
 * Encontrar la expresión x²+x-6 (usando las operaciones +, - y * y el conjunto {−10, . . . , 10, x}).
 * Encontrar la expresión (x + 3) / 3 usando el mismo conjunto que en el punto anterior.

 Los archivos arboles.py y ast.py son las librerías de árboles provistas (modificadas en los casos que se pidió).

### Implementación
Se utilizó python 3.7 para programar la librería y además se hizo uso de la librería numpy.

Para implementar variables se modificó el código arboles.py provisto, añadiendo un parámetro dict_val a la función eval que almacena los valores de las variables. Este diccionario queda como None en el caso de no ser necesario. Al momento de evaluar se chequea que el nodo terminal sea un string, y en caso afirmativo se busca el valor en el diccionario.

Para implementar la división simplemente se utilizó la misma estructura que el nodo de multiplicación provisto. Para prevenir divisiones por cero, se agregó un bloque try a la función de fitness lo que permite atrapar la excepción y dar puntaje 0 a árboles que la produzcan.

Las funciones de fitness fueron todas normalizadas para que su rango esté entre 0 y 1, para no perder generalidad entre cada ejemplo (por esto se escogieron funciones de la forma e^x^2).

### Resultados

Los siguientes gráficos muestran la evolución del fitness en cada generación para cada uno de los ejercicios. Cabe destacar que en todos se encontró una expresión equivalente a lo pedido exceptuando el ejercicio sin repetir nodos terminales (en donde de todas formas se consiguió un fitness alto), que se decidió terminar en la generación 1000. Todos los demás ejercicios terminaron al llegar al fitness óptimo (1):
![img1](/Tarea3/img/1.png)
En este primer gráfico se llegó bastante rápido a la solución con los hiperparámetros seleccionados, sin embargo para otros hiperparámetros tomaba mucho más tiempo o derechamente el programa no podía seguir ejecutándose.


![img2](/Tarea3/img/2.png)
En el segundo caso la ejecución tomó muchas más generaciones, pero cada iteración tomaba bastante menos tiempo.


![img3](/Tarea3/img/3.png)
En el caso sin repetición de nodos terminales se puede observar que el fitness medio se mantuvo muy bajo, debido a que los árboles que repetían nodos tenían automáticamente fitness 0.


![img4](/Tarea3/img/4.png)
Al buscar x²+x-6 se tuvo la suerte de escoger buenos hiperparámetros por lo que se encontró una expresión equivalente de forma bastante rápida.


![img5](/Tarea3/img/5.png)
En el caso de la división tomó más generaciones, pero de todas formas la ejecución fue rápida.

### Análisis
A continuación se presenta un heatmap para diferentes configuraciones de los hiperparámetros de tamaño de la población y tasa de mutación. El heatmap muestra la cantidad de generaciones que tomó encontrar la solución óptima en el problema de encontrar el número 65346 limitando el tamaño de los árboles. Se estableció un máximo de 50 generaciones para limitar el tiempo de cálculo. Se utilizaron valores en los rangos [50, 500] y [0, 1].
![img6](/Tarea3/img/heatmap.png)

Se puede observar que si bien la distribución tiene una gran componente aleatoria, se obtienen resultados en menos generaciones mientras la población sea más grande, al igual que la tasa de mutación, pero al mismo tiempo, al incrementar estos valores aumenta el tiempo de ejecución, por lo que existe un trade-off entre el número de generaciones que lleva al óptimo y el tiempo de cálculo.