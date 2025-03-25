import pygame
import sys

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
screen_width = 800
screen_height = 600

# Couleurs
background_color = (50, 50, 50)  # Gris foncé
grid_color = (30, 30, 30)        # Gris plus foncé
snake_color = (0, 255, 0)        # Vert
food_color = (255, 0, 0)         # Rouge

# Taille de la grille
cell_size = 20

# Création de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game avec Fond d'écran")

# Fonction pour dessiner le fond avec une grille
def draw_background():
    screen.fill(background_color)
    for x in range(0, screen_width, cell_size):
        pygame.draw.line(screen, grid_color, (x, 0), (x, screen_height))
    for y in range(0, screen_height, cell_size):
        pygame.draw.line(screen, grid_color, (0, y), (screen_width, y))

# Boucle principale
clock = pygame.time.Clock()
snake = [(100, 100), (120, 100), (140, 100)]  # Exemple de serpent
food = (200, 200)  # Exemple de nourriture

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dessiner le fond
    draw_background()

    # Dessiner le serpent
    for segment in snake:
        pygame.draw.rect(screen, snake_color, (*segment, cell_size, cell_size))

    # Dessiner la nourriture
    pygame.draw.rect(screen, food_color, (*food, cell_size, cell_size))

    # Mettre à jour l'affichage
    pygame.display.flip()
    clock.tick(10)