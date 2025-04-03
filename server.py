from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
model = pipeline("text-generation", model="gpt2")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    response = model(data["input"], max_length=100)
    return jsonify({"response": response[0]["generated_text"]})

if __name__ == "__main__":
    app.run(port=5000)
