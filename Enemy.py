import pygame
from enemy_bullet import EnemyBullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 5
        self.screen = screen
        self.move_left_counter = 0
        self.player_sprite = pygame.image.load("imgs/enemy.png")
        self.player_sprite = pygame.transform.scale(self.player_sprite, (30, 30))
        self.player_rect = pygame.Rect(self.x, self.y, 30, 30)

    def draw(self):
        self.screen.blit(self.player_sprite, self.player_rect)

    def move(self):
        if self.move_left_counter < 30:
            self.move_left()
            self.move_left_counter += 1
        elif self.move_left_counter >= 30 and self.move_left_counter < 90:
            self.move_right()
            self.move_left_counter += 1
        elif self.move_left_counter >= 90 and self.move_left_counter < 120:
            self.move_left()
            self.move_left_counter += 1
        elif self.move_left_counter == 120:
            self.move_left_counter = 0

    def move_left(self):
        self.player_rect.x -= self.speed
    def move_right(self):
        self.player_rect.x += self.speed

    def fire(self):
        bullet = EnemyBullet(self.screen, self.player_rect.x, self.player_rect.y - 20)
        return bullet







