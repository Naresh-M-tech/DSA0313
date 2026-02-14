import openai

openai.api_key = "sk-1234567890abcdef1234567890abcdef12345678"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Explain Natural Language Processing in simple terms.",
    max_tokens=100
)

print(response["choices"][0]["text"])
