import os
import openai
import constant

OPENAI_API_KEY = constant.open_ai_key
# Load your API key from an environment variable or secret management service
openai.api_key = OPENAI_API_KEY

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

print(chat_completion)