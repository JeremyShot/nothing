from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os


# os.environ['http_proxy'] = 'http://rr61h70dw22b7q87ra@zxcvbn.icu:SiJ1mhi42@api.openai.com:443'
# os.environ['https_proxy'] = 'http://rr61h70dw22b7q87ra@zxcvbn.icu:SiJ1mhi42@api.openai.com:443'


app = FastAPI()

class Message(BaseModel):
    content: str 


# Initialize your ChatGPT settings
openai.api_key = "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"

def generate_chat_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content


@app.post("/mychat")
def chat_with_gpt(message: Message):
    user_message = message.content

    generated_response = generate_chat_response(user_message)

    return {"response": generated_response}