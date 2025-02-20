from flask import Flask, jsonify
import requests

app2 = Flask(__name__)


@app2.route('/<string:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    url = "https://www.el-tiempo.net/api/json/v2/provincias/04/municipios/" + str(municipioid)
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        meteo_data = {
            'temperatura': data.get('temperatura_actual'),
            'temperatura_max': data.get('temperaturas').get('max'),
            'temperatura_min': data.get('temperaturas').get('min'),
            'humedad': data.get('humedad'),
            'viento': data.get('viento'),
            'precipitacion': data.get('precipitacion'),
            'lluvia': data.get('lluvia')
        }
        
        return jsonify(meteo_data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except ValueError:
        return jsonify({'error': 'Error parsing JSON response'}), 500

if __name__ == '__main__':
    app2.run(port=5001)
    
