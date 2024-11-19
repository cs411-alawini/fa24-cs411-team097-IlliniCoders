from flask import Flask, jsonify, request
from flask_cors import CORS
from db import get_natural_disaster 
# import sys
# sys.path.append('../')

# from db import get_natural_disaster

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        #data = request.data.decode("utf-8")
        data = request.get_json()
        print(data)
    
        if not data:
            return jsonify({"error": "No data found,"}), 404
    

        return jsonify({"data": get_natural_disaster(data.get("query"))}), 200
    
    if request.method == 'GET':
        return jsonify({"data": "hi"}), 200
    
if __name__ == '__main__':
    app.run(debug=True)