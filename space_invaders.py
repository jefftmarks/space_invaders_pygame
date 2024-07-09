import pygame
from constants import *
from game import Game
from player import Player

pygame.init()

# Window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Clock
clock = pygame.time.Clock()

# Create bullet groups
player_bullet_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()

# Create player group and object
player_group = pygame.sprite.Group()
player = Player(player_bullet_group)
player_group.add(player)

# Create alien group and object
alien_group = pygame.sprite.Group()

# Game loop
game = Game(window, player, alien_group, player_bullet_group, alien_bullet_group)
game.start_new_round()

while game.running:
    for event in pygame.event.get():
        # Player quits
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()

    # Fill display
    window.fill(Colors.BLACK)

    # Update and display all sprite groups
    player_group.update()
    player_group.draw(window)

    alien_group.update()
    alien_group.draw(window)

    player_bullet_group.update()
    player_bullet_group.draw(window)

    alien_bullet_group.update()
    alien_bullet_group.draw(window)

    # Update and draw game object
    game.update()
    game.draw()
    
    # Update display and clock
    pygame.display.update()
    clock.tick(FPS)

# End game
pygame.quit()

