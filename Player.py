import pygame
from player_bullet import PlayerBullet

class Player:
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 3
        self.x = x
        self.y = y
        self.speed = 2
        self.screen = screen
        self.firable = True
        self.bullets = []
        self.score = 0
        self.player_sprite = pygame.image.load("imgs/player.png")
        self.player_sprite = pygame.transform.scale(self.player_sprite, (30, 30))
        self.player_rect = pygame.Rect(self.x, self.y, 30, 30)

    def draw(self):
        self.screen.blit(self.player_sprite, self.player_rect)

    def move_left(self):
        if self.player_rect.left > 30:
            self.player_rect.x -= self.speed

    def move_right(self):
        if self.player_rect.right < 770:
            self.player_rect.x += self.speed

    def fire(self):
        if self.firable:
            bullet = PlayerBullet(self.screen, self.player_rect.x, self.player_rect.y - 20)
            self.bullets.append(bullet)
            self.firable = False

    def increase_score(self, amount):
        self.score += amount

