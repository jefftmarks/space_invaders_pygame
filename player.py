import pygame
from constants import *
from bullet import PlayerBullet

class Player(pygame.sprite.Sprite):
    """Spaceship controlled by user"""

    def __init__(self, bullet_group):
        """Initialize player object"""
        super().__init__()

        self.image = pygame.image.load('assets/player_ship.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = CENTER_X
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = STARTING_LIVES
        self.velocity = PLAYER_VELOCITY

        self.bullets = bullet_group

        self.shoot_sound = pygame.mixer.Sound('assets/player_fire.wav')

    def update(self):
        """Update player"""
        keys = pygame.key.get_pressed()

        # Move player within bounds of screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity

    def fire(self):
        """Fire bullet"""
        # Restrict number of bullets on screen at one time
        if len(self.bullets) < 2:
            self.shoot_sound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullets)

    def reset(self):
        """Reset player position"""
        self.rect.centerx = CENTER_X