from flask import Flask

app = Flask(__name__)

def read_csv_file_convert_to_json(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        json_data = []
        for line in lines[1:]:
            values = line.strip().split(',')
            entry = {headers[i]: values[i] for i in range(len(headers))}
            json_data.append(entry)
    return json_data

@app.route('/api')
def api_root():
    jsonArr = read_csv_file_convert_to_json('Assignment_3/Qs_1/dummy_data.csv')
    return {"data": jsonArr}

@app.route('/')
def home():
    return "Welcome to the Home Page!"

if __name__ == "__main__":
    app.run(debug=True)