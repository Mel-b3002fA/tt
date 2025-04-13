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


""" 
from flask import Flask, request, jsonify, render_template
import ollama

app = Flask(__name__)
conversation = []

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'reply': 'Invalid message'}), 400

    user_message = data['message']
    print(f"User said: {user_message}")

    conversation.append({'role': 'user', 'content': user_message})

    try:
        response = ollama.chat(model='llama3', messages=conversation)
        reply = response['message']['content']
        print(f"LLaMA3 replied: {reply}")
    except Exception as e:
        print("Error from Ollama:", e)
        reply = "Sorry, something went wrong."

    conversation.append({'role': 'assistant', 'content': reply})
    return jsonify({'reply': reply})

if __name__ == '__main__':
   app.run(debug=True, port=5050) """


""" from flask import Flask, request, jsonify, render_template
import ollama

ollama_url = "http://localhost:http://127.0.0.1:11434//api/chat"


app = Flask(__name__)
conversation = []

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    # Validate input
    if not data or 'message' not in data:
        return jsonify({'reply': 'Invalid message'}), 400

    user_message = data['message']
    print(f"User said: {user_message}")

    # Append user message to conversation
    try:
        # Send full conversation to Ollama
        response = ollama.chat(
            model='llama3',
            messages=conversation
        )
        reply = response['message']['content']
        print(f"LLaMA3 replied: {reply}")

        # Append AI reply to conversation
        conversation.append({'role': 'assistant', 'content': reply})
        return jsonify({'reply': reply})

    except Exception as e:
        # Catch errors and return a fallback response
        print("Error from Ollama:", e)
        return jsonify({'reply': "Sorry, something went wrong connecting to the model."}), 500

if __name__ == '__main__':
    app.run(debug=True)


 """

from flask import Flask, request, jsonify, render_template
import ollama

# Set the base URL for Ollama (Make sure Ollama is running on the correct port)
ollama_url = "http://localhost:11434/api/chat"

app = Flask(__name__)
conversation = []

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    # Validate input
    if not data or 'message' not in data:
        return jsonify({'reply': 'Invalid message'}), 400

    user_message = data['message']
    print(f"User said: {user_message}")

    # Append user message to conversation
    conversation.append({'role': 'user', 'content': user_message})

    try:
        # Send the conversation history (including user input) to Ollama
        response = ollama.chat(
            model='llama3',
            messages=conversation
        )

        # Check if the response has the expected structure
        if 'message' in response and 'content' in response['message']:
            reply = response['message']['content']
            print(f"Joi replied: {reply}")
            
            # Append AI reply to conversation
            conversation.append({'role': 'assistant', 'content': reply})

            return jsonify({'reply': reply})

        else:
            print("Error: Unexpected response format")
            return jsonify({'reply': "Sorry, something went wrong with the model's response."}), 500

    except Exception as e:
        # Catch errors and return a fallback response
        print("Error from Ollama:", e)
        return jsonify({'reply': "Sorry, something went wrong connecting to the model."}), 500
""" 
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Running on port 5001 (or any other available port) """
""" if __name__ == '__main__':
    import socket

    def find_free_port():
        s = socket.socket()
        s.bind(('', 0))  # Bind to any free port
        port = s.getsockname()[1]
        s.close()
        return port

    port = find_free_port()
    print(f"Running on free port: {port}")
    app.run(debug=True, port=port)
 """
if __name__ == '__main__':
    import sys

    port = 5000  # default
    if len(sys.argv) > 1 and sys.argv[1].startswith('--port='):
        port = int(sys.argv[1].split('=')[1])

    app.run(debug=True, port=port)
