from flask import Flask, jsonify
import json

app3 = Flask(__name__)

@app3.route('/<string:municipioid>/demo', methods=['GET'])
def get_geo(municipioid):
    with open('municipio.json', 'r') as file:
        json_data = json.load(file)

        if str(json_data.get("municipioid")) == municipioid:
            return jsonify(json_data)

    return jsonify({'error': 'Municipio no encontrado'}), 404


if __name__ == '__main__':
    app3.run(port=5002)
      
      
