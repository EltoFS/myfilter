from flask import Flask
from openai import OpenAI
from myfilter.prompts import Prompt

client = OpenAI()

app = Flask(__name__)

def request_message(prompt):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": str(prompt)}
    ]
    )
    return completion

@app.route("/")
def hello_world():
    message = ""
    prompt = Prompt.good_guy(message=message)
    print (prompt)
    completion = request_message(prompt)
    return "<p>"+str(completion.choices[0].message.content)+"</p>"