import http.client
import json
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') 
OPENAI_API_ENDPOINT = os.getenv('OPENAI_API_ENDPOINT') 


def call_openai_api(messages, top_p=0.5, temperature=0.7, model="gpt-3.5-turbo-1106"):
    response = client.chat.completions.create(
        model=model,
        #model="gpt-4-1106-preview",
        messages=messages,
        top_p=top_p,
        temperature=temperature
    )
    return response.choices[0].message.content
    # return response