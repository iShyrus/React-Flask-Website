from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route('/members', methods =['GET'])
def members():
    return jsonify({"members": "hello"})



CORS(app)
if __name__ == '__main__':
    app.run()
