# -------------------------------
# ANIMATION: Circle start from centre and grows until it touches border,
#            Then the circle bursts into multiple smaller circles
# -------------------------------
# GOAL:
# - Animate a circle growing from the center.
# - Stop when it touches the screen border.
# - Burst into multiple small bubbles.
# -------------------------------

import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circle Burst Animation")

# Clock for frame rate control
clock = pygame.time.Clock()

# -------------------------------
# Circle class
# -------------------------------
class Circle:
    def __init__(self, centre_position, radius, colour, width=0):
        self.centre_position = centre_position
        self.radius = radius
        self.width = width   # width=0 means filled circle
        self.rgb = colour
    
    def increase(self, amount=1):
        self.radius += amount
    
    def move(self):
        # small vertical jitter for bubbles
        self.centre_position = (
            self.centre_position[0],
            self.centre_position[1] + random.randint(-1, 1)
        )

# -------------------------------
# Main growing circle
# -------------------------------
circle = Circle((SCREEN_WIDTH//2, SCREEN_HEIGHT//2), 0, (100, 200, 255), 1)

# Grow until it touches border
burst_triggered = False
while not burst_triggered:
    screen.fill((255, 255, 255))
    
    # Draw circle
    pygame.draw.circle(screen, circle.rgb, circle.centre_position, circle.radius, circle.width)
    
    # Increase radius
    circle.increase()
    
    pygame.display.update()
    clock.tick(60)
    
    # Check if circle touches border
    if (circle.centre_position[0] - circle.radius <= 0 or
        circle.centre_position[0] + circle.radius >= SCREEN_WIDTH or
        circle.centre_position[1] - circle.radius <= 0 or
        circle.centre_position[1] + circle.radius >= SCREEN_HEIGHT):
        burst_triggered = True

# -------------------------------
# Burst into multiple bubbles
# -------------------------------
random_circles = [
    Circle(
        (random.randint(50, SCREEN_WIDTH-50), random.randint(50, SCREEN_HEIGHT-50)),
        random.randint(5, 15),
        (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),
        0
    ) for _ in range(100)
]

# Animate bubbles for a few seconds
for frame in range(4*60):  # 5 seconds at 60 FPS
    screen.fill((255, 255, 255))
    
    for bubble in random_circles:
        pygame.draw.circle(screen, bubble.rgb, bubble.centre_position, bubble.radius, bubble.width)
        bubble.move()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
