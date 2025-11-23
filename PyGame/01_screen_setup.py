# -------------------------------
# SCREEN SETUP
# -------------------------------
# GOAL:
# - Initialize PyGame
# - Set up screen size
# - Add headline/caption to the window
# - Work with colors (RGB)
# - Fill background with chosen color
#
# WHY:
# These are the building blocks for any animation project.
# Before drawing shapes or animating, you need a canvas (screen),
# a title (caption), and a way to control colors.
# -------------------------------

import pygame

# Initialize pygame
pygame.init()

# -------------------------------
# SCREEN SETUP
# -------------------------------
# Set screen size (width, height)
screen = pygame.display.set_mode((800, 600))  # Observe: Tuple (width, height)

# -------------------------------
# HEADLINE / CAPTION
# -------------------------------
# Set the window caption (appears in title bar)
pygame.display.set_caption("My First PyGame Window")

# -------------------------------
# COLORS
# -------------------------------
# Colors are defined using RGB values (Red, Green, Blue)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0,   255,   0)
BLUE  = (0,     0, 255)
LIGHT_BLUE = (200, 200, 255)

# Fill background with a color
screen.fill(LIGHT_BLUE)

# Update display so color shows
pygame.display.update()

# -------------------------------
# KEEP WINDOW OPEN
# -------------------------------
# Wait for a few seconds before quitting
pygame.time.wait(10000)

# Quit pygame safely
pygame.quit()
