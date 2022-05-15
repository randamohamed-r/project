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

@app.route('/', methods = ['GET'])
def get_plant():
  req_Json= request.json
  store_name=req_Json['store_name']
  
  regex = ".*" + store_name + ".*"

  for result in db.storeOwner.find( {"storeName" : {'$regex' : regex, "$options":"i"}} ):
      list.append(result)
  print(list)
  return json.dumps(list, indent=4, default = json_util.default)


app.run(debug=True)