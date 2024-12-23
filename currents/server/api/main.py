from flask import Flask, jsonify, request
from flask_cors import CORS
from db import get_results
from db import get_advanced_query1 
from db import get_advanced_query2
from db import get_advanced_query3
from db import get_advanced_query4
from db import sessions_query

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
        elif data.get('sessions') == 'yes':
            return jsonify({"data": sessions_query()}), 200

        return jsonify({"data": get_results(data.get('min_latitude'), data.get('max_latitude'), data.get('min_longitude'), data.get('max_longitude'))}), 200
    
    if request.method == 'GET':
        return jsonify({"data": "hi"}), 200
    
if __name__ == '__main__':
    app.run(debug=True)