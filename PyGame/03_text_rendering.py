# -------------------------------
# 03_text_rendering.py
# -------------------------------
# GOAL:
# - Understand how to render and display text in PyGame.
# - fonts, sizes, colors, antialiasing, positioning, and centering.
#
# KEY IDEAS:
# - You don't "print" to the screen; you RENDER text into a Surface, then BLIT it to the window.
# - Steps: create Font -> render text (to a Surface) -> blit onto screen -> update display.
# - Antialiasing smooths edges (True/False as first parameter in render()).
# - Colors are RGB tuples, same as shapes.
# - Positioning uses pixel coordinates: top-left is (0, 0).
#
# COMMON METHODS:
# - pygame.font.Font(None, size)         -> default system font
# - pygame.font.Font("path.ttf", size)   -> custom TTF font file
# - font.render(text, antialias, color)  -> returns a text Surface
# - surface.get_rect()                   -> get rectangle for positioning (center, top-left, etc.)
# - screen.blit(surface, (x, y))         -> draw the text surface onto the screen
# - pygame.display.update()              -> show changes
# -------------------------------

import pygame

# Initialize pygame (includes font subsystem)
pygame.init()

# -------------------------------
# SCREEN SETUP
# -------------------------------
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text Rendering in PyGame")

# Background color
BG = (245, 245, 245)   # light gray
screen.fill(BG)

# -------------------------------
# FONTS
# -------------------------------
# 1) Default system font: pass None
default_font_small  = pygame.font.Font(None, 24)
default_font_medium = pygame.font.Font(None, 36)
default_font_large  = pygame.font.Font(None, 64)

# 2) Custom font file (optional)
#    If you have a TTF file in your project (e.g., assets/Roboto-Regular.ttf), uncomment below:
# custom_font = pygame.font.Font("assets/Roboto-Regular.ttf", 32)

# -------------------------------
# COLORS
# -------------------------------
BLACK = (0, 0, 0)
BLUE  = (0, 120, 255)
RED   = (255, 60, 60)
GREEN = (60, 180, 75)

# -------------------------------
# RENDER TEXT -> GET SURFACE
# -------------------------------
# font.render(text, antialias(True/False), color)
title_surface   = default_font_large.render("PyGame Text Rendering", True, BLACK)
subtitle_surface = default_font_medium.render("Render -> Blit -> Update", True, BLUE)
note_surface    = default_font_small.render("Antialiasing makes edges smoother.", True, RED)

# Multiple lines with different colors/sizes
line1 = default_font_small.render("This is a small line of text.", True, BLACK)
line2 = default_font_small.render("Colors are RGB tuples like (r, g, b).", True, GREEN)
line3 = default_font_small.render("Position uses pixel coordinates from top-left.", True, BLACK)

# -------------------------------
# POSITIONING
# -------------------------------
# Use get_rect() to position text easily (center, midtop, etc.)
# Center the title near the top:
title_rect = title_surface.get_rect(center=(400, 80))         # 400 = screen width / 2
subtitle_rect = subtitle_surface.get_rect(center=(400, 140))
note_rect = note_surface.get_rect(center=(400, 180))

# Place lines using top-left coordinates (x, y):
line1_rect = line1.get_rect(topleft=(50, 260))
line2_rect = line2.get_rect(topleft=(50, 300))
line3_rect = line3.get_rect(topleft=(50, 340))

# -------------------------------
# BLIT (DRAW) TEXT SURFACES
# -------------------------------
# Blit = copy the text surface onto the screen surface
screen.blit(title_surface, title_rect)
screen.blit(subtitle_surface, subtitle_rect)
screen.blit(note_surface, note_rect)

screen.blit(line1, line1_rect)
screen.blit(line2, line2_rect)
screen.blit(line3, line3_rect)

# -------------------------------
# UPDATE DISPLAY
# -------------------------------
pygame.display.update()

# -------------------------------
# KEEP WINDOW OPEN
# -------------------------------
# We are not using events; just pause so you can see the text.
pygame.time.wait(5000)

pygame.quit()
