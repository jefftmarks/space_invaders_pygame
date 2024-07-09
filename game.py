class Game():
    """Controls and updates gameplay"""

    def __init__(self):
        """Initialize game object"""
        self.running = True

    def update(self):
        """Update game"""
        pass

    def draw(self):
        """Draw HUD and assets"""
        pass

    def shift_aliens(self):
        """Shift wave of aliens down the screen"""
        pass

    def check_collisions(self):
        """Check for collisions"""
        pass

    def check_round_completion(self):
        """Check to see if player completed single round"""

    def start_new_round(self):
        """Start new round"""
        pass
    
    def check_game_status(self):
        """Check game status"""
        pass

    def pause_game(self):
        """Pause game"""
        pass

    def reset_game(self):
        """Reset game"""
        pass