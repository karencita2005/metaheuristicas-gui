import random
from problemas.continuas import sphere

def ejecutar_pso(num_particulas, iteraciones):

    # ==========================================
    # PARÁMETROS PSO
    # ==========================================

    w = 0.7
    c1 = 1.5
    c2 = 1.5

    dimensiones = 2

    # ==========================================
    # CREAR PARTÍCULAS
    # ==========================================

    particulas = []

    for _ in range(num_particulas):

        posicion = [
            random.uniform(-10, 10)
            for _ in range(dimensiones)
        ]

        velocidad = [
            random.uniform(-1, 1)
            for _ in range(dimensiones)
        ]

        fitness = sphere(posicion)

        particula = {

            "posicion": posicion,
            "velocidad": velocidad,

            "pbest": posicion[:],
            "pbest_fitness": fitness
        }

        particulas.append(particula)

    # ==========================================
    # GLOBAL BEST
    # ==========================================

    gbest = min(
        particulas,
        key=lambda p: p["pbest_fitness"]
    )

    gbest_posicion = gbest["pbest"][:]
    gbest_fitness = gbest["pbest_fitness"]

    historial = []

    # ==========================================
    # ITERACIONES
    # ==========================================

    for _ in range(iteraciones):

        for p in particulas:

            for d in range(dimensiones):

                r1 = random.random()
                r2 = random.random()

                # Actualizar velocidad
                p["velocidad"][d] = (

                    w * p["velocidad"][d]

                    + c1 * r1 *
                    (
                        p["pbest"][d]
                        - p["posicion"][d]
                    )

                    + c2 * r2 *
                    (
                        gbest_posicion[d]
                        - p["posicion"][d]
                    )
                )

                # Actualizar posición
                p["posicion"][d] += p["velocidad"][d]

            # Evaluar fitness
            fitness = sphere(p["posicion"])

            # Actualizar pbest
            if fitness < p["pbest_fitness"]:

                p["pbest"] = p["posicion"][:]
                p["pbest_fitness"] = fitness

            # Actualizar gbest
            if fitness < gbest_fitness:

                gbest_posicion = p["posicion"][:]
                gbest_fitness = fitness

        historial.append(gbest_fitness)

    return gbest_posicion, gbest_fitness, historial