import pymongo
from pymongo import MongoClient
import json
from bson import ObjectId, json_util
from bson.json_util import dumps
from flask import Flask, render_template, jsonify , Response, request

app=Flask(__name__)

try:
  client = MongoClient(host="localhost", port=27017)
  db = client.Agrosnap 
  client.server_info()
except:
  print('ERROR')

@app.route('/<subName>', methods = ['GET'])
def get_plant(subName):
  data = db.plants
  result = data.find_one({'name' })
  print(result)
  return json.dumps(result, indent=4, default = json_util.default)


app.run(debug=True)