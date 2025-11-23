# 📝 Project 2: Animation using PyGame

This folder contains a series of PyGame animation exercises and a final sample project that ombines them. These animations are designed to teach step‑by‑step concepts of motion, collision, and transitions in PyGame.

---

## 📂 Files Overview

### 1. [animation_01.py](animation_01.py) – Rectangles Moving to Center
- **Description:** Four rectangles start from each corner of the screen and move diagonally toward the center.  
- **Concepts Learned:**  
  - Rectangles (pygame.Rect)  
  - Movement toward a target point  
  - Frame‑based animation  

### 2. [animation_02.py](animation_02.py) – Growing Circle Burst
- **Description:** A circle begins at the center with radius 0. It grows steadily until it touches the screen boundary, then bursts into multiple smaller bubbles.  
- **Concepts Learned:**  
  - Circle drawing (pygame.draw.circle)  
  - Growth logic based on radius  
  - Collision detection with screen edges  
  - Transition into new objects (bubbles)  

### 3. [animation_03.py](animation_03.py) – Bouncing Bubbles
- **Description:** Many small bubbles bounce around within the screen boundaries. Each bubble has random size, color, and speed.  
- **Concepts Learned:**  
  - Object‑oriented design with a Bubble class  
  - Randomized properties for variation  
  - Bounce logic when hitting screen edges  
  - Continuous motion and collision response  

### 4. [project2_sample.py](project2_sample.py) – Full Project Sample
- **Description:** A complete 20‑second animation combining all three phases:  
  1. Rectangles Phase (≈5s): Four rectangles move from corners and converge at the center.  
  2. Circle Phase (≈3s): Rectangles vanish, and a circle grows from the center until it hits the boundary.  
  3. Burst Phase: The circle bursts into multiple bubbles.  
  4. Bubbles Phase (remaining time): Bubbles bounce around the screen until the animation ends.  
- **Concepts Learned:**  
  - Sequencing multiple animations in one timeline  
  - Transitioning between phases smoothly  
  - Combining rectangle, circle, and bubble logic into a unified project  

---

## Hints & Suggestions  

### 1. Follow the Provided Template
- Always start from the **template posted on Canvas**.  
- **Do not change screen dimensions** — keep them at `1920 × 1080` for final submission.  
- Enter your **name** and the **theme of your animation** correctly in the designated variables.  
- Replace the **frame sequence number** with the one assigned to you in the spreadsheet.  
- Place your **20‑second animation code** inside the section marked with the comment: *“Your animation goes here”*.  
- **Lock your frame rate** at 60 FPS using `clock.tick(60)` for smooth motion, i.e. don't change it.

### 2. Break Down the 20 Seconds
- Think of your animation as a **timeline**.  
- Divide the 20 seconds into smaller segments (e.g., 5s rectangles, 3s circle, 12s bubbles).  
- Write separate logic for each segment, then combine them in the main loop.  
- This makes debugging easier and ensures each part has a clear start and end.

### 3. Ensure Smooth Transitions
- Avoid abrupt jumps between phases.  
Example: fade out shapes, or let them shrink/disappear smoothly.  
- Test your animation multiple times to check that each phase flows into the next.

### 4. Explore Beyond Shapes
- You’ve seen **rectangles, circles, and fonts** — but PyGame also supports:  
  - **Sprites:** animated pixel characters or images.  
  - **Sounds:** add audio effects or background music (`pygame.mixer`).  
- These can make your animation more engaging and unique.

### 5. Extra Tips
  
- **Use classes** (like `Bubble`, `Circle`) to keep code organized and reusable.  
- **Experiment with randomness** (colors, speeds, positions) to add variety.  
- **Plan your storyboard first** — sketch out what happens in each segment before coding.  
- **Test at smaller resolutions** (e.g., 640×360) while developing to save time, then switch back to 1920×1080 for final render.  
- **Keep backups** of working versions — don’t overwrite your progress without saving a copy.  

---

## Checklist
Use this checklist to make sure your Project‑2 animation is complete and ready to submit.

#### ✅ Technical Requirements
- [ ] Screen resolution set to **1920 × 1080** (FHD).  
- [ ] Frame rate locked at **60 FPS** using `clock.tick(60)`.  
- [ ] Your **name** and **animation theme** entered correctly in the template variables.  
- [ ] **Start sequence number** replaced with the TA‑assigned value (not the default 1000000).  
- [ ] Animation code placed inside the section marked *“Your animation goes here”* in the template.  
- [ ] Code runs end‑to‑end for the full duration (3+20 seconds).  

#### 🎨 Creative & Animation Flow
- [ ] 20 seconds broken into smaller segments
- [ ] Smooth transitions between phases (no abrupt jumps).  
- [ ] Consistent or thematic color palette chosen.  
- [ ] Optional extras considered (sprites, sounds, fonts).  
- [ ] Animation feels cohesive from start to finish.  

#### 📄 Documentation & Submission
- [ ] Code tested at least once at full resolution before submission.  
- [ ] Backup copy saved before submission.  
- [ ] Create zip of all the correctly numbered frames generated by running your final animation script and email to professor (you may keep the TA in CC).
- [ ] Assignment Submission in Canvas:
    * Python code in Text Area.
    * Upload a single representative frame (one png file from animatied frames).

#### 🏁 Final Step
- [ ] Confirm everything runs without errors.  
- [ ] Recheck your project submission following Canvas instructions.  

---

**✨ Remember: this project is not just about code, but about creativity and storytelling.**  
**Good luck -- you’ve got this, and we’re excited to see your animations shine!**
