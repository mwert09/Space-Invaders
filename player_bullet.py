import pygame

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 2
        self.screen = screen
        self.bullet_rect = pygame.Rect(self.x, self.y, 4, 8)

    def draw(self):
        pygame.draw.rect(self.screen, (254,52,110), self.bullet_rect)

    def move(self):
        self.bullet_rect.y -= self.speed

    def handleCollisions(self, enemy):
        return self.bullet_rect.colliderect(enemy.player_rect)