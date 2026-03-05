import os
from groq import Groq

client = Groq(
    api_key="gsk_YOUR_API_KEY_HERE",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "write a simple login functionality with playwright and python",
        }
    ],
    model="openai/gpt-oss-20b",
)

print(chat_completion.choices[0].message.content)
