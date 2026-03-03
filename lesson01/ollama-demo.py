import ollama

# שליחת השאלה למודל ושמירת התשובה במשתנה
response = ollama.chat(model='gemma3:1b', messages=[
  {
    'role': 'user',
    'content': 'HI there'
  }
])

# הדפסת התשובה למסך
print(response['message']['content'])