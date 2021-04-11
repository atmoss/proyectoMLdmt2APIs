import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
#from sklearn.externals import joblib
import joblib
import pickle
import pickle as p


data = pd.read_csv("/media/manchi/Respaldo1/Proyectos/Bigdata/diabetes/diabetes_data_upload.csv")

data = data.sample(frac=1) ##randomize


#saco Na
d2 = data.dropna()
##aplicar one hot eeee. No hay nas
d3 = d2.drop('class', 1)

categoricals = []

for col, col_type in d3.dtypes.iteritems():
     if col_type == 'O':
          categoricals.append(col)

data = pd.get_dummies(d3, columns=categoricals, dummy_na=True)

#vuelvo a poner 'class'
data['class'] = d2['class']

X_train = data[:-50]
X_test = data[-50:]

y_train = X_train['class']
y_test = X_test['class']

X_train = X_train.drop('class',1)
X_test = X_test.drop('class',1)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("accuracy_score: %.2f"
      % accuracy_score(y_test, y_pred))


pickle.dump(clf, open('models/tree_diab_01.pickle', 'wb'))


#necesito los nombre one hot encoder para usarlos en la entrada de datos
mc = list(X_train.columns)

pickle.dump(mc, open('models/mc.pickle', 'wb'))
aaa = 'models/mc.pickle'
mc2 = p.load(open(aaa, 'rb'))



























