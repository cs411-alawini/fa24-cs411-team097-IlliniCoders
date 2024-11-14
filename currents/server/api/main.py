from flask import Flask, jsonify, request
from flask_cors import CORS

# import sys
# sys.path.append('../')

from db import get_natural_disaster

app = Flask(__name__)
CORS(app)

res = get_natural_disaster('Joaquin')
# @app.route('/', methods=['GET','POST'])
# def receive_data():
#     # data = request.data.decode("utf-8")
#     # if not data:
#     #     return jsonify({"error": "main.py: No data found"}), 404
#     res = get_natural_disaster('Joaquin')
#     print('res')
#     return res, 200
#     # return jsonify({"data": data}), 200

if __name__ == '__main__':
    app.run()
