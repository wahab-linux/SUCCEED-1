class Settings:
    """Store the settings for the minimum Alien Invasion starter."""

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        self.ship_speed = 4.0
        self.ship_color = (30, 90, 180)
        self.ship_width = 60
        self.ship_height = 35

        self.bullet_speed = 7.0
        self.bullet_width = 4
        self.bullet_height = 16
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.alien_speed = 1.2
        self.alien_width = 48
        self.alien_height = 32
        self.alien_color = (40, 150, 70)
        self.fleet_drop_speed = 12
        self.fleet_direction = 1
