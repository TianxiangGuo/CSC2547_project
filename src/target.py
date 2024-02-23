import json
import os
import utilities


def respond(input_prompt):
    messages = [
        {"role": "user", "content": input_prompt}
    ]
    response = utilities.call_openai_api(messages, model="gpt-4-1106-preview")

    return response