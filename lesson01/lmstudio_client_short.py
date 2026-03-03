import lmstudio as lms

model = lms.llm("gemma-3-1b-it")
result = model.respond("What is the Capital of Thailand?")

print(result)
