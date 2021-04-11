from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)

modelfile = '/api/models/final_prediction.pickle'
model = p.load(open(modelfile, 'rb'))


@app.route('/api2', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))
    print (prediction)
    return jsonify(prediction)

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5002)
    #app.run(host='0.0.0.0')
