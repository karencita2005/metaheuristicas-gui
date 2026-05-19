# ==========================================
# COLOR MATCHING
# ==========================================

def color_matching(solucion):

    objetivo = ["rojo", "verde", "azul"]

    puntos = 0

    for i in range(len(solucion)):

        if solucion[i] == objetivo[i]:
            puntos += 1

    return puntos