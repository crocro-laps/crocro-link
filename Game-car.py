import pygame
import random
import sys

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de voiture")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Paramètres du jeu
car_width = 50
car_height = 80
obstacle_width = 50
obstacle_height = 80
speed = 5

# Initialisation de la voiture
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 10
car_speed = 0

# Initialisation des obstacles
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height

# Score
score = 0
font = pygame.font.SysFont(None, 35)

def show_score(score):
    """Affiche le score à l'écran."""
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over():
    """Affiche le message de fin de jeu."""
    text = font.render("Game Over!", True, RED)
    screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Boucle principale
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_speed = -5
            if event.key == pygame.K_RIGHT:
                car_speed = 5
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                car_speed = 0

    # Déplacement de la voiture
    car_x += car_speed
    if car_x < 0:
        car_x = 0
    if car_x > WIDTH - car_width:
        car_x = WIDTH - car_width

    # Déplacement de l'obstacle
    obstacle_y += speed
    if obstacle_y > HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        score += 1
        speed += 0.5  # Augmente la vitesse à chaque obstacle évité

    # Vérification de collision
    if (car_y < obstacle_y + obstacle_height and
        car_y + car_height > obstacle_y and
        car_x < obstacle_x + obstacle_width and
        car_x + car_width > obstacle_x):
        game_over()

    # Dessin de la voiture et de l'obstacle
    pygame.draw.rect(screen, BLUE, (car_x, car_y, car_width, car_height))
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Affichage du score
    show_score(score)

    # Rafraîchissement de l'écran
    pygame.display.flip()
    clock.tick(30)

pygame.quit()