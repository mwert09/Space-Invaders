import sys, pygame
from Player import Player
from Enemy import Enemy
import random

# Iniitialize pygame
pygame.init()
pygame.font.init()


myfont = pygame.font.SysFont('Arial', 20)



pygame.display.set_caption("Space Invaders")
# Background color
black = 0, 0, 0
# Screen resolution size
size = width, height = 800, 600
# Set resolution
screen = pygame.display.set_mode(size)
# Clock
clock = pygame.time.Clock()

# Events
move_side_event = pygame.USEREVENT + 1
enemy_shoot_event = pygame.USEREVENT + 2

# Timer
pygame.time.set_timer(move_side_event, 100)
pygame.time.set_timer(enemy_shoot_event, 1200)

# Player
player = Player(screen, width / 2, height - 40)

# Enemies
enemies_list = []
bullets = []
for i in range(5,13):
    for y in range(2,5):
        enemy = Enemy(screen, i * 45, y * 40)
        enemies_list.append(enemy)


game_loop = True
while game_loop:
    # Lock fps to 60
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        elif event.type == move_side_event:
            for enemy in enemies_list:
                enemy.move()
        elif event.type == enemy_shoot_event:
            random_enemy = random.choice(enemies_list)
            bullets.append(random_enemy.fire())



    # Handle Movement and Shooting
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move_left()
    elif key[pygame.K_RIGHT]:
        player.move_right()
    elif key[pygame.K_SPACE]:
        player.fire()

    screen.fill(black)

    # Draw player on the screen
    player.draw()

    # Draw enemis
    for enemy in enemies_list:
        enemy.draw()

    for bullet in player.bullets:
        bullet.draw()
        bullet.move()
        for enemy in enemies_list:
            if bullet.handleCollisions(enemy):
                player.increase_score(10)
                bullet.kill()
                player.bullets.pop()
                player.firable = True
                enemy.kill()
                enemies_list.remove(enemy)
    for bullet in bullets:
        bullet.draw()
        bullet.move()
        if bullet.handleCollisions(player):
            bullet.kill()
            bullets.remove(bullet)
            player.lives -= 1
            if player.lives == 0:
                game_loop = False

    textsurface = myfont.render('Score: ' + str(player.score) + "              Lives: " + str(player.lives), False, (0, 255, 0))
    screen.blit(textsurface, (30, 10))
    pygame.draw.line(screen, (255, 255, 255), (30, 40), (770, 40))
    pygame.display.flip()

print("Game Over")
pygame.quit()
sys.exit()

