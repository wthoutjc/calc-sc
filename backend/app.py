from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

#Cambio de base
from Cambio_Base import CambioBase

#Herramientas
import json       

app = Flask(__name__)
CORS(app)

#cambio_base = CambioBase()

@app.route("/calc", methods=['POST'])
def hello_world():
    if request.data:
        data_raw = request.data.decode("utf-8")
        json_data = json.loads(data_raw) #print(json_data) Debug de datos entrantes

        baseO = json_data['baseO']
        baseC = json_data['baseC']
        numero = json_data['input']

        cambio_base = CambioBase(baseO, numero, baseC)
        

        if cambio_base.base_n_10() == None:
            data, success = cambio_base.base_10_m()
            if success:
                return make_response(jsonify({"results": data}), 200)
            return make_response(jsonify({"results": data}), 500)
        else:
           return make_response(jsonify({"results": cambio_base.base_n_10()[0]}), 500) 
    return make_response(jsonify({"results": 'Falló la comunicación con el servidor'}), 500)

if __name__ == '__main__':
    app.run(debug=True)