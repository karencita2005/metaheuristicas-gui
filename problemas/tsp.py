import math

# ==========================================
# DISTANCIA EUCLIDIANA
# ==========================================

def distancia(ciudad1, ciudad2):

    return math.sqrt(
        (ciudad1[0] - ciudad2[0])**2
        +
        (ciudad1[1] - ciudad2[1])**2
    )

# ==========================================
# FITNESS TSP
# ==========================================

def tsp(ruta, ciudades):

    total = 0

    for i in range(len(ruta) - 1):

        ciudadA = ciudades[ruta[i]]
        ciudadB = ciudades[ruta[i+1]]

        total += distancia(ciudadA, ciudadB)

    return total