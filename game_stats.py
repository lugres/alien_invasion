from pathlib import Path

HIGH_SCORE_FILE = "high_score.txt"


class GameStats:
    """Track statistics for the game."""

    def __init__(self, ai_game):
        """Initialize stattistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Do not reset high score!
        self.high_score = self.read_high_score()

    def reset_stats(self):
        """Reset game's statistics, during the game as well."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        """Reading high score from a file. If not available, return None."""
        self.path = Path(HIGH_SCORE_FILE)
        score = 0
        if self.path.exists():
            contents = self.path.read_text()
            try:
                score = int(contents)
            except ValueError:
                pass

        return score

    def save_high_score(self, high_score):
        """Saving high score to a file."""
        self.path.write_text(str(high_score))
