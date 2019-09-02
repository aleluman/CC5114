# Tarea 1
En este repositorio se encuentra una implementación de una red neuronal básica, utilizada para el análisis de dos dataset: el dataset para clasificación
de especies de plantas del género Iris, y el dataset de clasificación de semillas. Esta red neuronal fue implementada en python 3.7 utilizando la
librería numpy.

### Implementación
Hay cuatro archivos necasarios para entrenar la red y obtener los resultados:
* utilities.py: Incluye las funciones necesarias para normalizar los datos, además de realizar el proceso de 
one-hot-encoding. Además incluye un wrapper para cargar los datasets presentes (o cualquier otro de formato similar) de forma más rápida.
* activation_functions.py: incluye las funciones sigmoid y tanh para entrenar la red, además de sus 
derivadas.
* network.py: En donde está implementada la red neuronal (utilizando matrices). Incluye métodos para entrenar, además de los
algoritmos de feedforward y backpropagation. Además aquí se encuentran métodos que permiten graficar los resultados luego de entrenar la red
e imprimir una matriz de confusión en consola.
* main.py: principal ejecutable donde se utilizan los archivos anteriores para entrenar la red y obtener los resultados.

### Resultados
Se obtuvieron los siguientes resultados en cada dataset luego de entrenar la red:

* En el caso del dataset Iris, se configuraron los parámetros de la red de esta forma:
red de 4 capas, con 4 neuronas de input, 3 de output, y dos capas intermedias con 8 y 5 neuronas. Se utilizó la función sigmoid con un learning rate de 
0.5 y 2000 epochs.
![iris](/Tarea1/images/iris.png)
Como se puede observar se obtuvieron buenos resultados, tanto el error como los aciertos de la red fueron mejorando al aumentar el número de iteraciones. 
El entrenamiento con este dataset tomó cerca de 15 segundos para los parámetros establecidos.

* Para el dataset de las semillas, los parámetros fueron los siguientes: 7 neuronas de input, 3 de output y dos capas intermedias con
12 y 5 neuronas cada una. Ahora se utilizó la función tanh como función de activación y se entrenó durante 2000 epochs
![seed](/Tarea1/images/seed.png)
En este caso también se obtuvieron buenos resultados, con un tiempo de entrenamiento similar al dataset anterior, pese a que cada tupla tiene más parámetros.

Como observación, y luego de realizar varias pruebas, se notó que la función de activación tanh logra mejores tiempos de entrenamiento que la función sigmoid, además de entregar
mejores resultados en el número de aciertos. También es necesario utilizar un learning rate menor que en la función sigmoid, o si no la red no trabaja correctamente. 

También se analizaron diversas configuraciones en las capas de la red neuronal, pero en la mayoría de los casos se encontraron resultados similares, por lo que el número de capas intermedias no afecta tanto para una tarea "simple"
como es la clasificación de estos dataset. 

Los resultados obtenidos representan un promedio al utilizar diferentes parámetros, hay configuraciónes de parámetros que tienen más dificultad de aprender o que simplemente no aprenden aunque se realicen muchas iteraciones.

Se realizaron experimentos con la función de activación ReLU (rectified linear unit) y se lograron resultados muy positivos: la red aprendió en menos iteraciones y en algunos casos se logró identificar
correctamente el 100% de los datos en el dataset de testing. Sin embargo la función es más sensible a los parámetros de la red y muchas veces no se podía entrenar correctamente.
