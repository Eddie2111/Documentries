## modules ##
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
## modules ##

## database ##
client = MongoClient("mongodb://localhost:27017/hospital")
db = client['dbname']
## database ##

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/data', methods=['GET'])
def data():
    return jsonify({'data': [1, 2, 3, 4, 5]})

if __name__ == '__main__':
    app.run(debug=True)