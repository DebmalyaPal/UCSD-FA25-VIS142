# 📝 Project 1 – AI Slop with TinyLlama on Raspberry Pi

## Problem Statement
Create a Python program that generates creative text - our playful theme is **“AI Slop”**.  
The program should use **prompts** to produce varied AI Slops as outputs such as poems or phrases.  
By connecting to the **TinyLlama language model** running locally on Raspberry Pi through Ollama’s REST API, the program must demonstrate:
- **Generative behavior** → each run produces different text.    
- **Integration skills** → combining Python programming, randomization, and REST API communication with a language model.  

This project is designed to help you practice **string & list processing, using functions, prompt engineering, and API integration** while exploring the creative side of AI.

---

## 🔹 What is Ollama?
- **Ollama** is a tool that lets you run large language models (LLMs) locally on your computer or Raspberry Pi.  
- It provides a simple way to **install, manage, and run models** without needing cloud services.  
- Ollama exposes a **REST API** so you can connect to it from Python programs.

---

## 🔹 Ollama Installation Steps (Linux / Raspberry Pi)

Open your terminal and run:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

- This downloads and installs Ollama.  
- After installation, you can check available models with: `ollama list`

---

## 🔹 What is TinyLlama?
- **TinyLlama** is a small language model (LLM) designed to run efficiently on devices like Raspberry Pi.  
- It is trained to generate text (poems, phrases, stories, etc.) but uses fewer resources compared to large models.  
- In this project, we use TinyLlama because:
  - It runs smoothly on Raspberry Pi hardware.
  - It can generate creative text outputs for our “AI Slop” theme.
  - It supports **generative behavior** (different outputs each run).

---

## 🔹 REST APIs and URLs

- **URL (Uniform Resource Locator):** The address used to access resources on the web or local server.  
  Example: `http://localhost:11434/api/generate`  
  - `localhost` → means your own computer (or Pi).  
  - `11434` → default port Ollama uses.  
  - `/api/generate` → endpoint for generating text.

- **REST API (Representational State Transfer):**  
  A way for programs to communicate over HTTP using URLs.  
  - You send a **request** (like “generate text”).  
  - You get a **response** (the generated text).

- **Python `requests` library:**  
  - A simple library to send HTTP requests from Python.  
  - Example: `requests.post(url, data)` sends data to a server and gets back a response.

---

## Program 1 – [Simple REST API Connection Script](rest_api.py)

This program is designed to show how Python can connect to a REST API.  
We use Ollama’s API to send a prompt to the TinyLlama model and receive generated text back.

### Motivation
- REST APIs are the standard way for programs to communicate over the web.  
- Learning how to connect to an API in Python builds skills that apply to many real-world tasks:
  - Fetching data from web services (weather, stock prices, social media).  
  - Sending data to servers (forms, uploads, IoT devices).  
  - Integrating AI models into your own applications.  
- In this project, the REST API connection is the bridge between **your Python program** and **TinyLlama running on Raspberry Pi**.

### Algorithm / Steps
1. **Define the API endpoint (URL)**  
   - Example: `http://localhost:11434/api/generate`  
   - `localhost` = your own machine (Raspberry Pi).  
   - `11434` = default Ollama port.  
   - `/api/generate` = endpoint for text generation.

2. **Set up request headers**  
   - Tell the server you are sending JSON data (`Content-Type: application/json`).

3. **Prepare the payload (data)**  
   - Include:
     - `model`: which model to use (`tinyllama`).  
     - `prompt`: the text you want the model to respond to.  
     - `stream`: whether to receive the response all at once or line by line.

4. **Send the request**  
   - Use Python’s `requests.post()` to send the payload to the API.

5. **Check the response**  
   - If status code = 200 → success.  
   - Otherwise → print the error message.

6. **Parse the JSON response**  
   - Extract the generated text from the `"response"` field.

7. **Display the result**  
   - Print the generated text to the terminal.

### Key Concepts Learned
- **URL** → the address of the API endpoint.  
- **REST API** → a way for programs to communicate using HTTP requests and responses.  
- **Requests library** → Python’s tool for sending HTTP requests easily.  
- **JSON** → the format used to send and receive data between client and server.  

---

## Program 2 – [Generative Poem Creator](ai_slop_sample.py)

