# UCSD-FA25-VIS142
[UCSD-FA25] VIS-142 - Practices in Computing Arts (Role: Teaching Assistant)  

This repository contains code, documentation, and projects from the VIS-142 course.  
It is divided into four main sections to guide students from **Python basics** to **hands-on AI and animation projects**.

---

## 📌 Sections Overview

### 1. Python
- **Goal:** Learn Python fundamentals
- **Contents:**
  - Variables, data types, and operators
  - Control flow (if/else, loops)
  - Functions and modules
  - File handling
- **Folder:** `python/`

### 2. Raspberry Pi & Linux
- **Goal:** Understand how to use Raspberry Pi with Linux
- **Contents:**
  - Introduction to Raspberry Pi and getting started
  - Basic Linux commands
  - Setting up Python on Raspberry Pi
- **Folder:** `Raspberrypi & Linux/`

### 3. Project-1: AI Slop using Python and Ollama
- **Goal:** Build an AI-powered application by connecting Python to Ollama
- **Contents:**
  - How to install and run Ollama locally
  - Python scripts to connect with Ollama API
  - Example prompts and responses
  - Project Sample
- **Folder:** `Project 1: AI Slop/`

### 4. Project-2: Animation using PyGame
- **Goal:** Learn game development basics with PyGame
- **Contents:**
  - Introduction to PyGame
  - Creating windows, drawing shapes
  - Intro to Animations using PyGame
  - Project Sample
- **Folder:** `Project 2: Animation with PyGame/`

---

## Folder Structure:
- 🐍 **Code examples** (`.py` files)  
  Small Python scripts with inline comments to demonstrate concepts.

- 📖 **Concepts / Explanations** (`.md` files)  
  Markdown notes that explain the theory, usage, and references.

---

## ⚙️ Setup Instructions

### 🍓 Raspberry Pi

1. **Hardware Setup**  
   Get your Raspberry Pi board, power supply, microSD card, monitor, keyboard, and mouse ready.  
   (Think of the Pi as the CPU, while the monitor/keyboard/mouse are the peripherals.)

2. **Install Raspberry Pi OS**  
   On another computer, install the **Raspberry Pi Imager** tool.  
   Insert the microSD card into that computer and use the Imager to flash the latest Raspberry Pi OS image onto the card.

3. **Insert the microSD Card**  
   Once the OS image is written, remove the card from your computer and insert it back into the Raspberry Pi.

4. **Power Up & Connect Peripherals**  
   Plug in the power supply to the Pi, and connect it to the monitor, keyboard, and mouse.

5. **Initial OS Setup**  
   Follow the on‑screen instructions to complete the Raspberry Pi OS setup.  
   When finished, you’ll land on the desktop screen — and your Pi is ready to use!
🎉 **Volla!! You have just assembled and set up a computer by yourself.   
Cheers!!**

### 🐍 Python
- As we will be working on Raspberry PI, Python comes in-built with it.
To verify your Python version:  `python --version`
We will be using **Thonny** IDE, which also comes pre-installed.
To open Thonny: `Home -> Programming -> Thonny`
- If you want to work on your personal computer, install **Python 3.9+** from the official site: [https://www.python.org/downloads/](https://www.python.org/downloads/).
After installation, verify it with: `python --version`
You may also install **Thonny** IDE (https://thonny.org) for a beginner-friendly environment. On most systems, you can open Thonny directly after installation.
Any other IDE (or plain in-built text editor) will be fine as well.

### 🤖 Ollama & Tinyllama
- Ollama is required for the AI project section.  
- Follow the official guide for linux: [Ollama Installation](https://ollama.ai/download)  
- Once installed, verify it runs locally from terminal: `ollama list`
- Download Tinyllama & run: `ollama run tinyllama`  
This will download tinyllama before running for the first time. Alternatively, you can use `ollama pull tinyllama` to download first and then run using `ollama run tinyllama`.
Once tinyllama is running in your terminal, you can use it as a chatbot.
To exit, use: `\bye`

---

## 📚 References
- [Python Official Docs](https://docs.python.org/3/)
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
- [Linux Command Cheat Sheet](https://linuxcommand.org/)
- [Ollama Documentation](https://ollama.ai/docs)
- [PyGame Documentation](https://www.pygame.org/docs/)

---

Happy learning 🚀
