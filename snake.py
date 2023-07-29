import pygame
import sys
import random
import time

pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

# Direccionamientos
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Función para mostrar mensaje y esperar antes de reiniciar el juego
def show_message(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, WHITE)
    SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    time.sleep(2)

def main():
    # Inicialización de variables
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_direction = RIGHT
    snake_speed = 10
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    level = 1
    food_to_next_level = 5
    foods_collected = 0
    game_over = False

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != DOWN:
                    snake_direction = UP
                elif event.key == pygame.K_DOWN and snake_direction != UP:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                    snake_direction = LEFT
                elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                    snake_direction = RIGHT

        # Actualizar posición de la serpiente
        head_x, head_y = snake[-1]
        dx, dy = snake_direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)

        if new_head in snake[:-1]:
            show_message("¡Perdiste! Inténtalo de nuevo.")
            snake.clear()
            snake.append((GRID_WIDTH // 2, GRID_HEIGHT // 2))
            snake_direction = RIGHT
            snake_speed = 10
            level = 1
            food_to_next_level = 5
            foods_collected = 0
        else:
            snake.append(new_head)
            if new_head == food:
                foods_collected += 1
                if foods_collected == food_to_next_level:
                    level += 1
                    snake_speed += 2
                    food_to_next_level += 5
                food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            else:
                snake.pop(0)
        
        # Dibujar el juego
        SCREEN.fill(GREEN)
        for segment in snake:
            pygame.draw.rect(SCREEN, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(SCREEN, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Mostrar el nivel actual en pantalla
        font = pygame.font.Font(None, 24)
        text = font.render(f"Nivel: {level}", True, WHITE)
        SCREEN.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(snake_speed)

if __name__ == "__main__":
    main()