# -------------------------------
# ANIMATION: 4 Rectangles starting from 4 corners and moving diagonally towards center
# -------------------------------
# GOAL:
# - Animate four rectangles moving diagonally from each corner.
# - Use clock.tick() for smooth frame rate.
# - Use time-based exit condition instead of manual counter.
# -------------------------------

import pygame

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Diagonal Rectangles Animation")

# Clock for frame rate control
clock = pygame.time.Clock()

# Rectangles starting at each corner
rectangle1 = pygame.Rect(0, 0, 50, 30)                # top-left
rectangle2 = pygame.Rect(SCREEN_WIDTH-50, 0, 50, 30)  # top-right
rectangle3 = pygame.Rect(SCREEN_WIDTH-50, SCREEN_HEIGHT-30, 50, 30)  # bottom-right
rectangle4 = pygame.Rect(0, SCREEN_HEIGHT-30, 50, 30) # bottom-left

# Run for a fixed number of frames (e.g., 480 frames ≈ 8 seconds at 60 FPS)
for frame in range(8*60):
    # Background color cycling
    screen.fill((255 - (frame % 255), frame % 255, 255 - (frame % 255)))

    # Draw rectangles
    pygame.draw.rect(screen, (255, 0, 255), rectangle1)
    pygame.draw.rect(screen, (255, 0, 255), rectangle2)
    pygame.draw.rect(screen, (255, 0, 255), rectangle3)
    pygame.draw.rect(screen, (255, 0, 255), rectangle4)

    # Move rectangles diagonally
    rectangle1.move_ip(1, 1)   # down-right
    rectangle2.move_ip(-1, 1)  # down-left
    rectangle3.move_ip(-1, -1) # up-left
    rectangle4.move_ip(1, -1)  # up-right

    # Update display
    pygame.display.update()

    # Control frame rate (60 FPS)
    clock.tick(60)

# Quit pygame
pygame.quit()