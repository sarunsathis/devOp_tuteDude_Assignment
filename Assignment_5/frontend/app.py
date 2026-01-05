from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__, template_folder='.')
 
@app.route('/')
def index_home():
    return render_template('index.html')

@app.route('/signUp')
def signUp():
   return render_template("signUp.html")

@app.route('/signUp/submit', methods=['POST'])
def signUpSubmit():
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        now = datetime.now()
        time_str = now.strftime("%H:%M")
        date_str = now.strftime("%A, %d-%b-%y")

        user_data = {
            'name': name,
            'email': email,
            'password': password,
            'time': time_str,
            'date': date_str
        }
        
        response = requests.post("http://backend:5000/signUp/updateData", json=user_data)
        if response.status_code != 200:
            return f"Failed to store user data: {response.text}"
        
        return render_template('thankYou.html', name=name, email=email, time=time_str, date=date_str)
    except Exception as e:
        return f"An error occurred: {e}"
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)