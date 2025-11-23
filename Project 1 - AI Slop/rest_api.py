# -------------------------------
# Simple Python script to connect to Ollama REST API
# and generate text using the TinyLlama model
# -------------------------------

import requests  # Import the requests library to make HTTP requests

# Define the API endpoint (URL) for Ollama
# 'localhost' means the server is running on your own machine (or Raspberry Pi)
# Port 11434 is the default Ollama port, and '/api/generate' is the endpoint for text generation
url = "http://localhost:11434/api/generate"

# Define headers for the request
# "Content-Type: application/json" tells the server that we are sending JSON data
headers = {
    "Content-Type": "application/json"
}

# Define the JSON payload (data we send to Ollama)
# - model: which language model to use (tinyllama)
# - prompt: the text we want the model to respond to
# - stream: False means we want the full response at once (not streamed line by line)
payload = {
    "model": "tinyllama",
    "prompt": "Hi, What is the capital of the United States of America?",
    "stream": False
}

# Send a POST request to Ollama with the URL, headers, and JSON payload
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful (status code 200 means OK)
if response.status_code == 200:
    # Convert the response to JSON format (dictionary in Python)
    response_in_json = response.json()

    # Extract the generated text from the "response" field
    poem = response_in_json["response"]

    # Print the generated text to the terminal
    print(poem)
else:
    # If there was an error, print the error message
    print("Error:", response.text)
