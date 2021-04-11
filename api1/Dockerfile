FROM python:3.6
#FROM python:2.7


#update
RUN apt-get update

#install requirements
COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip3 install -r requirements.txt
#RUN pip install -r requirements.txt

#copy app
COPY . /api
COPY ./models/tree_diab_01.pickle /api/models/tree_diab_01.pickle
COPY ./diabetes_data_upload.csv /api/diabetes_data_upload.csv
#COPY ./static/index.html /api/static/index.html
WORKDIR /

CMD ["gunicorn", "-w", "3", "-b", ":5001", "-t", "360", "--reload", "api.wsgi:app"]
