#This part has been coded by Saad Al-Mansoori.

import pygame

class Scoreboard:
    """
    Display and manage the players score.
    """

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()


        # Styling
        self.score = 0
        self.text_color = (30,30,30)
        self.font = pygame.font.Font(None, 36)
        self._prepare_score()

    def _prepare_score(self):
        """
        Turn the current score into an image.
        """
        score_text = f"Score: {self.score}"

        self.score_image = self.font.render(
            score_text,
            True,
            self.text_color
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 20
        self.score_rect.right = self.screen_rect.right - 20

    def add_points(self, points):
        """
        Increase the score and update the displayed image.
        """
        self.score += points
        self._prepare_score()

    def draw_score(self):
        """
        Draw the score onto the screen.
        """
        self.screen.blit(self.score_image, self.score_rect)

    def draw_lives(self, lives):
        lives_text = f"Lives: {lives}"

        lives_image = self.font.render(
            lives_text,
            True,
            self.text_color
        )

        lives_rect = lives_image.get_rect()
        lives_rect.top = 20
        lives_rect.left = 20

        self.screen.blit(lives_image, lives_rect)

    def draw_failed(self):
        failed_image = self.font.render(
            "GAME OVER",
            True,
            self.text_color
        )

        failed_rect = failed_image.get_rect()
        failed_rect.center = self.screen_rect.center

        self.screen.blit(failed_image, failed_rect)