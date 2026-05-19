import random

def ejecutar_ga(
    funcion,
    poblacion_size,
    generaciones,
    longitud=10
):

    poblacion = []

    # ==========================================
    # POBLACIÓN INICIAL
    # ==========================================

    for _ in range(poblacion_size):

        individuo = [
            random.randint(0, 1)
            for _ in range(longitud)
        ]

        poblacion.append(individuo)

    historial = []

    mejor_individuo = None
    mejor_fitness = -999999

    # ==========================================
    # GENERACIONES
    # ==========================================

    for _ in range(generaciones):

        fitnesses = []

        for individuo in poblacion:

            fitness = funcion(individuo)

            fitnesses.append(fitness)

            if fitness > mejor_fitness:

                mejor_fitness = fitness
                mejor_individuo = individuo[:]

        historial.append(mejor_fitness)

        nueva_poblacion = []

        # ==========================================
        # NUEVA POBLACIÓN
        # ==========================================

        for _ in range(poblacion_size):

            padre1 = random.choice(poblacion)
            padre2 = random.choice(poblacion)

            # Cruza
            punto = random.randint(1, longitud - 1)

            hijo = (
                padre1[:punto]
                +
                padre2[punto:]
            )

            # Mutación
            for i in range(longitud):

                if random.random() < 0.1:

                    hijo[i] = 1 - hijo[i]

            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    return mejor_individuo, mejor_fitness, historial