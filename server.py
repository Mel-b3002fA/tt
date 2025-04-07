""" from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
model = pipeline("text-generation", model="gpt2") """


""" @app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    response = model(data["input"], max_length=100)
    return jsonify({"response": response[0]["generated_text"]}) """

""" @app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    response = model(user_input, max_length=100, num_return_sequences=1)[0]["generated_text"]
    return jsonify({"response": response})  """

""" @app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    return jsonify({"response": f"You said: {data['message']}"}) """

""" 
if __name__ == "__main__":
    app.run(port=5000)
 """

""" 
from flask import Flask, request, jsonify
from transformers import pipeline

# Load the model from Hugging Face
model = pipeline("text-generation", model="gpt2")
`aa222
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    # Get the user's message from the POST request
    data = request.get_json()
    message = data['message']

    # Use the Hugging Face model to generate a response
    response = model(message, max_length=50, num_return_sequences=1)
    
    return jsonify({"response": response[0]['generated_text']})

if __name__ == "__main__":
    app.run(debug=True) """

""" 
import ollama 

while True:
    user = input('You: ')
    if user.lower() == 'bye':
        print('Goodbye!')
        break

    response = ollama.chat(model= 'llama3', messages=[
        {'role': 'user', 'content': user}
    ])
print('Joi:', response['message']['content'])
print(response) """

""" import ollama

response = ollama.chat(model='llama3', messages=[
    {'role': 'user', 'content': 'Hello!'}
])

print("Model response:", response['message']['content']) """


import ollama

conversation = []

print("You can start chatting with LLaMA3. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break

    conversation.append({'role': 'user', 'content': user_input})
    response = ollama.chat(model='llama3', messages=conversation)

    reply = response['message']['content']
    print("LLaMA3:", reply)

    conversation.append({'role': 'assistant', 'content': reply})

