#!/usr/bin/env python3

from flask import Flask
import csv
import re 

app = Flask(__name__)
csvdata  = {}
with open('binlist-data.csv') as csvfile :
    headers = csvfile.readline().split(",")[1:]
    csvrows = csv.reader(csvfile)
    for row in csvrows :
        csvdata[row[0]] = {k:v  for k, v in zip(headers, row[1:])}
    
@app.route('/')
def index():
    return "<h1>Welcome to the Bin Lookup service</h1>"

@app.route("/lookup/<card>")
def lookup(card) :
    card = re.sub("\s", "", card)
    card = card[0:6]
    if (card in csvdata) : return csvdata[card]
    return "Not found"
    

if __name__ == '__main__' :
    app.run(host="0.0.0.0")
