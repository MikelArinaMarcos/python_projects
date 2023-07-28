"""
Creación del juego HUNDIR LA FLOTA (versión simplificada)

Originalmente el juego está pensado para un tablero de 5x5 y con 5 barcos.
Si se quiere modificar, bastará con cambiar los parámetros que hay
al final del código.

El jeugo lo que realiza es: dibuja un único tablero, dibuja los barcos en pantalla que se han
colocado alatoriamente y vas jugando hundiendo esos mismos barcos.
Los barcos son de una única casilla.

"""
# Importamos la libreria random para colocar alatoriamente los barcos enemigos.
import random

# Función que crea el tablero
def crear_tablero(filas, columnas):
    return [[' ' for _ in range(columnas)] for _ in range(filas)]

# Función que imprime el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(' | '.join(fila))
        print('-' * (4 * len(fila) - 1))

# Función que coloca los barcos en el tablero
def colocar_barcos(tablero, num_barcos):
    filas = len(tablero)
    columnas = len(tablero[0])
    
    for _ in range(num_barcos):
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        
        while tablero[fila][columna] == 'B':
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - 1)
        
        tablero[fila][columna] = 'B'


# Función principal del juego
def jugar_hundir_la_flota(filas, columnas, num_barcos):
    print("Bienvenido a Hundir la Flota!")
    
    tablero = crear_tablero(filas, columnas)
    colocar_barcos(tablero, num_barcos)
    
    intentos = 0
    while True:
        imprimir_tablero(tablero)
        fila = int(input("Ingresa el número de fila: "))
        columna = int(input("Ingresa el número de columna: "))
        
        if 0 <= fila < filas and 0 <= columna < columnas:
            if tablero[fila][columna] == 'B':
                print("¡Barco hundido!")
                tablero[fila][columna] = 'X'
                num_barcos -= 1
                if num_barcos == 0:
                    print("¡Felicidades! Has hundido todos los barcos.")
                    break
            else:
                print("Agua...")
                tablero[fila][columna] = 'O'
            
            intentos += 1
        else:
            print("Coordenadas inválidas. Inténtalo nuevamente.")
    
    print(f"Juego terminado en {intentos} intentos.")

# Parámetros del juego

if __name__ == "__main__":
    filas = 5
    columnas = 5
    num_barcos = 5
    jugar_hundir_la_flota(filas, columnas, num_barcos)