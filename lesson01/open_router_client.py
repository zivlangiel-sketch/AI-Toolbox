from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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", 
)

completion = client.chat.completions.create(
  model="qwen/qwen3-vl-30b-a3b-thinking",
  messages=[
    {
      "role": "user",
      "content": "write a simple login functionality with playwright and python"
    }
  ]
)

print(completion.choices[0].message.content)