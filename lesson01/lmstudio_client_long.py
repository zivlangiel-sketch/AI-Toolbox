import requests

#First we build the url & endpoint
BASE_URL = "http://localhost:1234"
ENDPOINT = BASE_URL + "/v1/chat/completions"

#now to create the request ----- Creating the payload with model and messages
payload = {
    "model": "gemma-3-1b-it",
    "messages": [
        {"role": "user",
        "content": "How R you?"}
    ]
}

response = requests.post(ENDPOINT, json=payload)
data = response.json()
print(data)
content = data["choices"][0]["message"]["content"]
print("~~~~~~~~~~~~~~~~~~~")
print(content)
