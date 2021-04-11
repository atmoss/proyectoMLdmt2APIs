from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import numpy as np
import pickle as p
import json
import pandas as pd


app = Flask(__name__)


#data = pd.read_csv("/media/manchi/Respaldo1/Proyectos/Bigdata/diabetes/diabetes_data_upload.csv")
data = pd.read_csv("/api/diabetes_data_upload.csv")

modelfile = '/api/models/tree_diab_01.pickle'
model = p.load(open(modelfile, 'rb'))

#data = data.sample(frac=1) ##randomize

categoricals = ['Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring', 'Itching', 'Irritability',
                'delayed healing', 'partial paresis', 'muscle stiffness', 'Alopecia', 'Obesity']

#saco Na
d2 = data.dropna()
##aplicar one hot eeee. No hay nas
d3 = d2.drop('class', 1)


@app.route('/api1', methods=['POST'])
def makecalc():
    d4 = request.get_json()
    #lo que recibo lo transformo a dataframe
    d5 = pd.DataFrame.from_dict(d4, orient='columns')
    #lo agrego a una dataframe para hacer el dummy pero con las categorias presentes
    d11 = d3.append(d5, ignore_index=True)

    d12 = pd.get_dummies(d11, columns=categoricals, dummy_na=True)

    #ahor extraigo esa ulia columna formateada

    ddd = model.predict(d12[-1:])

    prediction = np.array2string(ddd)
    print (prediction)
    return jsonify(prediction)

if __name__ == '__main__':
    
    modelfile = '/api/models/tree_diab_01.pickle'
    #try:
        #model = p.load(open(modelfile, 'rb'))
    #except:
    #    print("aaaa")    

  #  app.run(debug=True, host='0.0.0.0', port=5001)
    app.run(debug=True, host='127.0.0.1', port=5001)

@app.route('/test')
def index():
    return 'Hello worldssss!'
@app.route('/')
def welcome():
    return render_template('index.html')


