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

# Función que detecta el final del juego
def juego_terminado(tablero):
    for fila in tablero:
        for elemento in fila:
            if elemento == " ":
                return False
    return True

# Función principal del juego
def jugar_tres_en_raya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while not juego_terminado(tablero):
        imprimir_tablero(tablero)

        fila = int(input(f"Jugador {jugador_actual}, ingresa el número de fila (0-2): "))
        columna = int(input(f"Jugador {jugador_actual}, ingresa el número de columna (0-2): "))

        if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"¡Jugador {jugador_actual} ha ganado!")
                break
            jugador_actual = "X" if jugador_actual == "O" else "O"
        else:
            print("Movimiento inválido. Inténtalo nuevamente.")

    if juego_terminado(tablero) and not verificar_ganador(tablero, "X") and not verificar_ganador(tablero, "O"):
        imprimir_tablero(tablero)
        print("¡Empate!")

# Llamada al juego
if __name__ == "__main__":
    jugar_tres_en_raya()