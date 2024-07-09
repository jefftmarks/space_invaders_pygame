import pygame
from constants import *

class Bullet(pygame.sprite.Sprite):
    """Projectile object"""

    def __init__(self, x, y, image, bullet_group):
        """Initialize bullet"""
        super().__init__()

        self.x = x
        self.y = y
        self.bullets = bullet_group

        self.rect = image.get_rect()
        self.rect.center = (x, y)

        self.velocity = 10

        self.bullets.add(self)

class PlayerBullet(Bullet):
    """Player bullet"""

    def __init__(self, x, y, bullet_group):
        """Initialize bullet"""
        self.image = pygame.image.load('assets/green_laser.png')

        super().__init__(x, y , self.image, bullet_group)

    def update(self):
        """Update bullet"""
        self.rect.y -= self.velocity

        # If bullet off screen, kill it
        if self.rect.bottom < 0:
            self.kill()

class AlienBullet(Bullet):
    """Alien bullet"""

    def __init__(self, x, y, bullet_group):
        """Initialize bullet"""
        self.image = pygame.image.load('assets/red_laser.png')

        super().__init__(x, y, self.image, bullet_group)

    def update(self):
        """Update bullet"""
        self.rect.y += self.velocity

        # If bullet off screen, kill it
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()