from flask import Flask, jsonify, request
from flask_cors import CORS

# import sys
# sys.path.append('../')

# from db import get_natural_disaster

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['GET', 'POST'])
def receive_data():
    data = request.data.decode("utf-8")
    print("Hi")

    if not data:
        return jsonify({"error": "No data found"}), 404

    return jsonify({"data": data}), 200

if __name__ == '__main__':
    app.run()
