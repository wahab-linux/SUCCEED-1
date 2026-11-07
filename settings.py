class Settings:
    # Set Values in a Class, faster lookup than typical data structures
    def __init__(self):
        # Screen
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship
        self.ship_width = 60
        self.ship_height = 35
        self.ship_color = (30, 90, 180)
        self.ship_speed = 4.0

        # Bullet
        self.bullet_width = 4
        self.bullet_height = 16
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 7.0
        self.bullets_allowed = 3

        # Alien
        self.alien_width = 48
        self.alien_height = 32
        self.alien_color = (40, 150, 70)
        self.alien_speed = 1.2
        self.fleet_drop_speed = 12
        self.fleet_direction = 1
        self.alien_points = 50