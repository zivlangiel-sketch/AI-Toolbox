import os
from dotenv import load_dotenv
from openai import OpenAI

# טעינת המשתנים מהכספת
load_dotenv("../.env")

# יצירת הלקוח - הוא יחפש אוטומטית משתנה בשם OPENAI_API_KEY
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)
# שליחת בקשה למודל
response = client.chat.completions.create(
    model="gpt-4o-mini", # מודל מעולה וזול להתחלה
    messages=[
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": "Write a Playwright login function in Python."}
    ]
)

print(response.choices[0].message.content)