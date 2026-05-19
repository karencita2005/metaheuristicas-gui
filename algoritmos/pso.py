import random

def ejecutar_pso(
    funcion,
    num_particulas,
    iteraciones,
    dimensiones=2
):
    w = 0.7
    c1 = 1.5
    c2 = 1.5

    x_min, x_max = -10, 10
    v_max = 0.2 * (x_max - x_min) 
    v_min = -v_max

    particulas = []

    # Inicializar partículas
    for _ in range(num_particulas):
        posicion = [random.uniform(x_min, x_max) for _ in range(dimensiones)]
        velocidad = [random.uniform(v_min, v_max) for _ in range(dimensiones)]
        fitness = funcion(posicion)

        particula = {
            "posicion": posicion,
            "velocidad": velocidad,
            "pbest": posicion[:],
            "pbest_fitness": fitness
        }
        particulas.append(particula)

    mejor = min(particulas, key=lambda p: p["pbest_fitness"])
    gbest_posicion = mejor["pbest"][:]
    gbest_fitness = mejor["pbest_fitness"]

    historial = []

    # Ciclo evolutivo
    for _ in range(iteraciones):
        for p in particulas:
            
            # 1. Calcular velocidades primero
            for d in range(dimensiones):
                r1 = random.random()
                r2 = random.random()

                p["velocidad"][d] = (
                    w * p["velocidad"][d]
                    + c1 * r1 * (p["pbest"][d] - p["posicion"][d])
                    + c2 * r2 * (gbest_posicion[d] - p["posicion"][d])
                )
                p["velocidad"][d] = max(v_min, min(v_max, p["velocidad"][d]))

            # 2. Aplicar el movimiento geométrico después
            for d in range(dimensiones):
                p["posicion"][d] += p["velocidad"][d]
                p["posicion"][d] = max(x_min, min(x_max, p["posicion"][d]))

            fitness = funcion(p["posicion"])

            if fitness < p["pbest_fitness"]:
                p["pbest"] = p["posicion"][:]
                p["pbest_fitness"] = fitness

            if fitness < gbest_fitness:
                gbest_posicion = p["posicion"][:]
                gbest_fitness = fitness

        historial.append(gbest_fitness)

    return gbest_posicion, gbest_fitness, historial