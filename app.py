from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Render! This is my Flask app."

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello, this is some data from the Flask app!"})

if __name__ == '__main__':
    app.run(debug=True)
