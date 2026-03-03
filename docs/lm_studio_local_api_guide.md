# LM Studio Local API – From Scratch Guide

## 🎯 Goal
Build a Python script that:
1. Sends a prompt to a local LM Studio server
2. Prints the model response

---

# 1️⃣ Start LM Studio

1. Open LM Studio
2. Load a model
3. Click **Start Server**
4. Default server address:

http://localhost:1234

Test:
http://localhost:1234/v1/models

If JSON appears → server is running.

---

# 2️⃣ Create Python File

Create a file:

lmstudio_client.py

---

# 3️⃣ Import Required Libraries

We need:

- requests → send HTTP requests
- json → handle JSON responses

---

# 4️⃣ Define Server URL

We define:

BASE_URL = "http://localhost:1234"

Chat endpoint path:

/v1/chat/completions

Combine them:

ENDPOINT = BASE_URL + "/v1/chat/completions"

---

# 5️⃣ Build the Payload

LM Studio expects this structure:

{
  "model": "MODEL_NAME",
  "messages": [
    {
      "role": "user",
      "content": "Your question here"
    }
  ]
}

---

## Step-by-step payload construction logic

1. Create empty dictionary:
payload = {}

2. Add model:
payload["model"] = "your_model_name"

3. Create empty messages list:
payload["messages"] = []

4. Create message dictionary:
message = {}
message["role"] = "user"
message["content"] = "Your question here"

5. Add message to list:
payload["messages"].append(message)

---

# 6️⃣ Send POST Request

response = requests.post(ENDPOINT, json=payload)

Important:
json=payload automatically converts Python dict to JSON.

---

# 7️⃣ Convert Response to JSON

data = response.json()

⚠ Always use parentheses:
response.json()  ✔
response.json    ✖

---

# 8️⃣ Extract Model Response

Response structure:

data
 └── "choices" (list)
      └── [0]
           └── "message"
                └── "content"

Extract content:

content = data["choices"][0]["message"]["content"]
print(content)

---

# 🧠 Core Python Concepts Used

Dictionary:
{}
dict["key"]

List:
[]
list.append(item)
list[0]

Function call:
function()

NOT:
function[]

---

# 🔍 Debugging Tips

Check status:
print(response.status_code)

200 = success

Print full response:
print(data)

---

# 🏗 Full Logical Flow

1. Start LM Studio server
2. Build URL
3. Build payload
4. Send POST
5. Convert response to JSON
6. Extract content
7. Print result

---

# 🚀 What You Now Know

- How REST APIs work
- How POST requests work
- How JSON is structured
- How to access nested data
- How local LLM APIs operate
- How to debug API calls

END