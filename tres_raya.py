"""
Creación del famoso juego de mesa
3 en Raya

"""

# Función que imprimirá el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

# Función que verifica el ganador de la partida
def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if all(elem == jugador for elem in fila):
            return True

    for columna in range(3):
        if all(tablero[i][columna] == jugador for i in range(3)):
            return True

    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False