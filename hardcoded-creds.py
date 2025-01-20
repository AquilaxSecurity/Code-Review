from flask import Flask, request, jsonify

app = Flask(__name__)

USERNAME = "Admin"
PASSWORD = "123456"

@app.route('/')
def home():
    return "Welcome to the App!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == USERNAME and password == PASSWORD:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
