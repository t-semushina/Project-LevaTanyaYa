import sys
import pygame
import random
import math
import settings


class Ball:
    def __init__(self, x, y, vx, vy, radius, r, g, b):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b

    def update(self, dt, blocks):

        self.x += self.vx * dt
        self.y += self.vy * dt
        if (self.x >= settings.canvas_width - self.radius):
            self.x -= self.radius + self.x - settings.canvas_width
            self.vx = -self.vx
        if (self.x <= self.radius):
            self.x += self.radius - self.x
            self.vx = -self.vx
        if (self.y >= settings.canvas_height - self.radius):
            self.y -= self.radius + self.y - settings.canvas_height
            self.vy = -self.vy
        if (self.y <= self.radius):
            self.y += self.radius - self.y
            self.vy = -self.vy



    def eat(self, ball):
        if ((ball.x - self.x) ** 2 + (self.y - ball.y) ** 2 <= (ball.radius + self.radius) ** 2) and (
                ball.radius < self.radius):
            if self.radius < settings.max_rad:
                self.radius = math.sqrt(self.radius **2 + ball.radius ** 2)
            ball.radius = 0

    def render(self, screen):
        pygame.draw.circle(screen, (self.r, self.g, self.b), (int(self.x), int(self.y)), int(self.radius))