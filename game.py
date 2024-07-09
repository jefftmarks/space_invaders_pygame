import pygame
from constants import *
from alien import Alien

class Game():
    """Controls and updates gameplay"""

    def __init__(self, window, player, alien_group, player_bullet_group, alien_bullet_group):
        """Initialize game object"""
        self.running = True

        self.round = STARTING_ROUND
        self.score = STARTING_SCORE 

        self.window = window
        self.player = player
        self.aliens = alien_group
        self.player_bullets = player_bullet_group
        self.alien_bullets = alien_bullet_group

        self.new_round_sound = pygame.mixer.Sound('assets/new_round.wav')
        self.breach_sound = pygame.mixer.Sound('assets/breach.wav')
        self.alien_hit_sound = pygame.mixer.Sound('assets/alien_hit.wav')
        self.player_hit_sound = pygame.mixer.Sound('assets/player_hit.wav')
        
        self.font = pygame.font.Font('assets/Facon.ttf', 32)

    def update(self):
        """Update game"""
        self.shift_aliens()
        self.check_collisions()
        self.check_round_completion()

    def draw(self):
        """Draw HUD and assets"""
        score_text = self.font.render("Score: " + str(self.score), True, Colors.WHITE)
        score_rect = score_text.get_rect()
        score_rect.centerx = CENTER_X
        score_rect.top = 10

        round_text = self.font.render("Round: " + str(self.round), True, Colors.WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (20, 10)

        lives_text = self.font.render("Lives: " + str(self.player.lives), True, Colors.WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH - 20, 10)

        self.window.blit(score_text, score_rect)
        self.window.blit(round_text, round_rect)
        self.window.blit(lives_text, lives_rect)

        pygame.draw.line(self.window, Colors.WHITE, (0, 50), (WINDOW_WIDTH, 50), 4)
        pygame.draw.line(self.window, Colors.WHITE, (0, BREACH_LINE), (WINDOW_WIDTH, BREACH_LINE), 4)


    def shift_aliens(self):
        """Shift wave of aliens down the screen"""
        # Determine if alien group hit edge
        shift = False
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0 or alien.rect.right >= WINDOW_WIDTH:
                shift = True
        
        # Shift every alien down, change direction, check for breach
        if shift:
            breach = False
            for alien in self.aliens.sprites():
                # Shift down
                alien.rect.y += 10 * self.round

                # Reverse direction
                alien.direction = -1 * alien.direction
                alien.rect.x += alien.direction * alien.velocity

                # Check if alien reached ship
                if alien.rect.bottom >= BREACH_LINE:
                    breach = True

            # Breach
            if breach:
                self.breach_sound.play()
                self.player.lives -= 1
                self.check_game_status(
                    "Aliens breached the line!",
                    "Press 'Enter' to continue"
                )
        
    def check_collisions(self):
        """Check for collisions"""
        # See if player bullet hit alien
        if pygame.sprite.groupcollide(self.player_bullets, self.aliens, True, True):
            self.alien_hit_sound.play()
            self.score += 100
        
        # See if alien bullet hits player
        if pygame.sprite.spritecollide(self.player, self.alien_bullets, True):
            self.player_hit_sound.play()
            self.player.lives -= 1
            
            if self.player.lives == 0:
                self.check_game_status(
                    "You've been hit!",
                    "Press 'Enter' to continue"
                )

    def check_round_completion(self):
        """Check to see if player completed single round"""
        if not self.aliens:
            self.score += 1000 * self.round
            self.round += 1
            
            self.start_new_round()

    def start_new_round(self):
        """Start new round"""
        for i in range(11):
            x = 64 + (i * 64)
            for j in range(5):
                y = 64 + (j * 64)
                alien = Alien(x, y, self.round, self.alien_bullets)
                self.aliens.add(alien)

        # Pause game
        self.new_round_sound.play()
        self.pause_game(
            "Space Invaders Round " + str(self.round),
            "Press 'Enter' to being"
        )
    
    def check_game_status(self, main_text, sub_text):
        """Check game status"""
        # Empty bullet groups and reset player and remaining aliens
        self.alien_bullets.empty()
        self.player_bullets.empty()

        self.player.reset()
        for alien in self.aliens:
            alien.reset()

        # Check if game over or round reset
        if self.player.lives == 0:
            self.reset_game()
        else:
            self.pause_game(main_text, sub_text)
        

    def pause_game(self, main_text, sub_text):
        """Pause game"""
        main_text = self.font.render(main_text, True, Colors.WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (CENTER_X, CENTER_Y)

        sub_text = self.font.render(sub_text, True, Colors.WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (CENTER_X, CENTER_Y + 64)

        self.window.fill(Colors.BLACK)
        self.window.blit(main_text, main_rect)
        self.window.blit(sub_text, sub_rect)

        pygame.display.update()

        # Pause game
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        paused = False
                if event.type == pygame.QUIT:
                    self.running = False
                    paused = False

    def reset_game(self):
        """Reset game"""
        self.pause_game(
            "Final Score: " + str(self.score),
            "Press 'Enter' to play again"
        )

        self.score = STARTING_SCORE
        self.round = STARTING_ROUND
        self.player.lives = STARTING_LIVES

        self.aliens.empty()
        self.alien_bullets.empty()
        self.player_bullets.empty()

        self.start_new_round()