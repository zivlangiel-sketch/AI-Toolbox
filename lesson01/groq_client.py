import os
from dotenv import load_dotenv
from groq import Groq

# טעינת המשתנים מקובץ ה-.env לתוך המערכת
load_dotenv()

# שליפת המפתח מתוך ה"כספת"
api_key = os.getenv("GROQ_API_KEY")

# יצירת הלקוח של Groq עם המפתח ששלפנו
client = Groq(api_key=api_key)

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
