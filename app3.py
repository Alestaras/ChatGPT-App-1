from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this import
import os
import requests
import openai

app3 = Flask(__name__)
CORS(app3)  # Add this line to enable CORS for all routes

# Replace with your OpenAI API key
openai.api_key = "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"

@app3.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json['message']

    # Interact with the ChatGPT API using the user_message
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{user_message}",
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.4,
    )

    chatgpt_message = response.choices[0].text.strip()
    return jsonify({"message": chatgpt_message})

if __name__ == "__main__":
    app3.run(debug=True)
