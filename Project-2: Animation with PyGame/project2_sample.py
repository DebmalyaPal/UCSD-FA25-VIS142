# Project 2 Sample Animation

import pygame
import random
import time

# -------------------------------
# Resolution (FHD 1920x1080)
# -------------------------------
width = 1920
height = 1080

# -------------------------------
# Name and Title
# -------------------------------
name = "Student Student"
title = "My Animation Theme"

# -------------------------------
# Normal pygame setup
# -------------------------------
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Project 2 Animation')
titles_font = pygame.font.SysFont(None, int(width/12))
name_f = titles_font.render(name, True, (255,255,255))
title_f = titles_font.render(title, True, (255,255,255))

# -------------------------------
# Classes for animation
# -------------------------------
class Bubble:
    def __init__(self, centre_position, radius, colour):
        self.centre_position = centre_position
        self.radius = radius
        self.rgb = colour
        self.x_speed = random.randint(-4, 4)
        self.y_speed = random.randint(-4, 4)
    
    def move(self):
        x, y = self.centre_position
        x += self.x_speed
        y += self.y_speed
        self.centre_position = (x, y)
        if x - self.radius <= 0 or x + self.radius >= width:
            self.x_speed = -self.x_speed
        if y - self.radius <= 0 or y + self.radius >= height:
            self.y_speed = -self.y_speed
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.rgb, self.centre_position, self.radius, 0)

# -------------------------------
# Helper: move rectangle toward center
# -------------------------------
center_x, center_y = width//2, height//2

def move_towards_center(rect, speed=3):
    x, y = rect.center
    dx = center_x - x
    dy = center_y - y
    if abs(dx) > speed:
        x += speed if dx > 0 else -speed
    else:
        x = center_x
    if abs(dy) > speed:
        y += speed if dy > 0 else -speed
    else:
        y = center_y
    rect.center = (x, y)

# -------------------------------
# Title Sequence (3 seconds)
# -------------------------------
for i in range(0, 3*60):
    screen.fill((0,0,0))
    screen.blit(name_f, (int(width/8), int(height/8)))
    screen.blit(title_f, (int(width/8), int(height/4)))
    pygame.display.update()
    clock.tick(60)

# -------------------------------
# Main Animation (20 seconds)
# -------------------------------
# Rectangles setup
rect1 = pygame.Rect(0, 0, 100, 60)
rect2 = pygame.Rect(width-100, 0, 100, 60)
rect3 = pygame.Rect(width-100, height-60, 100, 60)
rect4 = pygame.Rect(0, height-60, 100, 60)

circle_radius = 0
burst_triggered = False
bubbles = []

for i in range(0, 20*60):  # 20 seconds
    screen.fill((0,0,0))

    # Phase 1: Rectangles move to center (~5s)
    if i < 5*60:
        for r, color in zip([rect1, rect2, rect3, rect4],
                            [(255,0,0), (0,255,0), (0,0,255), (255,255,0)]):
            pygame.draw.rect(screen, color, r)
            move_towards_center(r, speed=3)

    # Phase 2: Circle grows until border (~3s)
    elif not burst_triggered:
        pygame.draw.circle(screen, (100,200,255), (center_x, center_y), circle_radius, 0)
        circle_radius += 12
        if (center_x - circle_radius <= 0 or center_x + circle_radius >= width or
            center_y - circle_radius <= 0 or center_y + circle_radius >= height):
            burst_triggered = True
            bubbles = [
                Bubble(
                    (random.randint(100, width-100), random.randint(100, height-100)),
                    random.randint(5, 20),
                    (random.randint(50,255), random.randint(50,255), random.randint(50,255))
                )
                for _ in range(50)
            ]

    # Phase 3: Bubbles bounce (remaining time)
    else:
        for bubble in bubbles:
            bubble.move()
            bubble.draw(screen)

    pygame.display.update()
    clock.tick(60)

# -------------------------------
# Quit Application
# -------------------------------
pygame.quit()
