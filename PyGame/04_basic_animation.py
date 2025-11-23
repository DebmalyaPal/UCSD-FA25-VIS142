# -------------------------------
# Basic Animation
# -------------------------------
# GOAL:
# - Understand how to animate a shape in PyGame.
# - Understand how to move a rectangle across the screen.
# - Understand the concept of a "game loop" with frame updates.
#
# KEY IDEAS:
# - Animation = repeatedly update position + redraw screen.
# - Use a loop to keep the window open and update frames.
# - Clear the screen each frame, redraw shapes at new positions.
# - Control speed with pygame.time.Clock().
# -------------------------------

import pygame

# Initialize pygame
pygame.init()

# -------------------------------
# SCREEN SETUP
# -------------------------------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Animation in PyGame")

# Colors
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

# -------------------------------
# SHAPE SETUP
# -------------------------------
# We'll animate a rectangle moving across the screen.
rect_x = 50   # starting x position
rect_y = 250  # starting y position
rect_width = 100
rect_height = 60
rect_speed = 5  # pixels per frame

# Clock object to control frame rate
clock = pygame.time.Clock()

# -------------------------------
# GAME LOOP
# -------------------------------
# Instead of waiting a fixed time, we run a loop to update frames.
running = True
while running:
    # 1. Fill background each frame (clear old drawings)
    screen.fill(WHITE)

    # 2. Draw rectangle at current position
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # 3. Update display
    pygame.display.update()

    # 4. Move rectangle (update position)
    rect_x += rect_speed

    # 5. Bounce back if it hits screen edge
    if rect_x + rect_width > WIDTH or rect_x < 0:
        rect_speed = -rect_speed  # reverse direction

    # 6. Control frame rate (60 frames per second)
    clock.tick(60)

    # 7. Simple exit condition: run for ~5 seconds then quit
    #    (Normally you'd use events, but we skip that here.)
    if pygame.time.get_ticks() > 5000:  # milliseconds since start
        running = False

# -------------------------------
# CLEAN UP
# -------------------------------
pygame.quit()
