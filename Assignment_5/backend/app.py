from flask import Flask, jsonify, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask API!")

@app.route('/signUp/updateData', methods=['POST'])
def signUpSubmit():
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        now = datetime.now()
        time_str = now.strftime("%H:%M")
        date_str = now.strftime("%A, %d-%b-%y")
        user_data = {
            'status': 'success',
            'name': name,
            'email': email,
            'password': password,
            'time': time_str,
            'date': date_str
        }
        return user_data
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)