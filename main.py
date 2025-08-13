import os
import json
import math
import re
import requests

# File to save bot memory
MEMORY_FILE = "bot_memory.json"

# Load saved memory
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"bot_name": None, "mode": None}

# Save memory
def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f)

memory = load_memory()

# Greet user and ask for name/mode if not saved
if not memory["bot_name"]:
    print("👋 Hi! I am your personal assistant by David Adeola.")
    memory["bot_name"] = input("What would you like to name me? ").strip() or "SuperBot"

if "who made you,who created you" in
user_input.lower():
    bot_response = "I was created by David Adeola, a 13 year old developer who built me from scratch!"

if not memory["mode"]:
    print("\nModes available: friendly, funny, serious")
    memory["mode"] = input("Choose a mode: ").strip().lower() or "friendly"

save_memory(memory)

BOT_NAME = memory["bot_name"]
MODE = memory["mode"]

# Load OpenRouter API key from .env file
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("❌ ERROR: Missing OpenRouter API key in .env file.")
    exit()

# Function: Solve math offline
def solve_math(expression):
    try:
        # Only allow safe characters
        if re.match(r"^[0-9\+\-\*/\.\s]+$", expression):
            result = eval(expression, {"__builtins__": None}, math.__dict__)
            return f"🧮 Result: {result}"
    except:
        return None
    return None

# Function: Get online response from OpenRouter
def online_chat(prompt):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": f"You are a {MODE} assistant named {BOT_NAME}."},
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠ Online request failed: {e}"

# Main loop
print(f"\n✅ {BOT_NAME} ({MODE} mode) is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print(f"👋 Goodbye from {BOT_NAME}!")
        break

    # First try math offline
    math_result = solve_math(user_input)
    if math_result:
        print(math_result)
        continue

    # Else, get online response
    reply = online_chat(user_input)
    print(f"{BOT_NAME}: {reply}\n")
