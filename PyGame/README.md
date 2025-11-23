# PyGame Basics for Animation Project

This path introduces the fundamentals of PyGame needed for your animation project.  
We focus on **screen setup, captions, colors, and drawing shapes** — not events or input handling.  

---

## ⚙️ Setup Instructions

- PyGame will be pre-installed in Raspberry Pi and we can directly start using it.
- If using outside Raspberry Pi, we can simply install PyGame using `pip install pygame` in the terminal.

---

## 📂 Contents

This path introduces the fundamentals of PyGame needed for your animation project.  
We focus on **screen setup, captions, colors, and drawing shapes** — not events or input handling.

### [01_screen_basics.py](02_drawing_shapes.py)
- Initialize PyGame
- Create a window with custom screen size
- Set window caption (headline/title bar text)
- Define and use RGB colors
- Fill background with chosen color

![Animation from PyGame file 1](<screenshots/pygame_animation_1.png>)

### [02_drawing_shapes.py](02_drawing_shapes.py)
- Draw rectangles, circles, lines, and polygons
- Position shapes using coordinates
- Practice layering shapes

![Animation from PyGame file 2](<screenshots/pygame_animation_2.png>)

### [03_text_rendering.py](03_text_rendering.py)
- Render text with fonts (default system font or custom TTF)
- Control size, color, and antialiasing
- Position text using `get_rect()` (center, topleft, etc.)
- Blit text surfaces to the screen and update the display
- Use multiple lines with varied styles for titles and labels

![Animation from PyGame file 3](<screenshots/pygame_animation_3.png>)

### [04_basic_animation.py](04_basic_animation.py)
- Move a shape across the screen
- Update display with `pygame.display.update()`
- Use `pygame.time.Clock()` for frame control

---

## Why This Path?
These lessons give you the building blocks for your animation project:
- **Screen setup** → control the canvas size.  
- **Captions and text** → add titles or labels.  
- **Colors and shapes** → create visuals.  
- **Basic animation** → bring objects to life.  

By combining these, you can design creative animations without worrying about events or user input.
