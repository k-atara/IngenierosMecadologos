# This programm executes both, a training-test dataset and the specified user dataset. The input from the user will be predicted with the default training dataset while calculating an estimated accuracy for the 2% of the data selected, from the default dataset, for testing.

# Execute the File 'main.py' (you could specify the input data to process) 
        # python main.py <file_name>.csv

# You have access to the trained model to use as you wish for this same aplication (inside the folder named 'model')


# The team:
    # Aarón Pérez Ontiveros
    # Emmanuel del Rio Sarmiento
    # Valeria Herbas
    # Alejandro Hidalgo Badillo
    # Kimberly Atara Lopez Vazquez
    
# HistGradientBoostingRegressor:
Es un algoritmo de aprendizaje automático (Machine learning) popular que ha sido implementado para distintos objetivos de forma efectiva. Dado que es un algoritmo basado en histograma es más eficiente tanto en el consumo de memoria como en la velocidad de entrenamiento, es por eso que desarrollaremos nuestro trabajo sobre esta base.

Funciona muy bien en una amplia gama de conjuntos de datos en la práctica (n_muestras >= 10 000).
Un algoritmo débil entrena el modelo, luego se reorganiza de acuerdo con los resultados del entrenamiento y se hace más fácil de aprender. Este modelo modificado luego se envía al siguiente algoritmo y el segundo algoritmo aprende más fácilmente que el primero. Una ventaja de usar tres modelos es que si surgen errores en uno, el siguiente puede ayudar a ajustar los mismos para lograr obtener mejores resultados.
Es un método basado en hojas, esto quiere decir que el árbol es más grande porque en el entrenamiento del algoritmo cultiva el árbol eligiendo la hoja con mayor peso para crecer. Si no se encontraron valores faltantes para una característica determinada durante el entrenamiento, las muestras con valores faltantes se asignan al hijo que tenga la mayor cantidad de muestras. Tiene una propiedad max_depth que permite limitar la profundidad del árbol.
La biblioteca scikit-learn proporciona una implementación alternativa del algoritmo de aumento de gradiente, denominado aumento de gradiente basado en histograma.
Con este modelo logramos una precisión en promedio de alrededor del 80% con el conjunto de datos proporcionado.
Ventajas:
        # Faster training speed and higher efficiency.
        # Lower memory usage.
        # Better accuracy.
        # Support of parallel, distributed, and GPU learning.
        # Capable of handling large-scale data.
Podremos usar este modelo a través de una instancia de AWS muy básica y consumir los datos enviados gracias a la alta eficiencia que ofrece este modelo.


    
