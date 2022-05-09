import pymongo
from pymongo import MongoClient
import json
from bson import ObjectId, json_util
from bson.json_util import dumps
from flask import Flask, render_template, jsonify , Response, request


app=Flask(__name__)
list=[]
try:
  client = MongoClient(host="localhost", port=27017)
  db = client.Agrosnap
  client.server_info()
except:
  print('ERROR')

@app.route('/<id>', methods = ['GET'])
def view(id):
    data = db.storeOwner

    result = data.find_one({'_id':ObjectId(id)},{'_id':0,"email":0, "password":0})
    print(result)
    return json.dumps(result, indent=4, default=json_util.default)

    
app.run(debug=True)