class GameStats:
    """Track statistics for the game."""

    def __init__(self, ai_game):
        """Initialize stattistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Do not reset high score!
        self.high_score = 0

    def reset_stats(self):
        """Reset game's statistics, during the game as well."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
