# -------------------------------
# ANIMATION: Bouncing bubbles
# -------------------------------
# GOAL:
# - Animate multiple circles bouncing around the screen.
# - Each circle has random position, size, color, and speed.
# - Circles bounce when they hit the screen edges.
# -------------------------------

import pygame
import random

# Initialize Pygame
pygame.init()

# -------------------------------
# SCREEN SETUP
# -------------------------------
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Circles")

# Clock to control frame rate
clock = pygame.time.Clock()

# -------------------------------
# Circle CLASS
# -------------------------------
class Circle:
    def __init__(self, centre_position, radius, colour, width=0):
        # Circle properties
        self.centre_position = centre_position
        self.radius = radius
        self.width = width        # 0 = filled circle, >0 = border thickness
        self.rgb = colour

        # Random speed in both directions
        self.x_speed = random.randint(1, 4)
        self.y_speed = random.randint(1, 4)
    
    def move(self):
        """Move circle and bounce off edges."""
        # Update position
        x, y = self.centre_position
        x += self.x_speed
        y += self.y_speed
        self.centre_position = (x, y)

        # Bounce horizontally
        if x - self.radius <= 0 or x + self.radius >= SCREEN_WIDTH:
            self.x_speed = -self.x_speed

        # Bounce vertically
        if y - self.radius <= 0 or y + self.radius >= SCREEN_HEIGHT:
            self.y_speed = -self.y_speed
    
    def draw(self, surface):
        """Draw circle on given surface."""
        pygame.draw.circle(surface, self.rgb, self.centre_position, self.radius, self.width)

# -------------------------------
# CREATE MULTIPLE RANDOM CIRCLES
# -------------------------------
random_circles = [
    Circle(
        (random.randint(50, SCREEN_WIDTH-50), random.randint(50, SCREEN_HEIGHT-50)), # random position
        random.randint(10, 30),                                                     # random radius
        (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),# random color
        0                                                                           # filled circle
    )
    for _ in range(30)  # number of circles
]

# -------------------------------
# FOR-LOOP BASED ON DURATION
# -------------------------------
seconds = 10       # run for 10 seconds
fps = 60           # frames per second
total_frames = seconds * fps

for frame in range(total_frames):
    # Fill background
    screen.fill((255, 255, 255))

    # Move and draw circles
    for circle in random_circles:
        circle.move()
        circle.draw(screen)

    # Update display
    pygame.display.update()

    # Control frame rate
    clock.tick(fps)

# -------------------------------
# Quit Application
# -------------------------------
pygame.quit()
