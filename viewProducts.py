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

@app.route('/<store_id>', methods = ['GET'])
def view(store_id):
    data = db.storeOwner

    for result in data.find({'_id':ObjectId(store_id)},{ '_id':0, 'storeName':0,'email':0,'password':0,'contacts':0,'location':0}):
      list.append(result)
    print(list)
    return json.dumps(list, indent=2, default=json_util.default)

app.run(debug=True)



