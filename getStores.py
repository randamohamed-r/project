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
    data = db.storeOwner

    for result in data.find({},{ 'email':0 , 'contacts':0, 'location':0, 'password':0, 'products':0}):
      list.append(result)
    print(list)
    return json.dumps(list, indent=4, default=json_util.default)

app.run(debug=True)