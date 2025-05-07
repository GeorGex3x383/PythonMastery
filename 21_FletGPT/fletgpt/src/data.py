import os
from dotenv import load_dotenv

load_dotenv()
API_KEY_ENV = os.environ.get("CHAT_API_KEY")

PAGE_BG_COLOR = "#ffffff"
DEFAULT_PROMPTS = [
                    ("Discuss pros and cons", "\nof renewable energy sources."),
                    ("Describe the structure", "\nof a typical animal cell."),
                    ("Compare and contrast", "\nmitosis and meiosis."),
                    ("Explain the importance", "\nof the Hubble Space Telescope.")
                ]
CHATGPT_IMAGE_URL = "https://pngimg.com/d/chatgpt_PNG1.png"
MY_IMAGE_PATH = "fletgpt/src/assets/pixel.png"

# Cohere
import requests
import json

# For more info, read the Cohere AI API documentation:
# https://docs.cohere.com/v2/reference/chat

def cohere_response(content):
    API_URL = "https://api.cohere.com/v2/chat"
    API_KEY = API_KEY_ENV  # Replace with your own API key and store it in a .env file

    DATA = {
        "stream": False,
        "model": "command-r",
        "messages": [
            {
                "role": "user",
                "content": content  # Change this message to customize the chatbot's response
            }
        ]
    }

    HEADERS = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    request = requests.post(API_URL, data=json.dumps(DATA), headers=HEADERS)
    response = request.json()
    texto = response['message']['content'][0]['text']
    return texto

# Prueba
# print(cohere_response("In 20 words, who is elon musk?"))