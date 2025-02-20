from flask import Flask, jsonify
import json
import requests

app4 = Flask(__name__)

@app4.route('/<string:municipioid>/<parametro1>/<parametro2>', methods=['GET'])
def get_combined(municipioid, parametro1, parametro2):
    with open('municipio.json', 'r') as file:
        json_data = json.load(file)
        
    parametro1 = parametro1.lower()
    parametro2 = parametro2.lower()

    urlGEO = "http://localhost:5000/" + str(municipioid) + "/geo"
    urlMETEO = "http://localhost:5001/" + str(municipioid) + "/meteo"
    if str(json_data.get("municipioid")) == municipioid:
        if parametro1 == 'geo' and parametro2 == 'meteo':
            try:
                response = requests.get(urlGEO)
                response.raise_for_status()
                response2 = requests.get(urlMETEO)
                response2.raise_for_status()

                data = response.json()
                data2 = response2.json()

                return jsonify(data, data2)

            except requests.exceptions.RequestException as e:
                return jsonify({'error': str(e)}), 500
            except ValueError:
                return jsonify({'error': 'Error parsing JSON response'}), 500

        elif parametro1 == 'meteo' and parametro2 == 'geo':
            try:
                response = requests.get(urlMETEO)
                response.raise_for_status()
                response2 = requests.get(urlGEO)
                response2.raise_for_status()

                data = response.json()
                data2 = response2.json()

                return jsonify(data, data2)

            except requests.exceptions.RequestException as e:
                return jsonify({'error': str(e)}), 500
            except ValueError:
                return jsonify({'error': 'Error parsing JSON response'}), 500

        else:
            return jsonify({'error': 'Parámetro no válido'}), 404

    return jsonify({'error': 'Municipio no encontrado'}), 404

if __name__ == '__main__':
    app4.run(port=5003)
