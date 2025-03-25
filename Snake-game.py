import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Direction initiale
direction = "RIGHT"
change_to = direction

# Position initiale du serpent
snake_pos = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE, 
            random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE]
food_spawn = True
score = 0

# Vitesse du jeu
clock = pygame.time.Clock()
speed = 10

def show_score():
    """Affiche le score en haut de l'écran."""
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over():
    """Affiche le message de fin de jeu et quitte après un délai."""
    font = pygame.font.Font(None, 50)
    text = font.render(f"Game Over! Score: {score}", True, RED)
    screen.blit(text, (WIDTH//4, HEIGHT//3))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    quit()

# Boucle du jeu
running = True
while running:
    screen.fill(BLACK)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    # Mise à jour de la direction
    direction = change_to

    # Déplacement du serpent
    if direction == "UP":
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] - CELL_SIZE])
    elif direction == "DOWN":
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] + CELL_SIZE])
    elif direction == "LEFT":
        snake_pos.insert(0, [snake_pos[0][0] - CELL_SIZE, snake_pos[0][1]])
    elif direction == "RIGHT":
        snake_pos.insert(0, [snake_pos[0][0] + CELL_SIZE, snake_pos[0][1]])

    # Vérification de la collision avec la nourriture
    if snake_pos[0] == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_pos.pop()  # Le serpent grandit uniquement s'il mange

    # Génération d'une nouvelle nourriture
    if not food_spawn:
        food_pos = [random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE, 
                    random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE]
        food_spawn = True

    # Vérification des collisions avec les bords ou soi-même
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or
        snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT or
        snake_pos[0] in snake_pos[1:]):
        game_over()

    # Dessin du serpent et de la nourriture
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    # Affichage du score
    show_score()

    # Rafraîchissement de l'affichage
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()