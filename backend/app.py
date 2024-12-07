from flask import Flask, render_template, jsonify
from flask_cors import CORS
from scriptData import getData

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api/users', methods=['GET'])
def get_data():
    dataApp = getData()
    return dataApp


if __name__ == "__main__":
    app.run(debug=True)