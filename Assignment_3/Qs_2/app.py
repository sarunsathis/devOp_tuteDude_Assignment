from flask import Flask, render_template, request
from datetime import datetime
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGO_URI")
client = pymongo.MongoClient(uri)
db = client.test_database
collection = db.test_collection

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
        collection.insert_one(user_data)
        return render_template('thankYou.html', name=name, email=email, time=time_str, date=date_str)
    except Exception as e:
        return f"An error occurred: {e}"
   

if __name__ == '__main__':
    app.run(debug=True)