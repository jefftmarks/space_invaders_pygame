import pygame, random
from bullet import AlienBullet

class Alien(pygame.sprite.Sprite):
    """Enemy alien object"""

    def __init__(self, x, y, velocity, bullet_group):
        """Initialize alien object"""
        super().__init__()

        self.image = pygame.image.load('assets/alien.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.starting_x = x
        self.starting_y = y

        self.direction = 1
        self.velocity = velocity

        self.bullets = bullet_group

        self.shoot_sound = pygame.mixer.Sound('assets/alien_fire.wav')

    def update(self):
        """Update alien"""
        self.rect.x += self.direction * self.velocity

        # random fire bullet
        if random.randint(0, 1000) > 999 and len(self.bullets) < 3:
            self.shoot_sound.play()
            self.fire()

    def fire(self):
        """Fire bullet"""
        AlienBullet(self.rect.centerx, self.rect.bottom, self.bullets)

    def reset(self):
        """Reset alien position"""
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1