import sys
import pygame
import random
import math
import settings
import iballs
import iblocks
import playballs

pygame.init()

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('FIELD')
clock = pygame.time.Clock()

blocks = []
for j in range(settings.Number_of_blocks):
    blocks.append(iblocks.Block(random.randint(0, settings.canvas_width), random.randint(0, settings.canvas_height),
                    random.randint(70, 120), random.randint(70, 120), random.randint(100, 150), random.randint(0, 50), random.randint(0, 50)))

ballplayer = playballs.Ball(settings.screen_width / 2, settings.screen_height / 2, 0, 0, settings.size, 0, 200, 120, 0, 0, settings.mass)
balls = []
for i in range(settings.Number_of_enemies):
    balls.append(iballs.Ball(random.randint(0, settings.canvas_width), random.randint(0, settings.canvas_height), random.randint(-70, 70),
                      random.randint(-70, 70), random.randint(5, 20), random.randint(100, 150),
                      random.randint(100, 150), random.randint(100, 150)))

while True:
    dt = clock.tick(50) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_0):
            sys.exit()


    for i in range(len(balls)):
        balls[i].update(dt, blocks)
    ballplayer.update(dt, playballs.Ball.acceleration_x(ballplayer), playballs.Ball.acceleration_y(ballplayer), blocks)

    for i in range(len(balls)):
        ballplayer.eat(balls[i], settings.relation)

    screen.fill((235, 235, 235))

    for i in range(len(balls)):
        if balls[i].radius > 0:
            balls[i].render(screen)
    ballplayer.render(screen)

    for i in range(len(blocks)):
        blocks[i].render(screen)

    pygame.display.flip()