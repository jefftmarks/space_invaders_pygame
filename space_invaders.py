import pygame
from constants import *
from game import Game

pygame.init()

# Window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Clock
clock = pygame.time.Clock()

# Game loop
game = Game()

while game.running:
    # Player quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
    
    # Update display and clock
    pygame.display.update()
    clock.tick(FPS)

# End game
pygame.quit()

