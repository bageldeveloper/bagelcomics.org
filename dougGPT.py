import openai_secret_manager
import open ai
from flask import Flask, request, jsonify

secrets = openai_secrets_manager.get_secret("openai")
openai.api_key = secrets["api_key"]

app = Flask(_name_)

model = "text-davinci-002"
temperature = 0.5
max_tokens = 50

def chat():
  user_message = request.json['message']
  
  response = openai.Completion.create(
    engine = model,
    prompt = user_message,
    tempature = tempature,
    max_tokens = max_tokens
  )
    
response_text = response["choices"][0]["text"].strip()
return json(response_text)

if _name_ == '_main_':
  app.run(debug = True)
