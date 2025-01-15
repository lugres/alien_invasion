class GameStats:
    """Track statistics for the game."""

    def __init__(self, ai_game):
        """Initialize stattistics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Reset game's statistics, during the game as well."""
        self.ships_left = self.settings.ship_limit
