# AI MASTER CHEAT SHEET
Local LLM Setup | LM Studio | Ollama | Python | QA

==================================================
SECTION 1 – LM STUDIO
==================================================

What is it?
Local GUI app that runs LLMs with an OpenAI-compatible API.

Server URL:
http://localhost:1234

--------------------------------------------------
Start Server
--------------------------------------------------

1. Open LM Studio
2. Go to "Local Server"
3. Click "Start Server"
4. Verify:
   Server running at http://localhost:1234

--------------------------------------------------
Load Model
--------------------------------------------------

1. Go to "Models"
2. Select model
3. Click "Load"
4. Verify it is Active

--------------------------------------------------
Check Server (Browser)
--------------------------------------------------

http://localhost:1234/v1/models

If JSON appears → server works.

--------------------------------------------------
Install Python Client
--------------------------------------------------

pip install lmstudio

--------------------------------------------------
Basic Python Script
--------------------------------------------------

from lmstudio import Client

client = Client(base_url="http://localhost:1234")

response = client.chat.completions.create(
    model="MODEL_NAME",
    messages=[
        {"role": "user", "content": "Hello! Write one short sentence."}
    ],
)

print(response.choices[0].message.content)

--------------------------------------------------
Run Script
--------------------------------------------------

python scripts\lmstudio_client.py

--------------------------------------------------
Common Errors
--------------------------------------------------

Connection refused
→ Server not running

Model not found
→ Wrong model name (check /v1/models)

==================================================
SECTION 2 – OLLAMA
==================================================

What is it?
Local LLM engine with its own API.

Server URL:
http://localhost:11434

--------------------------------------------------
Check Installation
--------------------------------------------------

ollama --version

--------------------------------------------------
Download & Run Model
--------------------------------------------------

ollama run llama3

--------------------------------------------------
List Installed Models
--------------------------------------------------

ollama list

--------------------------------------------------
Check Server
--------------------------------------------------

curl http://localhost:11434/api/tags

--------------------------------------------------
Basic Python (Ollama)
--------------------------------------------------

import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3",
    "prompt": "Say hello in one sentence.",
    "stream": False
}

response = requests.post(url, json=payload)

print(response.json()["response"])

==================================================
SECTION 3 – PROJECT STRUCTURE
==================================================

AI-Toolbox/
│
├── docs/
├── scripts/
├── tests/
├── data/
├── README.md
└── venv/

==================================================
SECTION 4 – WINDOWS COMMANDS
==================================================

Create virtual environment:
python -m venv venv

Activate venv:
.\venv\Scripts\Activate.ps1

Deactivate:
deactivate

Install package:
pip install package_name

Upgrade pip:
python -m pip install --upgrade pip

==================================================
SECTION 5 – AI QA BASICS
==================================================

Basic Validation Ideas:

□ Response is not empty  
□ Response length > 10 characters  
□ Contains expected keyword  
□ No hallucinated data  
□ Matches known context  

--------------------------------------------------
Simple Assertion Example
--------------------------------------------------

assert response != ""
assert "error" not in response.lower()

==================================================
SECTION 6 – RAG TESTING BASICS
==================================================

Check:
□ Retrieval accuracy
□ Groundedness
□ Hallucinations
□ Cross-document consistency

Example QA Question:
"Answer ONLY using provided context."

==================================================
SECTION 7 – DEBUG CHECKLIST
==================================================

□ Is the server running?
□ Is the model loaded?
□ Is the port correct?
□ Is the model name correct?
□ Are you inside venv?
□ Is the URL correct?

==================================================
SECTION 8 – LM STUDIO vs OLLAMA
==================================================

LM Studio:
- Port 1234
- OpenAI compatible
- GUI
- Good for workshops

Ollama:
- Port 11434
- CLI
- Lightweight
- Good for backend environments

==================================================
END OF CHEAT SHEET
==================================================