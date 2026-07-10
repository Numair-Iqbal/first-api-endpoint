from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Numair Iqbal's first API!"})

@app.route("/status")
def status():
    return jsonify({"status": "ok", "developer": "Numair Iqbal", "role": "Backend AI Engineering Intern"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)