This second program builds on Program 1 and introduces **randomization** to make the output generative.  
Instead of sending a fixed prompt, the program constructs a new prompt each run by randomly choosing a **theme**, **style**, and **rhyme scheme**. This ensures that every execution produces different text — meeting the expectation of Project 1 for creative “AI Slop.”

### Motivation
- Program 1 showed how to connect Python to Ollama’s REST API, Program 2 demonstrates how to **generate varied outputs** by combining programming logic (random choices) with AI text generation.  
- This helps us grasp:
  - How to build prompts dynamically.  
  - How to use randomness to make programs creative.  
  - How to orchestrate multiple functions together in a Python script.  

### Algorithm / Steps
1. **Define lists of options**  
   - Themes (e.g., Nature, Technology, Sports, Love, etc.)
   - Styles (e.g., stanzas of 4, 6, or 8 lines).  
   - Rhyme schemes (alternate rhyme, couplets, monorhyme, tercets).

2. **Randomly select one option from each list**  
   - Use Python’s `random.choice()` to pick a theme, style, and rhyme scheme.

3. **Construct the AI prompt**  
   - Combine the chosen theme, style, and rhyme into a detailed instruction string.  
   - Example: “Write a poem on *Nature*, approximately 50 lines, each stanza has *6 lines*, with *couplet rhyme*.”

4. **Send the prompt to Ollama REST API**  
   - Use `requests.post()` with the TinyLlama model and the constructed prompt.

5. **Check the response**  
   - If status code = 200 → parse JSON and extract the `"response"` field (the poem text).  
   - Otherwise → print the error message.

6. **Display the poem**  
   - Print the generated text.

7. **Main orchestration**  
   - Call the functions in order: randomize → build prompt → send to AI → display result.  
   - Each run produces a random prompt (high chance of a different prompt) and a different poem.

### Key Concepts Learned
- **Randomization** → using `random.choice()` to vary program behavior.  
- **Prompt engineering** → constructing detailed instructions for the AI model.  
- **REST API integration** → same as Program 1, but now with dynamic input.  
- **Generative output** → the program produces different prompts and results in each run.  

---

## Suggestions for Project Work

Once you have Program 1 and Program 2 working, it’s time to **push your creativity further**.  
Remember, the theme is *AI Slop* — it doesn’t need to make perfect sense. The goal is to explore text generation, randomness, and playful experimentation.  
Also, try to write your AI Slop to a file through program itself.

### Ideas to Try
1. **Add more random fields to your prompt**  
   - Beyond theme, style, and rhyme, consider randomizing:  
     - Tone (serious, humorous, sarcastic, dreamy).  
     - Perspective (first person, third person, narrator voice).  
     - Length (short verse, epic poem).  

2. **Include Varied Tone or Persona in the Prompt**  
Make your AI Slop more creative by shaping the **voice or character** of the language model in your prompt.  
You’re not only telling the AI *what* to write, but also *who* it should sound like while writing.
Examples:
   - “Write in a **dramatic tone**, full of intensity and emotion.”  
   - “Write in a **playful, silly tone**, with humor and exaggeration.”  
   - “Write as an **aged poet**, reflecting on wisdom and fading memories.”  
   - “Write as a **youthful poet**, full of energy and optimism.”  
   - “Write as a **poet oppressed by tyranny**, expressing frustration and longing for freedom.”  
   
   Changing the persona or tone can make the same theme feel completely different. Experimenting with this is a powerful way to produce surprising, varied outputs.

3. **Combine multiple AI responses**  
   - Generate 3-4 different outputs by sending 3-4 random prompts to TinyLlama.  
   - Break down your final poem or text by stitching these responses together.  
   - This creates a collage of AI Slop - chaotic, unexpected, and fun.

4. **Word substitutions**  
   - After generating a poem, replace certain words with your own choices. This adds another layer of randomness and humor
   Example: swap every occurrence of “love” with “pizza,” or “nature” with “Wi‑Fi.”  

5. **Play with constraints**  
   - Ask the AI to write in the style of a news article, a recipe, or a diary entry.  
   - Mix genres: “Write a fantasy poem that reads like a weather report.”
   - Have themes as well as sub-themes (maybe contrasting due to randomness).

---

### Conclusion
Be playful, be bold, and don’t worry about making sense — that’s the spirit of *AI Slop*!  
The more you experiment with prompts, randomness, and creative twists, the more unique your project will be. Think of this as a sandbox: try things out, break patterns, and surprise yourself with what TinyLlama can generate. 

