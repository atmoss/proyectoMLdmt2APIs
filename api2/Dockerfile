FROM python:3.6
#FROM python:2.7


#update
RUN apt-get update
RUN pip3 install --upgrade pip

#install requirements
COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip3 install -r requirements.txt
#RUN pip install -r requirements.txt

#copy app
COPY . /api
COPY ./models/final_prediction.pickle /api/models/final_prediction.pickle
WORKDIR /

CMD ["gunicorn", "-w", "3", "-b", ":5002", "-t", "360", "--reload", "api.wsgi:app"]
