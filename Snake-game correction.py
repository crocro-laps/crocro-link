import pygame
import time
import random

# Initialisation de pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (213, 50, 80)
VERT = (0, 255, 0)
BLEU = (50, 153, 213)

# Dimensions de la fenêtre
largeur = 600
hauteur = 400

# Taille des blocs du serpent
taille_bloc = 10
vitesse_snake = 15

# Police
font_style = pygame.font.SysFont("bahnschrift", 25)

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu du Serpent")

# Fonction pour dessiner le serpent
def dessiner_serpent(taille_bloc, liste_serpent):
    for bloc in liste_serpent:
        pygame.draw.rect(fenetre, NOIR, [bloc[0], bloc[1], taille_bloc, taille_bloc])

# Fonction pour afficher le message de fin
def message(msg, couleur, x, y):
    texte = font_style.render(msg, True, couleur)
    fenetre.blit(texte, [x, y])

# Fonction principale
def jeu():
    game_over = False
    game_close = False

    # Position initiale du serpent
    x = largeur / 2
    y = hauteur / 2

    # Direction initiale
    x_change = 0
    y_change = 0

    # Corps du serpent
    liste_serpent = []
    longueur_serpent = 1

    # Position initiale de la nourriture
    nourriture_x = round(random.randrange(0, largeur - taille_bloc) / 10.0) * 10.0
    nourriture_y = round(random.randrange(0, hauteur - taille_bloc) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            fenetre.fill(BLANC)
            message("Game Over ! Appuyez sur C pour rejouer ou Q pour quitter", ROUGE, 50, hauteur / 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jeu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -taille_bloc
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = taille_bloc
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -taille_bloc
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = taille_bloc
                    x_change = 0

        # Vérifier si le serpent touche les bords
        if x >= largeur or x < 0 or y >= hauteur or y < 0:
            game_close = True

        x += x_change
        y += y_change

        fenetre.fill(BLEU)
        pygame.draw.rect(fenetre, VERT, [nourriture_x, nourriture_y, taille_bloc, taille_bloc])

        # Mettre à jour le corps du serpent
        tete_serpent = []
        tete_serpent.append(x)
        tete_serpent.append(y)
        liste_serpent.append(tete_serpent)

        if len(liste_serpent) > longueur_serpent:
            del liste_serpent[0]

        # Vérifier si le serpent se mord lui-même
        for segment in liste_serpent[:-1]:
            if segment == tete_serpent:
                game_close = True

        dessiner_serpent(taille_bloc, liste_serpent)

        pygame.display.update()

        # Vérifier si le serpent mange la nourriture
        if x == nourriture_x and y == nourriture_y:
            nourriture_x = round(random.randrange(0, largeur - taille_bloc) / 10.0) * 10.0
            nourriture_y = round(random.randrange(0, hauteur - taille_bloc) / 10.0) * 10.0
            longueur_serpent += 1

        clock.tick(vitesse_snake)

    pygame.quit()
    quit()

jeu()
 
