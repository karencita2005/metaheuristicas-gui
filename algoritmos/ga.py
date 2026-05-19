import random

def ejecutar_ga(
    funcion,
    poblacion_size,
    generaciones,
    tasa_mutacion,
    tasa_cruza,
    objetivo="min",
    tipo="continuo",
    dimensiones=10
):
    # ==========================================
    # CREAR POBLACIÓN
    # ==========================================
    poblacion = []
    for _ in range(poblacion_size):
        if tipo == "binario":
            individuo = [random.randint(0, 1) for _ in range(dimensiones)]
        else:
            individuo = [random.uniform(-10, 10) for _ in range(dimensiones)]
        poblacion.append(individuo)

    historial = []
    mejor_fitness = float("inf") if objetivo == "min" else float("-inf")
    mejor_individuo = None
    sin_mejora = 0

    # ==========================================
    # GENERACIONES
    # ==========================================
    for _ in range(generaciones):
        # 1. EVALUAR (Se hace una sola vez por generación)
        fitnesses = [funcion(ind) for ind in poblacion]

        # Actualizar mejor histórico global
        for i, fitness in enumerate(fitnesses):
            mejoro = (fitness < mejor_fitness) if objetivo == "min" else (fitness > mejor_fitness)
            if mejoro:
                mejor_fitness = fitness
                mejor_individuo = poblacion[i][:]
                sin_mejora = 0

        historial.append(mejor_fitness)
        sin_mejora += 1

        if sin_mejora > 100:
            break

        # Emparejar población con su fitness para acelerar el torneo matemáticamente
        poblacion_con_fitness = list(zip(poblacion, fitnesses))
        nueva_poblacion = []

        # ==========================================
        # ELITISMO
        # ==========================================
        idx_mejor = fitnesses.index(min(fitnesses)) if objetivo == "min" else fitnesses.index(max(fitnesses))
        nueva_poblacion.append(poblacion[idx_mejor][:])

        # ==========================================
        # NUEVA POBLACIÓN
        # ==========================================
        while len(nueva_poblacion) < poblacion_size:
            
            # TORNEO 1 (Muestreamos de la lista emparejada)
            candidatos1 = random.sample(poblacion_con_fitness, 3)
            padre1 = min(candidatos1, key=lambda x: x[1])[0] if objetivo == "min" else max(candidatos1, key=lambda x: x[1])[0]

            # TORNEO 2
            candidatos2 = random.sample(poblacion_con_fitness, 3)
            padre2 = min(candidatos2, key=lambda x: x[1])[0] if objetivo == "min" else max(candidatos2, key=lambda x: x[1])[0]

            # ==========================================
            # CRUZA
            # ==========================================
            if random.random() < tasa_cruza:
                if tipo == "binario":
                    punto = random.randint(1, dimensiones - 1)
                    hijo = padre1[:punto] + padre2[punto:]
                else:
                    hijo = []
                    for i in range(dimensiones):
                        alpha = random.random()
                        valor = alpha * padre1[i] + (1 - alpha) * padre2[i]
                        hijo.append(valor)
            else:
                hijo = padre1[:]

            # ==========================================
            # MUTACIÓN
            # ==========================================
            for i in range(dimensiones):
                if random.random() < tasa_mutacion:
                    if tipo == "binario":
                        hijo[i] = 1 - hijo[i]
                    else:
                        hijo[i] += random.uniform(-1, 1)
                        # Corrección matemática: mantener al hijo dentro del hipercubo [-10, 10]
                        hijo[i] = max(-10, min(10, hijo[i]))

            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    return mejor_individuo, mejor_fitness, historial