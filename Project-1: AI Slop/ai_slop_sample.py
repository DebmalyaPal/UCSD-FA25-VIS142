# -------------------------------
# Program – Generative Poem Creator using TinyLlama
# -------------------------------
# This program connects to Ollama's REST API (TinyLlama model)
# and generates different poems each time it runs.
# It randomizes the theme, style, and rhyme scheme to make the output generative.

import requests   # For sending HTTP requests to Ollama REST API
import json       # For working with JSON responses
import random     # For randomizing themes, styles, and rhymes

# -------------------------------
# Functions to randomize poem attributes
# -------------------------------

def get_theme_of_poem():
    # List of possible themes for the poem
    themes = [
        "Nature", "Love", "Technology", "Identity", "Dreams and Aspirations",
        "Time", "Loneliness", "Mystery and Fantasy", "Death",
        "Human Struggles and Triumphs", "Growth and Change", "Memory", "Hope",
        "Friendship", "Adventure", "Peace and Harmony", "Fear", "Transformation",
        "Strength", "Hope and Despair", "The Unknown", "Resilience", "Wisdom",
        "Regret", "Freedom", "Justice and Equality", "Nature's Fury",
        "Youth and Innocence", "Rebirth", "War and Peace"
    ]
    # Randomly select one theme
    return random.choice(themes)

def get_style_of_poem():
    # Possible stanza styles
    styles = [
        "each stanza have 4 lines",
        "each stanza have 6 lines",
        "each stanza have 8 lines"
    ]
    # Randomly select one style
    return random.choice(styles)

def get_rhyme_of_poem():
    # Possible rhyme schemes
    rhymes = [
        "Every other line of the poem ends with similar sounding words (alternate rhyme)",
        "Every two consecutive lines of the poem end with similar sounding words (couplet rhyme)",
        "Each line within the stanza ends with similar sounding words (monorhyme)",
        "The rhyme repeats every three lines of the poem, with each third line ending in similar sounding words (tercets)",
    ]
    # Randomly select one rhyme scheme
    return random.choice(rhymes)

# -------------------------------
# Function to build the AI prompt
# -------------------------------

def get_prompt_for_ai(theme, style, rhyme):
    # Construct a detailed prompt for TinyLlama
    prompt = "Hello AI! My friend, you are a creative author and a poet. \n"
    prompt += "Please help me write a poem on " + theme + ". "
    prompt += "Please make the poem a little long - let's say approximately 50 lines, "
    prompt += "and make " + style + ". " + rhyme + ".\n"
    
    # (Optional instructions commented out: asking AI to return a Python list of lines)
    # prompt += "Please return the lines of the poem in form of a Python list. "
    # prompt += "Make sure you don't write a program in python - just respond with a list containing sentences of the poem. "
    # prompt += "To recap, the following is a python list -> ['Line 1', 'Line 2', 'Line 3']"
    
    return prompt

# -------------------------------
# Function to send prompt to Ollama API and get poem
# -------------------------------

def generate_poem_using_ai(prompt_to_ai):
    # Ollama REST API endpoint
    url = 'http://localhost:11434/api/generate'
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "tinyllama",   # Use TinyLlama model
        "prompt": prompt_to_ai, # Prompt we constructed
        "stream": False         # Get full response at once
    }

    # Send POST request to Ollama
    response = requests.post(url, json=payload, headers=headers)

    # If request successful
    if response.status_code == 200:
        response_in_json = response.json()           # Convert response to JSON
        lines_of_poem = response_in_json["response"] # Extract generated text
        display_poem(lines_of_poem)                  # Display nicely
    else:
        print("Error: ", response.text)

# -------------------------------
# Function to display the poem
# -------------------------------

def display_poem(lines_of_poem):
    # Add a header before printing the poem
    poem = "POEM by Fname's AI for PROJECT-1 of VIS-142 (section-no.): \n\n" + lines_of_poem
    print(poem)

# -------------------------------
# Main function – orchestrates the program
# -------------------------------

def main():
    # Randomize theme, style, and rhyme
    theme = get_theme_of_poem()
    style = get_style_of_poem()
    rhyme = get_rhyme_of_poem()
    
    # Build the AI prompt
    my_prompt = get_prompt_for_ai(theme, style, rhyme)
    
    # Print the prompt (for debugging / understanding)
    print(my_prompt)
    print("\n\n\n\n")
    
    # Generate and display the poem
    generate_poem_using_ai(my_prompt)

# -------------------------------
# Entry point of the program
# -------------------------------
if __name__=='__main__':
    main()
