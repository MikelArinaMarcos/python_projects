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
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)

# Direccionamientos
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Función para mostrar mensaje y esperar antes de continuar
def show_message(message, font_size=36):
    font = pygame.font.Font(None, font_size)
    text = font.render(message, True, WHITE)
    SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    time.sleep(2)

# Función para dibujar el texto en la pantalla
def draw_text(text, font_size, x, y):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, WHITE)
    SCREEN.blit(text_surface, (x, y))

# Función para mostrar el menú de inicio
def show_menu():
    SCREEN.fill(GREEN)
    draw_text("¡Bienvenido a Snake!", 48, WIDTH // 2 - 200, HEIGHT // 2 - 100)
    draw_text("Presiona ENTER para comenzar", 24, WIDTH // 2 - 160, HEIGHT // 2 + 50)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

# Función para comprobar colisiones
def check_collision(snake):
    head_x, head_y = snake[-1]
    return head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT or (head_x, head_y) in snake[:-1]

# Función para jugar un nivel
def play_level(level):
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_direction = RIGHT
    snake_speed = 10 + level * 2
    snake_growth = 0
    food_type = random.choice([RED, BLUE, ORANGE, WHITE])
    if food_type == WHITE:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        food = (random.randint(2, GRID_WIDTH - 3), random.randint(2, GRID_HEIGHT - 3))
    food_to_next_level = 5 + level * 5
    foods_collected = 0
    score = 0

    obstacles = [(2, 5), (5, 2), (GRID_WIDTH - 3, GRID_HEIGHT - 6), (GRID_WIDTH - 6, GRID_HEIGHT - 3)]

    clock = pygame.time.Clock()

    while True:
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
        new_head = (head_x + dx, head_y + dy)

        if check_collision(snake) or new_head in obstacles:
            return score
        else:
            snake.append(new_head)
            if new_head == food:
                foods_collected += 1
                if food_type == WHITE:
                    score += 50
                elif food_type == ORANGE:
                    score += 30
                elif food_type == BLUE:
                    score += 20
                else:
                    score += 10 * level
                snake_growth += 1

                if foods_collected == food_to_next_level:
                    return score
                food_type = random.choice([RED, BLUE, ORANGE, WHITE])
                if food_type == WHITE:
                    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                else:
                    food = (random.randint(2, GRID_WIDTH - 3), random.randint(2, GRID_HEIGHT - 3))
            else:
                if snake_growth > 0:
                    snake_growth -= 1
                else:
                    snake.pop(0)

        # Dibujar el juego
        SCREEN.fill(GREEN)
        for segment in snake:
            pygame.draw.rect(SCREEN, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        for obstacle in obstacles:
            pygame.draw.rect(SCREEN, GRAY, (obstacle[0] * GRID_SIZE, obstacle[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(SCREEN, food_type, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        draw_text(f"Nivel: {level}", 24, 10, 10)
        draw_text(f"Puntuación: {score}", 24, 10, 40)
        pygame.display.flip()
        clock.tick(snake_speed)

def main():
    show_menu()
    high_score = 0
    level = 1

    while True:
        score = play_level(level)
        if score > high_score:
            high_score = score

        show_message(f"¡Perdiste! Puntuación: {score} | Récord: {high_score}", font_size=30)
        level += 1

if __name__ == "__main__":
    main()
