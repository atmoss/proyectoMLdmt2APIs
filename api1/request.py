import requests
import json

url = 'http://127.0.0.1:81/api1'

#data = [[14.34, 1.68, 2.7, 25.0, 98.0, 2.8, 1.31, 0.53, 2.7, 13.0, 0.57, 1.96, 660.0]]
data2 = [51, 'Female', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'No']

data = [{"Age":20,"Gender":"Female","Polyuria":"No","Polydipsia":"No","sudden weight loss":"Yes","weakness":"Yes","Polyphagia":"No","Genital thrush":"No","visual blurring":"Yes","Itching":"No","Irritability":"No","delayed healing":"No","partial paresis":"No","muscle stiffness":"No","Alopecia":"No","Obesity":"No"}]

j_data = json.dumps(data)
#print(j_data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)

