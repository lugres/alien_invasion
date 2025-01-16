class Settings:
    """A class to store all settings for Alien Invasion game."""

    def __init__(self):
        """Initilize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly a game speeds up
        self.speed_up_scale = 1.2

        self.difficulty_level = "medium"

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        if self.difficulty_level == "easy":
            self.ship_speed = 1.5
            self.bullet_speed = 1.5
            self.alien_speed = 1.0
        elif self.difficulty_level == "medium":
            self.ship_speed = 2.5
            self.bullet_speed = 3.0
            self.alien_speed = 2.0
        elif self.difficulty_level == "hard":
            self.ship_speed = 4.5
            self.bullet_speed = 6.0
            self.alien_speed = 4.0

        # fleet_direction of 1 means right; -1 means left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale

    def set_difficulty(self, diff_setting):
        """Display difficulty level"""
        if diff_setting == "easy":
            print("easy")
        if diff_setting == "medium":
            print("medium")
        if diff_setting == "hard":
            print("hard")
