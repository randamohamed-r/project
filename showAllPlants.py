import pymongo
from pymongo import MongoClient
import json
from bson import ObjectId, json_util
from bson.json_util import dumps
from flask import Flask, render_template, jsonify , Response, request

list = [ ]
app=Flask(__name__)

try:
  client = MongoClient(host="localhost", port=27017)
  db = client.Agrosnap
  client.server_info()
except:
  print('ERROR')

@app.route('/', methods = ['GET'])
def view():
    data = db.plants

    for result in data.find({},{ 'overview':0 , 'soil_characteristics':0, 'best_ways_for_agriculture':0, 'harvest':0, 'agricultural_methods':0, 
    'growth_factors':0, 'care_about_plants':0, 'seed_extraction':0, 'irrigation':0, 'fertilizers':0, 'scientific classification':0}):
      list.append(result)
    print(list)
    return json.dumps(list, indent=4, default=json_util.default)

app.run(debug=True)