from flask import Flask, jsonify, request
from flask_cors import CORS
from db import get_natural_disaster 
from db import get_advanced_query1 
from db import get_advanced_query2
from db import get_advanced_query3
from db import get_advanced_query4

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/data', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
    
        if not data:
            return jsonify({"error": "No data found,"}), 404
    
        elif data.get('advanced_query') == '1':
            print("here")
            return jsonify({"data": get_advanced_query1()}), 200
        elif data.get('advanced_query') == '2':
            print("here")
            return jsonify({"data": get_advanced_query2()}), 200
        elif data.get('advanced_query') == '3':
            print("here")
            return jsonify({"data": get_advanced_query3()}), 200
        elif data.get('advanced_query') == '4':
            print("here")
            return jsonify({"data": get_advanced_query4()}), 200
        # print("here outside")
        return jsonify({"data": get_natural_disaster(data.get('min_latitude'), data.get('max_latitude'), data.get('min_longitude'), data.get('max_longitude'))}), 200
    
    if request.method == 'GET':
        return jsonify({"data": "hi"}), 200
    
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS
from db import get_natural_disaster 
from db import get_advanced_query1 
from db import get_advanced_query2
from db import get_advanced_query3
from db import get_advanced_query4

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/data', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        data = request.get_json()
    
        if not data:
            return jsonify({"error": "No data found,"}), 404

        elif data.get('advanced_query') == '1':
            return jsonify({"data": get_advanced_query1()}), 200
        elif data.get('advanced_query') == '2':
            return jsonify({"data": get_advanced_query2()}), 200
        elif data.get('advanced_query') == '3':
            return jsonify({"data": get_advanced_query3()}), 200
        elif data.get('advanced_query') == '4':
            return jsonify({"data": get_advanced_query4()}), 200

        return jsonify({"data": get_natural_disaster(data.get('min_latitude'), data.get('max_latitude'), data.get('min_longitude'), data.get('max_longitude'))}), 200
    
    if request.method == 'GET':
        return jsonify({"data": "hi"}), 200
    
if __name__ == '__main__':
    app.run(debug=True)