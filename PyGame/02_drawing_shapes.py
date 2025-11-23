# -------------------------------
# DRAWING SHAPES
# -------------------------------
# GOAL:
# - Understand how to draw basic shapes in PyGame: rectangle, circle, line, polygon.
#   Two approaches:
#     (1) Direct syntax with pygame.draw functions
#     (2) Object-based syntax using pygame.Rect class (only for Rectangle)
#   Pros & Cons:
#     - Direct syntax is quick for static shapes.
#     - Rect objects are useful when you want to move, resize, or check collisions.
# - Understand how to position shapes using coordinates.
# - Demonstrate layering (drawing multiple shapes).
#
# WHY:
# Drawing shapes is the foundation of animation.
# Once you know how to place and color shapes,
# you can move them around to create motion.
# -------------------------------

import pygame

# Initialize pygame
pygame.init()

# -------------------------------
# SCREEN SETUP
# -------------------------------
# Create a window (width=800, height=600)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Shapes in PyGame")

# Define colors (RGB)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0,   255,   0)
BLUE  = (0,     0, 255)
YELLOW = (255, 255,   0)

# Fill background with white
screen.fill(WHITE)

# -------------------------------
# KEY NOTES FOR STUDENTS:
# - Coordinates: (x, y) starts with (0,0) from the top-left corner of the window.
# - Rectangle: needs (x, y, width, height).
# - Circle: needs (center_x, center_y, radius).
# - Line: needs start and end points, plus thickness.
# - Polygon: needs a list of points.
# - Layering: Shapes are drawn in the order you call them, later shapes appear on top of earlier ones.
# -------------------------------

# -------------------------------
# DRAWING SHAPES
# -------------------------------

# -------------------------------
# APPROACH 1: DIRECT SYNTAX
# -------------------------------

# 1. Rectangle
# Syntax: pygame.draw.rect(surface, color, (x, y, width, height))
pygame.draw.rect(screen, RED, (50, 50, 200, 100))   # red rectangle at (50,50)

# 2. Circle
# Syntax: pygame.draw.circle(surface, color, (center_x, center_y), radius)
pygame.draw.circle(screen, BLUE, (400, 300), 75)    # blue circle at center

# 3. Line
# Syntax: pygame.draw.line(surface, color, (start_x, start_y), (end_x, end_y), thickness)
pygame.draw.line(screen, GREEN, (100, 500), (700, 500), 5)  # green line across bottom

# 4. Polygon
# Syntax: pygame.draw.polygon(surface, color, [(x1,y1), (x2,y2), (x3,y3), ...])
pygame.draw.polygon(screen, YELLOW, [(600,100), (700,200), (650,300), (550,200)])  # yellow diamond shape


# -------------------------------
# APPROACH 2: USING RECT OBJECTS
# -------------------------------
# Rect is a class that stores position and size.
# Syntax: pygame.Rect(x, y, width, height)
rect_obj = pygame.Rect(100, 100, 150, 80)   # create a rectangle object
pygame.draw.rect(screen, GREEN, rect_obj)   # draw using the object

# You can move or modify rect_obj later:
rect_obj.move_ip(200,25)                    # move rectangle in-place (x+200,y+25)
pygame.draw.rect(screen, GREEN, rect_obj)   # draw moved rectangle

# -------------------------------
# UPDATE DISPLAY
# -------------------------------
pygame.display.update()

# -------------------------------
# KEEP WINDOW OPEN
# -------------------------------
# Wait for 5 seconds so you can see the shapes
pygame.time.wait(5000)

# Quit pygame
pygame.quit()
