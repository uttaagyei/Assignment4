from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/covid')
def tracker():
    data = dict(
        total=1000,
        active=100,
        recovered=800,
        deaths=50,
        ncases=50
    )
    return jsonify(data)