FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
COPY rest.py rest.py
COPY binlist-data.csv binlist-data.csv
RUN pip3 install -r requirements.txt

CMD [ "python3", "rest.py" , "--host=0.0.0.0"]
