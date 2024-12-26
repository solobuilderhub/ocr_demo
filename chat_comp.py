import base64
import json
from openai import OpenAI
import os
from prompt_file import prompt, prompt_cheque_account, prompt_for_text, text
client = OpenAI(api_key="")

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "statement/td/page_1.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)



response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={
        "type": "json_object"
    },
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt_cheque_account
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                        "detail": "high"
                    },
                }
            ],
        }
    ],
)

messages=[
        {
            "role": "system", 
            "content": prompt_cheque_account
        },
        {
            "role": "user", 
            "content": text
        }
    ],


# Print the response for debugging
# print(response)

# Assuming the response contains the transactions in the 'content' field
transactions_str = response.choices[0].message.content
print(transactions_str)
# # Print the transactions string for debugging
# print("Transactions String:", transactions_str)

# print(type(transactions_str))

# Convert the string to JSON
try:
    transactions = json.loads(transactions_str)
    # Save the transactions to a JSON file
    with open("transactions.json", "w") as json_file:
        json.dump(transactions, json_file, indent=4)
except json.JSONDecodeError as e:
    print("Failed to decode JSON:", e)